---
tags: [odoo, enterprise, generated, views]
---

# views/l10n_ec_taxpayer_type_view.xml

- Module: [[docs/Enterprise Addons/l10n_ec_edi/l10n_ec_edi|l10n_ec_edi]]
- Scope: Enterprise Addons
- Source file: `views/l10n_ec_taxpayer_type_view.xml`
- Views: 2
- Actions: 1
- Menus: 1
- Rules: 0

## View records

### `view_taxpayer_type_tree`
- Name: view.taxpayer.type.list
- Model: `l10n_ec.taxpayer.type`
- Type: `list`
- Root tag: `list`
- Field references: 6
- Sample fields: `active`, `name`, `profit_withhold_tax_id`, `sequence`, `vat_goods_withhold_tax_id`, `vat_services_withhold_tax_id`
- XPath or positional patches: 0

### `view_taxpayer_type_form`
- Name: view.taxpayer.type.form
- Model: `l10n_ec.taxpayer.type`
- Type: `form`
- Root tag: `form`
- Field references: 4
- Sample fields: `name`, `profit_withhold_tax_id`, `vat_goods_withhold_tax_id`, `vat_services_withhold_tax_id`
- XPath or positional patches: 0

## Actions

- `action_taxpayer_type`: `act_window` Taxpayer Type

## Menus

- `menu_taxpayer_type`: Taxpayer Type SRI

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_ec_edi/Views]]

