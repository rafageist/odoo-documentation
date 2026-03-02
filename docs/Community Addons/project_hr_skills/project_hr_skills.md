<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Project - Skills

- Scope: Community Addons
- Source: odoo/addons/project_hr_skills
- Dependencies: [[docs/Community Addons/project/project|project]], [[docs/Community Addons/hr_skills/hr_skills|hr_skills]]

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
- `ResUsers`

```plantuml
@startuml
!include ../../../templates/DiagramStyles.puml
title Project - Skills - Models and Relations
class ProjectTask
class ResUsers
class "hr.employee.skill" as hr_employee_skill
ProjectTask --|> hr_employee_skill : one2many
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->





