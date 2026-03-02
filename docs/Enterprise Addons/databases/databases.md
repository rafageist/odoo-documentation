<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Databases

- Scope: Enterprise Addons
- Source: enterprise/databases
- Dependencies: [[docs/Community Addons/project/project|project]]

## Summary

Manage a fleet of Odoo databases

## XML Artifacts (detected)

- Views: 6
- Actions: 7
- Menus: 5
- Rules (ir.rule): 3
- Access CSV entries: 4

## Detected Models

- `databases.user`
- `ProjectProject`

```plantuml
@startuml
!include ../../../templates/DiagramStyles.puml
title Databases - Models and Relations
class "databases.user" as databases_user
class ProjectProject
class "project.project" as project_project
databases_user --> project_project : many2one
class "res.users" as res_users
databases_user --> res_users : many2one
class "properties.base.definition" as properties_base_definition
ProjectProject --> properties_base_definition : many2one
ProjectProject --|> databases_user : one2many
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->


