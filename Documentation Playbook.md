---
tags: [meta, playbook, v19]
status: active
---

# Documentation Playbook

## Objective
Build reliable Odoo 19 documentation that stays close to the codebase and avoids duplicated notes.

## Source hierarchy
1. Odoo 19 community source in `C:\Users\RafaelRodríguez\sources\repos\odoo19`
2. Odoo 19 enterprise source in `C:\Users\RafaelRodríguez\sources\repos\docker\odoo19-enterprise-sync\enterprise-cache\3ff6ea5148ee9e3209f05e677ba8fff51fc44d0d`
3. Tests, demo data, and manifests inside those same modules
4. `C:\Users\RafaelRodríguez\sources\repos\odoo-skills` for example patterns and explanation angles

## Structure rules
- Canonical module notes live at `Odoo 19/<Community Addons|Enterprise Addons>/<technical_name>/<technical_name>.md`.
- Category folders such as `Finance`, `HR`, `Sales`, or `Operations` contain only index notes.
- Core notes live under `Odoo 19/Core/` and should document framework behavior, shared models, and transversal processes.
- Avoid creating a second note for the same module inside a category folder.

## Writing workflow
1. Start from the relevant index page and confirm the target note does not already exist elsewhere.
2. Read the manifest, models, views, security files, data files, and tests before drafting.
3. Capture concrete evidence: source paths, model names, XML ids, menu/actions, and side effects.
4. Use the closest template from `[[Templates]]`.
5. Add the interpretation layer: business purpose, extension points, risks, and module interactions.
6. Link related modules, core topics, and category indexes with `[[wikilinks]]`.
7. Update `[[Changelog]]` when the repository structure or writing rules change.

## Minimum standard for module notes
- Purpose and business value
- Dependencies and important reverse dependencies when relevant
- Main models and relationships
- UI surface: views, actions, menus, reports, wizards
- Security footprint: groups, ACLs, record rules
- Integrations, automations, or external services
- Code references for critical behavior

## Evidence rules
- Prefer repository-relative source references such as `odoo19/addons/sale/models/sale_order.py`.
- Mention tests when behavior is non-trivial or risky.
- If a conclusion is inferred rather than directly stated in code, say so explicitly.

## Enrichment guidance
- Use `odoo-skills` to improve examples, terminology, and learning paths.
- Do not copy a skill verbatim into the docs; adapt it to the actual Odoo 19 module being documented.
- Favor short diagrams that explain real relationships over decorative diagrams.

## Navigation
- **Parent:** [[Welcome]]
