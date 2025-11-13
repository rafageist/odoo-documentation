<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, community, module]
---

# Data Recycle

- Version: v19
- Category: community
- Source: odoo19/addons/data_recycle
- Dependencies: [[Odoo 19/Community Addons/mail/mail|mail]]

## Summary

Find old records and archive/delete them

## XML Artifacts (detected)

- Views: 4
- Actions: 3
- Menus: 5
- Rules (ir.rule): 0
- Access CSV entries: 2

## Detected Models

- `data_recycle.model`
- `data_recycle.record`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Data Recycle - Models and Relations
class "data_recycle.model" as data_recycle_model
class "data_recycle.record" as data_recycle_record
class "ir.model" as ir_model
data_recycle_model --> ir_model : many2one
data_recycle_model --|> data_recycle_record : one2many
class "ir.model.fields" as ir_model_fields
data_recycle_model --> ir_model_fields : many2one
class "res.users" as res_users
data_recycle_model .. res_users : many2many
data_recycle_record --> data_recycle_model : many2one
class "res.company" as res_company
data_recycle_record --> res_company : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->
