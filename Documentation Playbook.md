---
tags: [meta, playbook]
status: active
---
# Documentation Playbook

## Objectives
- Keep notes stylistically consistent.
- Ground every statement in source code and data artefacts.
- Encourage deliberate use of diagrams (PlantUML, Mermaid) to capture structure and flow.

## Workflow
1. **Scope selection** - start from a folder index and ensure its children are linked.
2. **Template instantiation** - duplicate the relevant template in `[[Templates/]]`.
3. **Code excavation** - review Python, XML, CSV, and test assets; capture file+line references.
4. **Narrative drafting** - describe business context, invariants, and cross-module effects.
5. **Visualisation** - add at least one diagram explaining structure or sequence.
6. **Linking** - connect to parent index, sibling modules, and related concepts.
7. **Review** - update `[[Changelog]]` and, when appropriate, `[[Comparisons/Index]]`.

## Conventions
- **Tags:** use `#v18`, `#v19`, `#core`, `#community`, `#enterprise`, `#business`, `#technical` as relevant.
- **References:** prefer the format `` `odoo/addons/base/models/res_partner.py:798` `` for code.
- **Linking:** when a note mentions another concept, ensure a `[[wikilink]]` exists (create stubs if needed).
- **Sections:** finish each index or model note with a `## Navigation` block (parent + children + peers).

## Iteration roadmap
| Phase | Focus | Representative notes |
|-------|-------|-----------------------|
| Wave 1 | Core master data (`res.partner`, `res.company`, `res.users`) | `[[Odoo 18/Core/Master Data/res_partner.md]]` |
| Wave 2 | Core processes (Sales, Accounting, Inventory) | `[[Odoo 18/Core/Processes/Index]]` |
| Wave 3 | Community modules with heavy inheritance (CRM, Account) | TODO |
| Wave 4 | Enterprise exclusives (Advanced Finance, Operations) | TODO |
| Wave 5 | Cross-version deltas and migration scripts | `[[Comparisons/Index]]` |

## Quality gates
- Cross-check that every method documented cites its source file.
- Run supporting tests or note missing coverage when behaviour is critical.
- Capture open questions in each note to drive follow-up sprints.

## Navigation
- **Parent:** `[[Welcome]]`
- **Related:** `[[Templates/Module Documentation Template]]`, `[[Changelog]]`
