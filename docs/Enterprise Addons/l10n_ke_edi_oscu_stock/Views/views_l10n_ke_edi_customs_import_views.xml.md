---
tags: [odoo, enterprise, generated, views]
---

# views/l10n_ke_edi_customs_import_views.xml

- Module: [[docs/Enterprise Addons/l10n_ke_edi_oscu_stock/l10n_ke_edi_oscu_stock|l10n_ke_edi_oscu_stock]]
- Scope: Enterprise Addons
- Source file: `views/l10n_ke_edi_customs_import_views.xml`
- Views: 3
- Actions: 2
- Menus: 1
- Rules: 0

## View records

### `l10n_ke_customs_import_search_view`
- Name: l10n.ke.edi.oscu.stock.customs.import.search
- Model: `l10n_ke_edi.customs.import`
- Type: inferred from arch
- Root tag: `search`
- Field references: 5
- Sample fields: `declaration_number`, `hs_code`, `item_name`, `product_id`, `task_code`
- XPath or positional patches: 0

### `l10n_ke_edi_customs_import_view_branch_form`
- Name: l10n.ke.edi.oscu.stock.customs.import.form
- Model: `l10n_ke_edi.customs.import`
- Type: inferred from arch
- Root tag: `form`
- Field references: 21
- Sample fields: `company_id`, `declaration_date`, `declaration_number`, `export_country_id`, `hs_code`, `item_name`, `item_seq`, `number_packages`, `origin_country_id`, `package_unit_code_id`, and 11 more
- Buttons: `action_create_purchase_order`, `action_view_purchase_order`, `button_approve`, `button_reject`
- XPath or positional patches: 0

### `l10n_ke_edi_customs_import_view_tree`
- Name: l10n.ke.edi.oscu.stock.customs.import.list
- Model: `l10n_ke_edi.customs.import`
- Type: inferred from arch
- Root tag: `list`
- Field references: 10
- Sample fields: `company_id`, `declaration_date`, `declaration_number`, `item_name`, `number_packages`, `product_id`, `quantity`, `state`, `task_code`, `uom_code_id`
- XPath or positional patches: 0

## Actions

- `purchase_create`: `server` Create Purchase
- `action_l10n_ke_edi_oscu_customs_import`: `act_window` Customs Import

## Menus

- `menu_action_l10n_ke_edi_customs_import`: Customs Imports

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_ke_edi_oscu_stock/Views]]

