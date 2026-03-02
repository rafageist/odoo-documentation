<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Automation Rules

- Scope: Community Addons
- Source: odoo/addons/base_automation
- Dependencies: base (not documented), [[docs/Community Addons/digest/digest|digest]], [[docs/Community Addons/resource/resource|resource]], [[docs/Community Addons/mail/mail|mail]], [[docs/Community Addons/sms/sms|sms]]

## XML Artifacts (detected)

- Views: 5
- Actions: 1
- Menus: 1
- Rules (ir.rule): 0
- Access CSV entries: 1

## Detected Models

- `base.automation`
- `IrActionsServer`
- `IrCron`

```plantuml
@startuml
!include ../../../templates/DiagramStyles.puml
title Automation Rules - Models and Relations
class "base.automation" as base_automation
class IrActionsServer
class IrCron
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
IrActionsServer --> base_automation : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->





