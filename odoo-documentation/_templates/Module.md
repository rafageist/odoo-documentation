---
tags: [odoo, module]
aliases: [Module Template]
---

# {{module_name}}

- Versión: {{version_tag}}
- Categoría: {{category_tag}}
- Ruta fuente: {{source_path}}
- Dependencias: {{depends}}

## Resumen

{{summary}}

## Negocio / Casos de Uso

- {{use_case_1}}
- {{use_case_2}}

## Modelos Principales

```plantuml
@startuml
!include DiagramStyles.puml
title {{module_name}} - Modelos
skinparam linetype ortho

' Clases ejemplo. Sustituir por clases reales detectadas.
class {{module_name}}Model1 {
  +_name: string
  +_inherit: list
}
class {{module_name}}Model2

{{module_name}}Model1 --> {{module_name}}Model2 : many2one
@enduml
```

## Vistas, Acciones y Seguridad

- Vistas: {{views_count}}
- Acciones: {{actions_count}}
- Menús: {{menus_count}}
- Reglas de Seguridad: {{security_rules_count}}

## Integraciones

- {{integration_1}}

## Código Destacado

```python
# pegue aquí snippets relevantes
```

## Enlaces

- [[../README|Volver a categoría]]
- [[../../README|Volver a versión]]

