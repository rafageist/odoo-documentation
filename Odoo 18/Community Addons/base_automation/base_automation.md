<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, community, module]
---

# Automation Rules

- Version: v18
- Category: community
- Source: odoo/addons/base_automation
- Dependencies: base (not documented), [[Odoo 18/Community Addons/digest/digest|digest]], [[Odoo 18/Community Addons/resource/resource|resource]], [[Odoo 18/Community Addons/mail/mail|mail]], [[Odoo 18/Community Addons/sms/sms|sms]]
## XML Artifacts (detected)

- Views: 5
- Actions: 1
- Menus: 1
- Rules (ir.rule): 0
- Access CSV entries: 1

## Detected Models

- `base.automation`
- `ServerAction`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Automation Rules - Models and Relations
class "base.automation" as base_automation
class ServerAction
class "ir.model" as ir_model
base_automation --> ir_model : many2one
class "ir.actions.server" as ir_actions_server
base_automation --|> ir_actions_server : one2many
class "ir.model.fields.selection" as ir_model_fields_selection
base_automation --> ir_model_fields_selection : many2one
class "ir.model.fields" as ir_model_fields
base_automation --> ir_model_fields : many2one
class "resource.calendar" as resource_calendar
base_automation --> resource_calendar : many2one
base_automation .. ir_model_fields : many2many
base_automation .. ir_model_fields : many2many
ServerAction --> base_automation : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
