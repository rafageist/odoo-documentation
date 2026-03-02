<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, enterprise, module]
---

# WhatsApp-eCommerce

- Version: v19
- Scope: Enterprise Addons
- Source: enterprise19/whatsapp_website_sale
- Dependencies: [[Odoo 19/Community Addons/website_sale/website_sale|website_sale]], [[Odoo 19/Enterprise Addons/whatsapp/whatsapp|whatsapp]]

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
!include ../../../Templates/DiagramStyles.puml
title WhatsApp-eCommerce - Models and Relations
class SaleOrder
class Website
class "whatsapp.template" as whatsapp_template
Website --> whatsapp_template : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->

