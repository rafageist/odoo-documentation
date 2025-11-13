---
tags: [odoo, service]
aliases: [Service Template]
---

# {{service_name}}

## Responsabilidades

- {{responsibility_1}}

## Dependencias

- {{dependency_1}}

## Interfaces

```plantuml
@startuml
!include DiagramStyles.puml
title {{service_name}} - Interfaces

component {{service_name}}
interface IAPI

{{service_name}} ..> IAPI
@enduml
```

