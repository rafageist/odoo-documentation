---
tags: [meta, playbook]
status: active
---

# Documentation Playbook

## Objective
Build reliable Odoo documentation that stays close to the codebase and avoids duplicated notes.

## Source hierarchy
1. Community source in `<workspace>/odoo19`
2. Enterprise source in `<workspace>/docker/odoo19-enterprise-sync/enterprise-cache/<snapshot>`
3. Tests, demo data, and manifests inside those same modules
4. `<workspace>/odoo-skills` for example patterns and explanation angles

## Structure rules
- Canonical module notes live at `docs/<Community Addons|Enterprise Addons>/<technical_name>/<technical_name>.md`.
- Category folders such as `Finance`, `HR`, `Sales`, or `Operations` contain only index notes.
- Core notes live under `docs/Core/` and should document framework behavior, shared models, and transversal processes.
- Glossary notes live under `docs/Glossary/` and should explain business terms without duplicating module or model notes.
- Avoid creating a second note for the same module inside a category folder.
- Generated module content stays inside the `<!-- GENERATED:MODULE -->` block; manual analysis should be added before or after it.

## Writing workflow
1. Start from the relevant index page and confirm the target note does not already exist elsewhere.
2. Read the manifest, models, views, security files, data files, and tests before drafting.
3. Capture concrete evidence: source paths, model names, XML ids, menu/actions, and side effects.
4. Use the closest template from `[[templates]]`.
5. Add the interpretation layer: business purpose, extension points, risks, and module interactions.
6. When a business term is central to the explanation, link the relevant glossary note or create one if the concept is reused across modules.
7. Link related modules, core topics, category indexes, and glossary terms with `[[wikilinks]]`.
8. Update `[[Changelog]]` when the repository structure or writing rules change.

## Template set
- `[[templates/Module Documentation Template]]` for canonical addon notes.
- `[[templates/Model Documentation Template]]` for models that deserve their own explanation.
- `[[templates/Service Documentation Template]]` for controllers, import/export services, and jobs.
- `[[templates/Business Process Template]]` for end-to-end operational flows.
- `[[templates/Glossary Term Template]]` for reusable business terminology notes.
- `[[templates/Diagram Examples]]` for reusable PlantUML, Mermaid, and cross-link snippets.

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

## Cross-link conventions
- Link the parent scope note and the `[[docs/docs]]` root note in every canonical page.
- Link module notes by technical name and show the functional label in the alias when useful.
- Link glossary notes when the business meaning of a term is essential to understanding the code.
- Use relative wikilinks only when they stay readable; otherwise prefer full vault paths.
- When legacy material is mentioned for context, mark it as retired instead of reopening a parallel note tree.

## Diagram conventions
- Use PlantUML for model relations and sequence flows that need stable styling.
- Use Mermaid for quick flowcharts in process notes or ADR-style explanations.
- Keep diagrams under 12 nodes when possible and split complex flows into multiple diagrams.
- Store reusable snippets in `[[templates/Diagram Examples]]` instead of duplicating boilerplate.

## Enrichment guidance
- Use `odoo-skills` to improve examples, terminology, and learning paths.
- Do not copy a skill verbatim into the docs; adapt it to the actual module being documented.
- Favor short diagrams that explain real relationships over decorative diagrams.

## Navigation
- **Parent:** [[Welcome]]
