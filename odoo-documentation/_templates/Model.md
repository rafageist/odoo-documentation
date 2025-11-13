---
tags: [odoo, model]
aliases: [Model Template]
---

# {{model_name}}

- Módulo: [[{{module_note_ref}}]]
- Técnica: `models.Model`

## Campos

| Nombre | Tipo | Requerido | Help |
|-------|------|-----------|------|
| {{field_1}} | {{type}} | {{req}} | {{help}} |

## Reglas de Seguridad

- {{rule_1}}

## Relaciones

```plantuml
@startuml
!include DiagramStyles.puml
title {{model_name}} - Relaciones

class {{model_name}}
{{model_name}} --> {{related_model}} : many2one
@enduml
```

## Lógica Destacada

```python
class {{py_class}}(models.Model):
    _name = '{{model_name}}'
    # ...
```

