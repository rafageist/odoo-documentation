<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# HTML Editor

- Scope: Community Addons
- Source: odoo/addons/html_editor
- Dependencies: base (not documented), [[docs/Community Addons/bus/bus|bus]], [[docs/Community Addons/web/web|web]]

## Summary


        A Html Editor component and plugin system
    

## XML Artifacts (detected)

- Views: 0
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 2

## Detected Models

- `IrAttachment`
- `IrUiView`
- `html_editor.converter.test`
- `html_editor.converter.test.sub`

```plantuml
@startuml
!include ../../../templates/DiagramStyles.puml
title HTML Editor - Models and Relations
class IrAttachment
class IrUiView
class "html_editor.converter.test" as html_editor_converter_test
class "html_editor.converter.test.sub" as html_editor_converter_test_sub
class "ir.attachment" as ir_attachment
IrAttachment --> ir_attachment : many2one
html_editor_converter_test --> html_editor_converter_test_sub : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->





