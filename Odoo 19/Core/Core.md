---
tags: [odoo, v19, core, index]
status: active
---

# Odoo 19 Core

## Role in the vault
- This branch explains how Odoo 19 behaves before any business addon specialization.
- Use it to understand framework services, shared master data, infrastructure concerns, and cross-module processes.
- When a module note references a shared mechanism, the target explanation should usually live here.

## Architecture corridors
- `[[Odoo 19/Core/Framework/Framework]]` for request lifecycle, web client hooks, auth, mail, and controller entry points.
- `[[Odoo 19/Core/Master Data/Master Data]]` for entities reused by multiple domains such as partners, companies, products, and units of measure.
- `[[Odoo 19/Core/Processes/Processes]]` for end-to-end flows that span several addons.
- `[[Odoo 19/Core/Infrastructure/Infrastructure]]` for ORM, reports, files, security, and eventing primitives.
- `[[Odoo 19/Core/Integrations/Integrations]]` for provider-facing contracts, callbacks, and transport layers.

## Source anchor
- Primary source tree: `odoo19/odoo` and `odoo19/addons`
- Typical files: `odoo/http.py`, `odoo/orm/*`, `odoo/addons/base/models/*`, and shared services in core addons

## Active follow-up tickets
- Issue `#39`: framework runtime lifecycle
- Issue `#40`: master data deep dives
- Issue `#41`: core integration contracts

## Context links
- Version map: `[[Odoo 19/Odoo 19]]`
- Community catalog: `[[Odoo 19/Community Addons/Community Addons]]`
- Enterprise catalog: `[[Odoo 19/Enterprise Addons/Enterprise Addons]]`

## Navigation
- **Parent:** [[Odoo 19/Odoo 19]]
## Children
- [[Odoo 19/Core/Framework/Framework]]
- [[Odoo 19/Core/Infrastructure/Infrastructure]]
- [[Odoo 19/Core/Integrations/Integrations]]
- [[Odoo 19/Core/Master Data/Master Data]]
- [[Odoo 19/Core/Processes/Processes]]
