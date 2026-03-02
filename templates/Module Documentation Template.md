---
tags: [template, module, documentation]
scope: community|enterprise|core
status: draft
---

# {{Display Name}} (`{{technical_name}}`)

## Template usage
- Use this for canonical module notes under `docs/<scope>/<technical_name>/<technical_name>.md`.
- If the note is generated, keep manual analysis outside the `<!-- GENERATED:MODULE -->` block.
- Remove optional sections that do not add signal.

- Scope: `{{scope}}`
- Source: `{{source_path}}`
- Dependencies: `{{dependencies}}`

## Summary
- Functional purpose:
- Business value:
- Main entry points:

## Why it exists
- Actors:
- Operational pain point solved:
- KPIs or workflows affected:

## Main models
- `{{model_1}}`
- `{{model_2}}`

```plantuml
@startuml
!include DiagramStyles.puml
title {{technical_name}} - Main Models
class {{model_1}}
class {{model_2}}
{{model_1}} --> {{model_2}} : relation
@enduml
```

## UI surface
- Views:
- Actions:
- Menus:
- Reports or wizards:

## Security and automation
- Groups:
- ACLs / record rules:
- Cron jobs / mail templates / server actions:

## Data and configuration
- Demo or seed data:
- Company or journal settings:
- Localization hooks or fiscal mappings:

## Integrations
- External systems:
- RPC / HTTP / webhooks:

## Upgrade and rollout notes
- Pre-configuration required:
- Data migration concerns:
- Backward-compatibility risks:

## Code references
- `{{source_file}}:{{line}}`
- `{{test_file}}:{{line}}`

## Notes and risks
- Extension points:
- Known constraints:
- Open questions:

## Related material
- `[[Related Note]]`
- `[[templates/Model Documentation Template]]`
- `[[templates/Service Documentation Template]]`
- `[[templates/Diagram Examples]]`
