---
tags: [odoo, v19, index]
status: active
---

# Odoo 19

## Architecture overview
- Client layer: OWL web client, assets, and interactive views rendered from `web` and addon bundles.
- Request layer: `odoo.http` controllers, route dispatch, session handling, and RPC entry points.
- Business layer: ORM, model methods, server actions, mail/thread side effects, and scheduled jobs.
- Data layer: PostgreSQL tables, attachments, reporting artifacts, and bus notifications that feed the UI back.

```plantuml
@startuml
!include ../Templates/DiagramStyles.puml
title Odoo 19 runtime map
component "OWL Web Client" as web_client
component "HTTP / RPC Layer" as http_layer
component "Core Services" as core_services
database "PostgreSQL + Filestore" as data_store
component "Community Addons" as community
component "Enterprise Addons" as enterprise
component "External Providers" as providers
web_client --> http_layer : routes, RPC, assets
http_layer --> core_services : env, auth, controllers
core_services --> data_store : ORM, attachments, reports
community --> core_services : extend models and flows
enterprise --> core_services : extend models and flows
core_services --> providers : callbacks, APIs, mail, payments
@enduml
```

## Main branches
- `[[Odoo 19/Core/Core]]` for framework behavior, shared models, integrations, and transversal processes.
- `[[Odoo 19/Community Addons/Community Addons]]` for standard addons shipped with Odoo 19.
- `[[Odoo 19/Enterprise Addons/Enterprise Addons]]` for enterprise-only addons and extensions.

## Documentation strategy
- Start in `Core` when the question is about runtime behavior, shared models, or infrastructure reused across many modules.
- Start in `Community Addons` when the behavior is delivered by a standard addon under `odoo19/addons`.
- Start in `Enterprise Addons` when the feature depends on the enterprise snapshot in this workspace.
- Keep manual analysis outside generated module blocks so the generator can refresh evidence without destroying curated notes.

## Source alignment
- Community source root: `<workspace>/odoo19`
- Enterprise source root: `<workspace>/docker/odoo19-enterprise-sync/enterprise-cache/<snapshot>`
- Supporting examples and explanation angles: `<workspace>/odoo-skills`

## Current follow-up queue
- Framework runtime lifecycle: issue `#39`
- Master data deep dives: issue `#40`
- Core integration contracts: issue `#41`

## Scope note
- The repository retired Odoo 18 comparisons and migration-only notes on 2026-03-02 so the vault can stay focused on Odoo 19 execution details.

## Navigation
- **Parent:** [[Welcome]]
## Children
- [[Odoo 19/Core/Core]]
- [[Odoo 19/Community Addons/Community Addons]]
- [[Odoo 19/Enterprise Addons/Enterprise Addons]]
