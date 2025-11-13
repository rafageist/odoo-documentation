<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, enterprise, module]
---

# Website Helpdesk

- Version: v18
- Category: enterprise
- Source: enterprise18/website_helpdesk
- Dependencies: [[Odoo 18/Enterprise Addons/helpdesk/helpdesk|helpdesk]], [[Odoo 18/Community Addons/website/website|website]]

## Summary

Bridge module for helpdesk modules using the website.

## XML Artifacts (detected)

- Views: 1
- Actions: 0
- Menus: 0
- Rules (ir.rule): 1
- Access CSV entries: 0

## Detected Models

- `helpdesk.team`
- `HelpdeskTicket`
- `Website`
- `WebsiteMenu`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Website Helpdesk - Models and Relations
class "helpdesk.team" as helpdesk_team
class HelpdeskTicket
class Website
class WebsiteMenu
class website
helpdesk_team --> website : many2one
class "website.menu" as website_menu
helpdesk_team --> website_menu : many2one
class "ir.ui.view" as ir_ui_view
helpdesk_team --> ir_ui_view : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
