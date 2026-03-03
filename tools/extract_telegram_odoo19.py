#!/usr/bin/env python
import argparse
import json
import re
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


DEFAULT_PATTERN = r"(?i)\bodoo\s*19\b|\bodoo19\b|\bv19\b"
TOPIC_PATTERNS = {
    "website": r"(?i)\bwebsite\b|website builder|header template|footer template|snippet|theme customize",
    "website_sale": r"(?i)\bwebsite_sale\b|website sale|\becommerce\b|/shop\b|cart|checkout|product detail",
    "owl": r"(?i)\bowl\b|@odoo/owl|public\.interactions|website-plugins|Component",
    "security": r"(?i)record rule|record rules|ir\.rule|access rule|access rights|acl|security",
    "import_export": r"(?i)\bimport\b|\bexport\b|csv|xlsx|external id|base_import",
}


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


def normalize_text(text: str) -> str:
    return " ".join(text.split())


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
                text=normalize_text(flatten_text(raw.get("text", "")).strip()),
                reply_to_message_id=raw.get("reply_to_message_id"),
            )
            current = messages.get(message_id)
            if current is None or normalized.date_unixtime >= current.date_unixtime:
                messages[message_id] = normalized
    return messages


def build_children(messages: dict[int, Message]) -> dict[int, list[int]]:
    children: dict[int, list[int]] = defaultdict(list)
    for message in messages.values():
        if message.reply_to_message_id in messages:
            children[message.reply_to_message_id].append(message.id)
    for child_ids in children.values():
        child_ids.sort(key=lambda child_id: messages[child_id].date_unixtime)
    return children


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


def compile_topic_filters(topic_names: list[str], custom_topic_patterns: list[str]) -> list[tuple[str, re.Pattern[str]]]:
    compiled = []
    for name in topic_names:
        compiled.append((name, re.compile(TOPIC_PATTERNS[name])))
    for item in custom_topic_patterns:
        if "=" not in item:
            raise SystemExit(f"Invalid --topic-pattern value: {item}. Expected NAME=REGEX.")
        name, pattern = item.split("=", 1)
        name = name.strip()
        pattern = pattern.strip()
        if not name or not pattern:
            raise SystemExit(f"Invalid --topic-pattern value: {item}. Expected NAME=REGEX.")
        compiled.append((name, re.compile(pattern)))
    return compiled


def match_topics(text: str, topics: list[tuple[str, re.Pattern[str]]]) -> list[str]:
    return [name for name, pattern in topics if pattern.search(text)]


def build_thread_report(
    messages: dict[int, Message],
    pattern: re.Pattern[str],
    after: str | None,
    limit: int,
    topics: list[tuple[str, re.Pattern[str]]],
) -> dict:
    children = build_children(messages)

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

    first_candidate = min(candidates, key=lambda item: item.date_unixtime) if candidates else None
    thread_payloads = []
    for root_id in root_ids:
        descendant_ids = collect_descendants(root_id, children)
        thread_ids = [root_id] + descendant_ids
        thread_messages = sorted((messages[item_id] for item_id in thread_ids), key=lambda item: item.date_unixtime)
        combined_text = "\n".join(item.text for item in thread_messages)
        matched_topics = sorted(set(match_topics(combined_text, topics)))
        if topics and not matched_topics:
            continue

        message_payloads = []
        explicit_match_count = 0
        for item in thread_messages:
            is_explicit_match = bool(pattern.search(item.text))
            if is_explicit_match:
                explicit_match_count += 1
            message_payloads.append({
                "id": item.id,
                "date": item.date,
                "author": item.author,
                "export_name": item.export_name,
                "reply_to_message_id": item.reply_to_message_id,
                "explicit_match": is_explicit_match,
                "topic_hits": match_topics(item.text, topics),
                "text": item.text,
            })

        thread_payloads.append({
            "root_id": root_id,
            "root_date": thread_messages[0].date,
            "root_author": thread_messages[0].author,
            "root_export_name": thread_messages[0].export_name,
            "message_count": len(thread_messages),
            "explicit_match_count": explicit_match_count,
            "matched_topics": matched_topics,
            "messages": message_payloads,
        })

    report = {
        "summary": {
            "messages_scanned": len(messages),
            "explicit_odoo19_mentions": len(candidates),
            "distinct_candidate_threads": len(root_ids),
            "topic_filtered_threads": len(thread_payloads),
            "topics_requested": [name for name, _pattern in topics],
            "after": after,
        },
        "threads": thread_payloads[:limit],
    }
    if first_candidate:
        report["summary"]["earliest_explicit_mention"] = {
            "message_id": first_candidate.id,
            "date": first_candidate.date,
            "export_name": first_candidate.export_name,
            "author": first_candidate.author,
        }
    return report


