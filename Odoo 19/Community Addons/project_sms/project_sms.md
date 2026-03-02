<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, community, module]
---

# Project - SMS

- Version: v19
- Scope: Community Addons
- Source: odoo19/addons/project_sms
- Dependencies: [[Odoo 19/Community Addons/project/project|project]], [[Odoo 19/Community Addons/sms/sms|sms]]

## Summary

Send text messages when project/task stage move

## XML Artifacts (detected)

- Views: 6
- Actions: 2
- Menus: 0
- Rules (ir.rule): 1
- Access CSV entries: 1

## Detected Models

- `ProjectProject`
- `ProjectProjectStage`
- `ProjectTask`
- `ProjectTaskType`

```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Project - SMS - Models and Relations
class ProjectProject
class ProjectProjectStage
class ProjectTask
class ProjectTaskType
class "sms.template" as sms_template
ProjectProjectStage --> sms_template : many2one
ProjectTaskType --> sms_template : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->


