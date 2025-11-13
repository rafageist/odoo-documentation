<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, community, module]
---

# Website Test

- Version: v18
- Category: community
- Source: odoo/addons/test_website
- Dependencies: [[Odoo 18/Community Addons/web_unsplash/web_unsplash|web_unsplash]], [[Odoo 18/Community Addons/website/website|website]], [[Odoo 18/Community Addons/theme_default/theme_default|theme_default]]

## Summary

Website Test, mainly for module install/uninstall tests

## XML Artifacts (detected)

- Views: 11
- Actions: 4
- Menus: 1
- Rules (ir.rule): 1
- Access CSV entries: 19

## Detected Models

- `Website`
- `test.model`
- `test.submodel`
- `test.tag`
- `test.model.multi.website`
- `test.model.exposed`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Website Test - Models and Relations
class Website
class "test.model" as test_model
class "test.submodel" as test_submodel
class "test.tag" as test_tag
class "test.model.multi.website" as test_model_multi_website
class "test.model.exposed" as test_model_exposed
test_model --|> test_submodel : one2many
test_model --> test_tag : many2one
test_submodel --> test_model : many2one
test_submodel --> test_tag : many2one
class website
test_model_multi_website --> website : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
