---
tags: [odoo, core, index]
status: active
---

# Core

## Role in the vault
- This branch explains how Odoo behaves before any business addon specialization.
- Use it to understand framework services, shared master data, infrastructure concerns, and cross-module processes.
- When a module note references a shared mechanism, the target explanation should usually live here.

## Architecture corridors
- `[[docs/Core/Framework/Framework]]` for request lifecycle, web client hooks, auth, mail, and controller entry points.
- `[[docs/Core/Master Data/Master Data]]` for entities reused by multiple domains such as partners, companies, products, and units of measure.
- `[[docs/Core/Processes/Processes]]` for end-to-end flows that span several addons.
- `[[docs/Core/Infrastructure/Infrastructure]]` for ORM, reports, files, security, and eventing primitives.
- `[[docs/Core/Integrations/Integrations]]` for provider-facing contracts, callbacks, and transport layers.

## Source anchor
- Primary source tree: `odoo19/odoo` and `odoo19/addons`
- Typical files: `odoo/http.py`, `odoo/orm/*`, `odoo/addons/base/models/*`, and shared services in core addons

## Active follow-up tickets
- Issue `#39`: framework runtime lifecycle
- Issue `#40`: master data deep dives
- Issue `#41`: core integration contracts

## Context links
- Documentation map: `[[docs/docs]]`
- Community catalog: `[[docs/Community Addons/Community Addons]]`
- Enterprise catalog: `[[docs/Enterprise Addons/Enterprise Addons]]`

## Navigation
- **Parent:** [[docs/docs]]
## Children
- [[docs/Core/Framework/Framework]]
- [[docs/Core/Infrastructure/Infrastructure]]
- [[docs/Core/Integrations/Integrations]]
- [[docs/Core/Master Data/Master Data]]
- [[docs/Core/Processes/Processes]]
