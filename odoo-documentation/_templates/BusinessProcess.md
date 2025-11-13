---
tags: [odoo, process]
aliases: [Business Process Template]
---

# {{process_name}}

## Descripción

{{business_summary}}

## Flujo (Secuencia)

```plantuml
@startuml
!include DiagramStyles.puml
title {{process_name}} - Flujo

actor Usuario
participant "{{Module}}" as M

Usuario -> M: {{Trigger}}
activate M
M -> M: {{Validaciones}}
M --> Usuario: {{Resultado}}
deactivate M
@enduml
```

## Entidades y Reglas

- {{entity_1}}: {{rule}}

