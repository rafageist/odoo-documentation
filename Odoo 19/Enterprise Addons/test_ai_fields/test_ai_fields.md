<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, enterprise, module]
---

# Test AI Field

- Version: v19
- Scope: Enterprise Addons
- Source: enterprise19/test_ai_fields
- Dependencies: [[Odoo 19/Enterprise Addons/ai_fields/ai_fields|ai_fields]]

## XML Artifacts (detected)

- Views: 0
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 5

## Detected Models

- `test.ai.fields.parent`
- `test.ai.fields.model`
- `test.ai.fields.definition`
- `test.ai.fields.no.ai`
- `test.ai.read.model`

```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Test AI Field - Models and Relations
class "test.ai.fields.parent" as test_ai_fields_parent
class "test.ai.fields.model" as test_ai_fields_model
class "test.ai.fields.definition" as test_ai_fields_definition
class "test.ai.fields.no.ai" as test_ai_fields_no_ai
class "test.ai.read.model" as test_ai_read_model
test_ai_fields_model --> test_ai_fields_parent : many2one
class "res.partner" as res_partner
test_ai_fields_model --> res_partner : many2one
test_ai_fields_model .. res_partner : many2many
class "res.currency" as res_currency
test_ai_read_model --> res_currency : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->

