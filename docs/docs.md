---
tags: [odoo, index]
status: active
---

# Documentation

## Architecture overview
- Client layer: OWL web client, assets, and interactive views rendered from `web` and addon bundles.
- Request layer: `odoo.http` controllers, route dispatch, session handling, and RPC entry points.
- Business layer: ORM, model methods, server actions, mail/thread side effects, and scheduled jobs.
- Data layer: PostgreSQL tables, attachments, reporting artifacts, and bus notifications that feed the UI back.

```plantuml
@startuml
!include ../templates/DiagramStyles.puml
title Odoo runtime map
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
- `[[docs/Core/Core]]` for framework behavior, shared models, integrations, and transversal processes.
- `[[docs/Community Addons/Community Addons]]` for standard addons shipped in the active source tree.
- `[[docs/Enterprise Addons/Enterprise Addons]]` for enterprise-only addons and extensions.
- `[[docs/Glossary/Glossary]]` for business vocabulary that developers need to map back to Odoo models and workflows.

## Documentation strategy
- Start in `Core` when the question is about runtime behavior, shared models, or infrastructure reused across many modules.
- Start in `Community Addons` when the behavior is delivered by a standard addon under `odoo19/addons`.
- Start in `Enterprise Addons` when the feature depends on the enterprise snapshot in this workspace.
- Start in `Glossary` when the requirement is written in business language and you first need to resolve what Odoo concept or model it refers to.
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
- The repository retired parallel version trees and migration-only notes on 2026-03-02 so the vault can stay focused on the active codebase.

## Navigation
- **Parent:** [[Welcome]]

## Children
- [[docs/Core/Core]]
- [[docs/Community Addons/Community Addons]]
- [[docs/Enterprise Addons/Enterprise Addons]]
- [[docs/Glossary/Glossary]]
