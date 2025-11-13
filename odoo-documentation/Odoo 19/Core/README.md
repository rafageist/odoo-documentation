---
tags: [odoo, v19, core]
---

# Odoo 19 - Core

Punto de entrada para notas sobre el core de Odoo 19.

## Mapa de Componentes (placeholder)

```plantuml
@startuml
!include ../../_templates/DiagramStyles.puml
title Odoo 19 - Core (Vista de Componentes)

component "Odoo Server" as Server
database PostgreSQL as PG
folder "Addons (Core)" as Addons
rectangle "Web Client" as Web

Server --> PG : ORM
Server ..> Addons : Carga/registración
Web --> Server : HTTP/JSON-RPC
@enduml
```

Enlaza cada subámbito (ORM, RPC, vistas, seguridad) con notas específicas.

