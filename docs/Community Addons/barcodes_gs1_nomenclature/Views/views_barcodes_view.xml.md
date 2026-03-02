<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/barcodes_view.xml

- Module: [[docs/Community Addons/barcodes_gs1_nomenclature/barcodes_gs1_nomenclature|barcodes_gs1_nomenclature]]
- Scope: Community Addons
- Source file: `views/barcodes_view.xml`
- Views: 3
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `view_barcode_gs1_rule_form`
- Name: Barcode Rule
- Model: `barcode.rule`
- Type: inferred from arch
- Inherits: `barcodes.view_barcode_rule_form`
- Root tag: `xpath`
- Field references: 4
- Sample fields: `associated_uom_id`, `gs1_content_type`, `gs1_decimal_usage`, `is_gs1_nomenclature`
- XPath or positional patches: 2

### `view_barcode_gs1_nomenclature_tree`
- Name: Barcode Nomenclatures
- Model: `barcode.nomenclature`
- Type: inferred from arch
- Inherits: `barcodes.view_barcode_nomenclature_tree`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `is_gs1_nomenclature`
- XPath or positional patches: 1

### `view_barcode_gs1_nomenclature_form`
- Name: Barcode Nomenclatures
- Model: `barcode.nomenclature`
- Type: inferred from arch
- Inherits: `barcodes.view_barcode_nomenclature_form`
- Root tag: `xpath`
- Field references: 5
- Sample fields: `associated_uom_id`, `gs1_content_type`, `gs1_decimal_usage`, `gs1_separator_fnc1`, `is_gs1_nomenclature`
- XPath or positional patches: 5

## Navigation

- **Parent:** [[docs/Community Addons/barcodes_gs1_nomenclature/Views]]

<!-- GENERATED:VIEWFILE -->
