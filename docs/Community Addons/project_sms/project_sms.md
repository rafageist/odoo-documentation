<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Project - SMS

- Scope: Community Addons
- Source: odoo/addons/project_sms
- Dependencies: [[docs/Community Addons/project/project|project]], [[docs/Community Addons/sms/sms|sms]]

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
!include ../../../templates/DiagramStyles.puml
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
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->





