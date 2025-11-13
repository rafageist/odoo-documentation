<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, community, module]
---

# Web Editor

- Version: v18
- Category: community
- Source: odoo/addons/web_editor
- Dependencies: [[Odoo 18/Community Addons/bus/bus|bus]], [[Odoo 18/Community Addons/web/web|web]], [[Odoo 18/Community Addons/html_editor/html_editor|html_editor]]
## XML Artifacts (detected)

- Views: 0
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 2

## Detected Models

- `IrUiView`
- `web_editor.converter.test`
- `web_editor.converter.test.sub`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Web Editor - Models and Relations
class IrUiView
class "web_editor.converter.test" as web_editor_converter_test
class "web_editor.converter.test.sub" as web_editor_converter_test_sub
web_editor_converter_test --> web_editor_converter_test_sub : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
