<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Web Studio Tests

- Scope: Enterprise Addons
- Source: enterprise/test_web_studio
- Dependencies: [[docs/Enterprise Addons/web_studio/web_studio|web_studio]], [[docs/Community Addons/website/website|website]], [[docs/Community Addons/sale/sale|sale]]

## Summary

Web studio Test

## XML Artifacts (detected)

- Views: 0
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 6

## Detected Models

- `test.studio.model_action`
- `test.studio.model_action2`
- `test.studio.model_action3`
- `test.studio_export.model1`
- `test.studio_export.model2`
- `test.studio_export.model3`

```plantuml
@startuml
!include ../../../templates/DiagramStyles.puml
title Web Studio Tests - Models and Relations
class "test.studio.model_action" as test_studio_model_action
class "test.studio.model_action2" as test_studio_model_action2
class "test.studio.model_action3" as test_studio_model_action3
class "test.studio_export.model1" as test_studio_export_model1
class "test.studio_export.model2" as test_studio_export_model2
class "test.studio_export.model3" as test_studio_export_model3
class "res.currency" as res_currency
test_studio_model_action --> res_currency : many2one
class "res.partner" as res_partner
test_studio_model_action --> res_partner : many2one
test_studio_model_action3 --> test_studio_model_action : many2one
class "ir.attachment" as ir_attachment
test_studio_export_model1 --> ir_attachment : many2one
test_studio_export_model1 --|> ir_attachment : one2many
test_studio_export_model1 --> test_studio_export_model2 : many2one
test_studio_export_model2 --> test_studio_export_model2 : many2one
test_studio_export_model2 --> test_studio_export_model3 : many2one
test_studio_export_model3 --> test_studio_export_model1 : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->



