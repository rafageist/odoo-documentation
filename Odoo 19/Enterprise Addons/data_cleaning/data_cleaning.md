<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, enterprise, module]
---

# Data Cleaning

- Version: v19
- Scope: Enterprise Addons
- Source: enterprise19/data_cleaning
- Dependencies: [[Odoo 19/Community Addons/data_recycle/data_recycle|data_recycle]], [[Odoo 19/Community Addons/phone_validation/phone_validation|phone_validation]], [[Odoo 19/Community Addons/mail/mail|mail]]

## Summary

Easily format text data across multiple records. Find duplicate records and easily merge them.

## XML Artifacts (detected)

- Views: 19
- Actions: 8
- Menus: 6
- Rules (ir.rule): 2
- Access CSV entries: 8

## Detected Models

- `data_cleaning.model`
- `data_cleaning.record`
- `data_cleaning.rule`
- `data_merge.group`
- `data_merge.model`
- `data_merge.record`
- `data_merge.rule`
- `IrModel`
- `ResPartner`

```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Data Cleaning - Models and Relations
class "data_cleaning.model" as data_cleaning_model
class "data_cleaning.record" as data_cleaning_record
class "data_cleaning.rule" as data_cleaning_rule
class "data_merge.group" as data_merge_group
class "data_merge.model" as data_merge_model
class "data_merge.record" as data_merge_record
class "data_merge.rule" as data_merge_rule
class IrModel
class ResPartner
class "ir.model" as ir_model
data_cleaning_model --> ir_model : many2one
data_cleaning_model --|> data_cleaning_rule : one2many
class "res.users" as res_users
data_cleaning_model .. res_users : many2many
data_cleaning_record .. data_cleaning_rule : many2many
class "ir.model.fields" as ir_model_fields
data_cleaning_record --> ir_model_fields : many2one
data_cleaning_record --> data_cleaning_model : many2one
class "res.country" as res_country
data_cleaning_record --> res_country : many2one
class "res.company" as res_company
data_cleaning_record --> res_company : many2one
data_cleaning_rule --> data_cleaning_model : many2one
data_cleaning_rule --> ir_model_fields : many2one
data_merge_group --> data_merge_model : many2one
data_merge_group --|> data_merge_record : one2many
data_merge_model --> ir_model : many2one
data_merge_model --|> data_merge_rule : one2many
data_merge_model .. res_users : many2many
data_merge_record --> data_merge_group : many2one
data_merge_record --> res_company : many2one
data_merge_rule --> data_merge_model : many2one
data_merge_rule --> ir_model_fields : many2one
class "ir.actions.server" as ir_actions_server
IrModel --> ir_actions_server : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->