def build_markdown(report: dict, excerpt_length: int) -> str:
    summary = report["summary"]
    lines = [
        "# Odoo 19 Telegram Candidate Threads",
        "",
        f"- Messages scanned: {summary['messages_scanned']}",
        f"- Explicit Odoo 19 mentions: {summary['explicit_odoo19_mentions']}",
        f"- Distinct candidate threads: {summary['distinct_candidate_threads']}",
        f"- Threads after topic filter: {summary['topic_filtered_threads']}",
    ]
    if summary.get("topics_requested"):
        lines.append(f"- Topic filters: {', '.join(summary['topics_requested'])}")
    if summary.get("after"):
        lines.append(f"- Date floor: {summary['after']}")
    earliest = summary.get("earliest_explicit_mention")
    if earliest:
        lines.append(
            f"- Earliest explicit mention: {earliest['date']} in `{earliest['export_name']}` "
            f"(message `{earliest['message_id']}`)"
        )
    lines.extend(["", "## Threads", ""])

    for thread in report["threads"]:
        lines.append(
            f"### {thread['root_date']} | {thread['root_author']} | `{thread['root_export_name']}` "
            f"| root `{thread['root_id']}`"
        )
        lines.append("")
        if thread["matched_topics"]:
            lines.append(f"- Matched topics: {', '.join(thread['matched_topics'])}")
        lines.append(f"- Messages in thread: {thread['message_count']}")
        lines.append(f"- Explicit Odoo 19 matches in thread: {thread['explicit_match_count']}")
        lines.append("")
        for item in thread["messages"]:
            body = item["text"][:excerpt_length]
            lines.append(f"- `{item['id']}` {item['date']} {item['author']}: {body}")
        lines.append("")
    return "\n".join(lines)


def list_topics() -> str:
    lines = ["Available topic filters:"]
    for name, pattern in sorted(TOPIC_PATTERNS.items()):
        lines.append(f"- {name}: {pattern}")
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description="Extract candidate Odoo 19 threads from Telegram exports.")
    parser.add_argument("--root", default=r"D:\Odoo Developers", help="Directory that contains Telegram export folders.")
    parser.add_argument("--pattern", default=DEFAULT_PATTERN, help="Regex used to detect candidate Odoo 19 messages.")
    parser.add_argument("--after", help="Only keep matches on or after YYYY-MM-DD.")
    parser.add_argument("--limit", type=int, default=50, help="Maximum number of threads to include in the report.")
    parser.add_argument("--topic", action="append", choices=sorted(TOPIC_PATTERNS), default=[], help="Restrict results to predefined topic filters.")
    parser.add_argument("--topic-pattern", action="append", default=[], metavar="NAME=REGEX", help="Add a custom named topic filter.")
    parser.add_argument("--format", choices=("markdown", "json"), default="markdown", help="Output format.")
    parser.add_argument("--excerpt-length", type=int, default=500, help="Maximum characters per message in markdown output.")
    parser.add_argument("--list-topics", action="store_true", help="Print available topic filters and exit.")
    parser.add_argument("--output", help="Write output to this path instead of stdout.")
    args = parser.parse_args()

    if args.list_topics:
        print(list_topics())
        return

    root = Path(args.root)
    if not root.exists():
        raise SystemExit(f"Root path does not exist: {root}")

    messages = load_messages(root)
    topics = compile_topic_filters(args.topic, args.topic_pattern)
    report = build_thread_report(messages, re.compile(args.pattern), args.after, args.limit, topics)
    if args.format == "json":
        output_text = json.dumps(report, indent=2, ensure_ascii=False)
    else:
        output_text = build_markdown(report, args.excerpt_length)

    if args.output:
        output = Path(args.output)
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(output_text, encoding="utf-8")
    else:
        print(output_text)


if __name__ == "__main__":
    main()
