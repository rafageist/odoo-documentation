#!/usr/bin/env python
import argparse
import json
import re
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


DEFAULT_PATTERN = r"(?i)\bodoo\s*19\b|\bodoo19\b|\bv19\b"


@dataclass
class Message:
    id: int
    export_name: str
    date: str
    date_unixtime: int
    author: str
    text: str
    reply_to_message_id: int | None


def flatten_text(payload) -> str:
    if isinstance(payload, str):
        return payload
    if isinstance(payload, list):
        parts = []
        for item in payload:
            if isinstance(item, dict):
                parts.append(str(item.get("text", "")))
            else:
                parts.append(str(item))
        return "".join(parts)
    if payload is None:
        return ""
    return str(payload)


def iter_exports(root: Path) -> Iterable[Path]:
    return sorted(root.rglob("result.json"))


def load_messages(root: Path) -> dict[int, Message]:
    messages: dict[int, Message] = {}
    for export_path in iter_exports(root):
        data = json.loads(export_path.read_text(encoding="utf-8"))
        export_name = export_path.parent.name
        for raw in data.get("messages", []):
            if raw.get("type") != "message":
                continue
            message_id = raw.get("id")
            if message_id is None:
                continue
            normalized = Message(
                id=message_id,
                export_name=export_name,
                date=raw.get("date", ""),
                date_unixtime=int(raw.get("date_unixtime", "0")),
                author=raw.get("from", "?"),
                text=flatten_text(raw.get("text", "")).strip(),
                reply_to_message_id=raw.get("reply_to_message_id"),
            )
            current = messages.get(message_id)
            if current is None or normalized.date_unixtime >= current.date_unixtime:
                messages[message_id] = normalized
    return messages


def thread_root_id(message_id: int, messages: dict[int, Message]) -> int:
    seen = set()
    current_id = message_id
    while current_id not in seen:
        seen.add(current_id)
        current = messages.get(current_id)
        if not current or not current.reply_to_message_id or current.reply_to_message_id not in messages:
            return current_id
        current_id = current.reply_to_message_id
    return message_id


def collect_descendants(root_id: int, children: dict[int, list[int]]) -> list[int]:
    ordered: list[int] = []
    stack = [root_id]
    while stack:
        current = stack.pop()
        for child_id in children.get(current, []):
            ordered.append(child_id)
            stack.append(child_id)
    return ordered


def build_markdown(messages: dict[int, Message], pattern: re.Pattern[str], after: str | None, limit: int) -> str:
    children: dict[int, list[int]] = defaultdict(list)
    for message in messages.values():
        if message.reply_to_message_id in messages:
            children[message.reply_to_message_id].append(message.id)
    for child_ids in children.values():
        child_ids.sort(key=lambda child_id: messages[child_id].date_unixtime)

    candidates = []
    for message in sorted(messages.values(), key=lambda item: item.date_unixtime):
        if after and message.date[:10] < after:
            continue
        if pattern.search(message.text):
            candidates.append(message)

    root_ids = []
    seen_roots = set()
    for message in candidates:
        root_id = thread_root_id(message.id, messages)
        if root_id not in seen_roots:
            seen_roots.add(root_id)
            root_ids.append(root_id)

    lines = [
        "# Odoo 19 Telegram Candidate Threads",
        "",
        f"- Messages scanned: {len(messages)}",
        f"- Explicit Odoo 19 mentions: {len(candidates)}",
        f"- Distinct candidate threads: {len(root_ids)}",
    ]
    if candidates:
        first = min(candidates, key=lambda item: item.date_unixtime)
        lines.append(f"- Earliest explicit mention: {first.date} in `{first.export_name}` (message `{first.id}`)")
    lines.extend(["", "## Threads", ""])

    for root_id in root_ids[:limit]:
        root = messages[root_id]
        descendant_ids = collect_descendants(root_id, children)
        thread_ids = [root_id] + descendant_ids
        thread_messages = sorted((messages[item_id] for item_id in thread_ids), key=lambda item: item.date_unixtime)
        lines.append(f"### {root.date} | {root.author} | `{root.export_name}` | root `{root.id}`")
        lines.append("")
        for item in thread_messages:
            body = " ".join(item.text.split())
            lines.append(f"- `{item.id}` {item.date} {item.author}: {body[:500]}")
        lines.append("")
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description="Extract candidate Odoo 19 threads from Telegram exports.")
    parser.add_argument("--root", default=r"D:\Odoo Developers", help="Directory that contains Telegram export folders.")
    parser.add_argument("--pattern", default=DEFAULT_PATTERN, help="Regex used to detect candidate Odoo 19 messages.")
    parser.add_argument("--after", help="Only keep matches on or after YYYY-MM-DD.")
    parser.add_argument("--limit", type=int, default=50, help="Maximum number of threads to include in the report.")
    parser.add_argument("--output", help="Write markdown output to this path instead of stdout.")
    args = parser.parse_args()

    root = Path(args.root)
    if not root.exists():
        raise SystemExit(f"Root path does not exist: {root}")

    messages = load_messages(root)
    report = build_markdown(messages, re.compile(args.pattern), args.after, args.limit)
    if args.output:
        output = Path(args.output)
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(report, encoding="utf-8")
    else:
        print(report)


if __name__ == "__main__":
    main()
