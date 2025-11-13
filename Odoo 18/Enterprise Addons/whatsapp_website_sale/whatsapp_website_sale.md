<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, enterprise, module]
---

# WhatsApp-eCommerce

- Version: v18
- Category: enterprise
- Source: enterprise18/whatsapp_website_sale
- Dependencies: [[Odoo 18/Community Addons/website_sale/website_sale|website_sale]], [[Odoo 18/Enterprise Addons/whatsapp/whatsapp|whatsapp]]

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

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
