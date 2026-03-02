<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# WhatsApp-eCommerce

- Scope: Enterprise Addons
- Source: enterprise/whatsapp_website_sale
- Dependencies: [[docs/Community Addons/website_sale/website_sale|website_sale]], [[docs/Enterprise Addons/whatsapp/whatsapp|whatsapp]]

## Summary

This module integrates website sale with WhatsApp

## XML Artifacts (detected)

- Views: 1
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `SaleOrder`
- `Website`

```plantuml
@startuml
!include ../../../templates/DiagramStyles.puml
title WhatsApp-eCommerce - Models and Relations
class SaleOrder
class Website
class "whatsapp.template" as whatsapp_template
Website --> whatsapp_template : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->



