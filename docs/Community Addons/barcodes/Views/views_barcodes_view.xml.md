<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/barcodes_view.xml

- Module: [[docs/Community Addons/barcodes/barcodes|barcodes]]
- Scope: Community Addons
- Source file: `views/barcodes_view.xml`
- Views: 3
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `view_barcode_rule_form`
- Name: Barcode Rule
- Model: `barcode.rule`
- Type: inferred from arch
- Root tag: `form`
- Field references: 6
- Sample fields: `alias`, `encoding`, `name`, `pattern`, `sequence`, `type`
- XPath or positional patches: 0

### `view_barcode_nomenclature_tree`
- Name: Barcode Nomenclatures
- Model: `barcode.nomenclature`
- Type: inferred from arch
- Root tag: `list`
- Field references: 1
- Sample fields: `name`
- XPath or positional patches: 0

### `view_barcode_nomenclature_form`
- Name: Barcode Nomenclatures
- Model: `barcode.nomenclature`
- Type: inferred from arch
- Root tag: `form`
- Field references: 7
- Sample fields: `encoding`, `name`, `pattern`, `rule_ids`, `sequence`, `type`, `upc_ean_conv`
- XPath or positional patches: 0

## Actions

- `action_barcode_nomenclature_form`: `act_window` Barcode Nomenclatures

## Navigation

- **Parent:** [[docs/Community Addons/barcodes/Views]]

<!-- GENERATED:VIEWFILE -->
