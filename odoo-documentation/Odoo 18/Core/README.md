---
tags: [odoo, v18, core]
---

# Odoo 18 - Core

Punto de entrada para notas sobre el core de Odoo 18.

## Mapa de Componentes (placeholder)

```plantuml
@startuml
!include ../../_templates/DiagramStyles.puml
title Odoo 18 - Core (Vista de Componentes)

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

