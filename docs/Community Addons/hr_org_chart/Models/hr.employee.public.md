<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# hr.employee.public

- Module: [[docs/Community Addons/hr_org_chart/hr_org_chart|hr_org_chart]]
- Scope: Community Addons
- Defined in module: extension only
- Source files: `models/hr_employee.py`, `models/hr_org_chart_mixin.py`
- Python classes: `HrEmployeePublic`

## Field footprint

- Detected fields: 5
- Field types: `Boolean` x 1, `Integer` x 3, `One2many` x 1
- Relation fields: 1

## Sample fields

- `child_all_count`: `Integer` (compute `_compute_child_all_count`)
- `child_count`: `Integer` (compute `_compute_child_count`)
- `department_color`: `Integer` (compute `_compute_department_color`)
- `is_subordinate`: `Boolean` (related `employee_id.is_subordinate`)
- `subordinate_ids`: `One2many` (related `employee_id.subordinate_ids`)

## Method hints

- Detected methods: 3
- Action methods: none
- Compute methods: `_compute_child_all_count`, `_compute_child_count`, `_compute_department_color`
- Onchange methods: none

## Direct relation diagram

```plantuml
@startuml
!define ODOO_COLOR_PRIMARY #714B67
!define ODOO_COLOR_ACCENT #875A7B
!define ODOO_COLOR_BG #FAF7FA

skinparam backgroundColor ODOO_COLOR_BG
skinparam defaultTextAlignment left
skinparam ArrowColor ODOO_COLOR_ACCENT
skinparam ClassBackgroundColor white
skinparam ClassBorderColor ODOO_COLOR_PRIMARY
skinparam ComponentBackgroundColor white
skinparam ComponentBorderColor ODOO_COLOR_PRIMARY
skinparam NoteBackgroundColor #FFF8FF
skinparam NoteBorderColor ODOO_COLOR_ACCENT
skinparam SequenceLifeLineBorderColor ODOO_COLOR_ACCENT
skinparam SequenceLifeLineBackgroundColor #FFFFFF
skinparam SequenceParticipantBorderColor ODOO_COLOR_PRIMARY
skinparam SequenceParticipantBackgroundColor #FFFFFF
skinparam sequence {
  ArrowColor ODOO_COLOR_ACCENT
  ActorBorderColor ODOO_COLOR_PRIMARY
}
title hr.employee.public - Direct Relations
class "hr.employee.public" as hr_employee_public
@enduml
```

## Navigation

- **Parent:** [[docs/Community Addons/hr_org_chart/Models]]

<!-- GENERATED:MODEL -->
