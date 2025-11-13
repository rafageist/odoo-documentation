<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, community, module]
---

# Project - Skills

- Version: v18
- Category: community
- Source: odoo/addons/project_hr_skills
- Dependencies: [[Odoo 18/Community Addons/project/project|project]], [[Odoo 18/Community Addons/hr_skills/hr_skills|hr_skills]]

## Summary

Project skills

## XML Artifacts (detected)

- Views: 1
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `ProjectTask`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Project - Skills - Models and Relations
class ProjectTask
class "hr.employee.skill" as hr_employee_skill
ProjectTask --|> hr_employee_skill : one2many
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
