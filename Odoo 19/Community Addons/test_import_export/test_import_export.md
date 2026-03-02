<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, community, module]
---

# Test - Import & Export

- Version: v19
- Scope: Community Addons
- Source: odoo19/addons/test_import_export
- Dependencies: [[Odoo 19/Community Addons/web/web|web]], [[Odoo 19/Community Addons/base_import/base_import|base_import]], [[Odoo 19/Community Addons/website/website|website]]

## Summary

Base Import & Export Tests: Ensure Flow Robustness

## XML Artifacts (detected)

- Views: 0
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 53

## Detected Models

- `export.aggregator`
- `export.aggregator.one2many`
- `export.one2many.child`
- `export.one2many.multiple`
- `export.one2many.multiple.child`
- `export.one2many.child.1`
- `export.one2many.child.2`
- `export.many2many.other`
- `export.selection.withdefault`
- `export.one2many.recursive`
- `export.unique`
- `export.inherits.parent`
- `export.inherits.child`
- `export.m2o.str`
- `export.m2o.str.child`
- `export.with.required.field`
- `export.many2one.required.subfield`
- `export.with.non.demo.constraint`
- `import.char`
- `import.char.required`
- `import.char.readonly`
- `import.char.noreadonly`
- `import.char.stillreadonly`
- `import.m2o`
- `import.m2o.related`
- `import.m2o.required`
- `import.m2o.required.related`
- `import.o2m`
- `import.o2m.child`
- `import.preview`
- `import.float`
- `import.complex`
- `import.properties.definition`
- `import.properties`
- `PropertyInherits`
- `PathToProperty`

```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Test - Import & Export - Models and Relations
class "export.aggregator" as export_aggregator
class "export.aggregator.one2many" as export_aggregator_one2many
class "export.one2many.child" as export_one2many_child
class "export.one2many.multiple" as export_one2many_multiple
class "export.one2many.multiple.child" as export_one2many_multiple_child
class "export.one2many.child.1" as export_one2many_child_1
class "export.one2many.child.2" as export_one2many_child_2
class "export.many2many.other" as export_many2many_other
class "export.selection.withdefault" as export_selection_withdefault
class "export.one2many.recursive" as export_one2many_recursive
class "export.unique" as export_unique
class "export.inherits.parent" as export_inherits_parent
class "export.inherits.child" as export_inherits_child
class "export.m2o.str" as export_m2o_str
class "export.m2o.str.child" as export_m2o_str_child
class "export.with.required.field" as export_with_required_field
class "export.many2one.required.subfield" as export_many2one_required_subfield
class "export.with.non.demo.constraint" as export_with_non_demo_constraint
class "import.char" as import_char
class "import.char.required" as import_char_required
class "import.char.readonly" as import_char_readonly
class "import.char.noreadonly" as import_char_noreadonly
class "import.char.stillreadonly" as import_char_stillreadonly
class "import.m2o" as import_m2o
class "import.m2o.related" as import_m2o_related
class "import.m2o.required" as import_m2o_required
class "import.m2o.required.related" as import_m2o_required_related
class "import.o2m" as import_o2m
class "import.o2m.child" as import_o2m_child
class "import.preview" as import_preview
class "import.float" as import_float
class "import.complex" as import_complex
class "import.properties.definition" as import_properties_definition
class "import.properties" as import_properties
class PropertyInherits
class PathToProperty
class "res.currency" as res_currency
export_aggregator --> res_currency : many2one
class "export.integer" as export_integer
export_aggregator --> export_integer : many2one
export_aggregator --|> export_aggregator_one2many : one2many
class "res.partner" as res_partner
export_aggregator .. res_partner : many2many
export_aggregator_one2many --> export_aggregator : many2one
class "export.one2many" as export_one2many
export_one2many_child --> export_one2many : many2one
export_one2many_child --> export_integer : many2one
export_one2many_multiple --> export_one2many_recursive : many2one
export_one2many_multiple --|> export_one2many_child_1 : one2many
export_one2many_multiple --|> export_one2many_child_2 : one2many
export_one2many_multiple_child --> export_one2many_multiple : many2one
export_one2many_recursive --|> export_one2many_multiple : one2many
export_inherits_child --> export_inherits_parent : many2one
export_m2o_str --> export_m2o_str_child : many2one
export_many2one_required_subfield --> export_with_required_field : many2one
import_m2o --> import_m2o_related : many2one
import_m2o_required --> import_m2o_required_related : many2one
import_o2m --|> import_o2m_child : one2many
import_o2m_child --> import_o2m : many2one
import_float --> res_currency : many2one
import_complex --> res_currency : many2one
import_complex --> import_complex : many2one
import_properties_definition --|> import_properties : one2many
import_properties_definition --> import_properties : many2one
import_properties --> import_properties_definition : many2one
PropertyInherits --> import_properties : many2one
PathToProperty --> import_properties : many2one
PathToProperty --> import_properties : many2one
PathToProperty .. import_properties : many2many
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->


