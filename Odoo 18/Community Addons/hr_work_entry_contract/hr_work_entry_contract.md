<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, community, module]
---

# Work Entries - Contract

- Version: v18
- Category: community
- Source: odoo/addons/hr_work_entry_contract
- Dependencies: [[Odoo 18/Community Addons/hr_work_entry/hr_work_entry|hr_work_entry]], [[Odoo 18/Community Addons/hr_contract/hr_contract|hr_contract]]

## Summary

Manage work entries

## XML Artifacts (detected)

- Views: 5
- Actions: 1
- Menus: 0
- Rules (ir.rule): 1
- Access CSV entries: 1

## Detected Models

- `HrContract`
- `HrEmployee`
- `HrWorkEntry`
- `HrWorkEntryType`
- `ResourceCalendar`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Work Entries - Contract - Models and Relations
class HrContract
class HrEmployee
class HrWorkEntry
class HrWorkEntryType
class ResourceCalendar
class "hr.contract" as hr_contract
HrWorkEntry --> hr_contract : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
