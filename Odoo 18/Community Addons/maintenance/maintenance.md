<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, community, module]
---

# Maintenance

- Version: v18
- Category: community
- Source: odoo/addons/maintenance
- Dependencies: [[Odoo 18/Community Addons/mail/mail|mail]]

## Summary

Track equipment and manage maintenance requests

## XML Artifacts (detected)

- Views: 25
- Actions: 14
- Menus: 17
- Rules (ir.rule): 8
- Access CSV entries: 10

## Detected Models

- `maintenance.stage`
- `maintenance.equipment.category`
- `maintenance.equipment`
- `maintenance.request`
- `maintenance.team`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Maintenance - Models and Relations
class "maintenance.stage" as maintenance_stage
class "maintenance.equipment.category" as maintenance_equipment_category
class "maintenance.equipment" as maintenance_equipment
class "maintenance.request" as maintenance_request
class "maintenance.team" as maintenance_team
class "res.company" as res_company
maintenance_equipment_category --> res_company : many2one
class "res.users" as res_users
maintenance_equipment_category --> res_users : many2one
maintenance_equipment_category --|> maintenance_equipment : one2many
maintenance_equipment_category --|> maintenance_request : one2many
maintenance_equipment --> res_users : many2one
maintenance_equipment --> maintenance_equipment_category : many2one
class "res.partner" as res_partner
maintenance_equipment --> res_partner : many2one
maintenance_equipment --|> maintenance_request : one2many
maintenance_request --> res_company : many2one
maintenance_request --> res_users : many2one
maintenance_request --> maintenance_equipment_category : many2one
maintenance_request --> maintenance_equipment : many2one
maintenance_request --> res_users : many2one
maintenance_request --> maintenance_stage : many2one
maintenance_request --> maintenance_team : many2one
maintenance_team --> res_company : many2one
maintenance_team .. res_users : many2many
maintenance_team --|> maintenance_request : one2many
maintenance_team --|> maintenance_equipment : one2many
maintenance_team --|> maintenance_request : one2many
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
