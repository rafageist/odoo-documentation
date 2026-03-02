<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, enterprise, module]
---

# Planning

- Version: v19
- Scope: Enterprise Addons
- Source: enterprise19/planning
- Dependencies: [[Odoo 19/Community Addons/hr/hr|hr]], [[Odoo 19/Community Addons/hr_hourly_cost/hr_hourly_cost|hr_hourly_cost]], [[Odoo 19/Enterprise Addons/web_gantt/web_gantt|web_gantt]], [[Odoo 19/Community Addons/digest/digest|digest]]

## Summary

Manage your employees' schedule

## XML Artifacts (detected)

- Views: 51
- Actions: 40
- Menus: 14
- Rules (ir.rule): 9
- Access CSV entries: 17

## Detected Models

- `HrEmployee`
- `HrEmployeePublic`
- `planning.calendar.resource`
- `planning.planning`
- `planning.recurrency`
- `planning.role`
- `planning.slot`
- `planning.slot.template`
- `ResourceResource`
- `ResCompany`

```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Planning - Models and Relations
class HrEmployee
class HrEmployeePublic
class "planning.calendar.resource" as planning_calendar_resource
class "planning.planning" as planning_planning
class "planning.recurrency" as planning_recurrency
class "planning.role" as planning_role
class "planning.slot" as planning_slot
class "planning.slot.template" as planning_slot_template
class ResourceResource
class ResCompany
class "res.users" as res_users
planning_calendar_resource --> res_users : many2one
class "resource.resource" as resource_resource
planning_calendar_resource --> resource_resource : many2one
class "res.company" as res_company
planning_planning --> res_company : many2one
planning_recurrency --|> planning_slot : one2many
planning_recurrency --> res_company : many2one
planning_role .. resource_resource : many2many
planning_slot --> resource_resource : many2one
class "hr.employee" as hr_employee
planning_slot --> hr_employee : many2one
planning_slot --> res_users : many2one
planning_slot --> res_company : many2one
planning_slot --> planning_role : many2one
planning_slot .. planning_slot : many2many
planning_slot .. planning_slot_template : many2many
planning_slot --> planning_slot_template : many2one
planning_slot --> planning_slot_template : many2one
planning_slot --> planning_recurrency : many2one
planning_slot_template --> planning_role : many2one
ResourceResource .. planning_role : many2many
ResourceResource --> planning_role : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->

