<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, enterprise, module]
---

# Web Studio Tests

- Version: v19
- Category: enterprise
- Source: enterprise19/test_web_studio
- Dependencies: [[Odoo 19/Enterprise Addons/web_studio/web_studio|web_studio]], [[Odoo 19/Community Addons/website/website|website]], [[Odoo 19/Community Addons/sale/sale|sale]]

## Summary

Web studio Test

## XML Artifacts (detected)

- Views: 0
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 5

## Detected Models

- `test.studio.model_action`
- `test.studio.model_action2`
- `test.studio_export.model1`
- `test.studio_export.model2`
- `test.studio_export.model3`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Web Studio Tests - Models and Relations
class "test.studio.model_action" as test_studio_model_action
class "test.studio.model_action2" as test_studio_model_action2
class "test.studio_export.model1" as test_studio_export_model1
class "test.studio_export.model2" as test_studio_export_model2
class "test.studio_export.model3" as test_studio_export_model3
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

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->
