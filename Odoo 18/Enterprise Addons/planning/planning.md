<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, enterprise, module]
---

# Planning

- Version: v18
- Category: enterprise
- Source: enterprise18/planning
- Dependencies: [[Odoo 18/Community Addons/hr/hr|hr]], [[Odoo 18/Community Addons/hr_hourly_cost/hr_hourly_cost|hr_hourly_cost]], [[Odoo 18/Enterprise Addons/web_gantt/web_gantt|web_gantt]], [[Odoo 18/Community Addons/digest/digest|digest]]

## Summary

Manage your employees' schedule

## XML Artifacts (detected)

- Views: 43
- Actions: 32
- Menus: 13
- Rules (ir.rule): 8
- Access CSV entries: 15

## Detected Models

- `Employee`
- `planning.slot`
- `planning.role`
- `planning.planning`
- `planning.recurrency`
- `planning.slot.template`
- `ResourceResource`
- `Company`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Planning - Models and Relations
class Employee
class "planning.slot" as planning_slot
class "planning.role" as planning_role
class "planning.planning" as planning_planning
class "planning.recurrency" as planning_recurrency
class "planning.slot.template" as planning_slot_template
class ResourceResource
class Company
class "resource.resource" as resource_resource
planning_slot --> resource_resource : many2one
class "hr.employee" as hr_employee
planning_slot --> hr_employee : many2one
class "res.users" as res_users
planning_slot --> res_users : many2one
class "res.company" as res_company
planning_slot --> res_company : many2one
planning_slot --> planning_role : many2one
planning_slot .. planning_slot : many2many
planning_slot .. planning_slot_template : many2many
planning_slot --> planning_slot_template : many2one
planning_slot --> planning_slot_template : many2one
planning_slot --> planning_recurrency : many2one
planning_role .. resource_resource : many2many
planning_planning --> res_company : many2one
planning_recurrency --|> planning_slot : one2many
planning_recurrency --> res_company : many2one
planning_slot_template --> planning_role : many2one
ResourceResource .. planning_role : many2many
ResourceResource --> planning_role : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
