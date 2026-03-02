<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/l10n_ar_earnings_scale_view.xml

- Module: [[docs/Community Addons/l10n_ar_withholding/l10n_ar_withholding|l10n_ar_withholding]]
- Scope: Community Addons
- Source file: `views/l10n_ar_earnings_scale_view.xml`
- Views: 2
- Actions: 1
- Menus: 1
- Rules: 0

## View records

### `view_afip_earnings_table_scale_form`
- Name: l10n_ar.earnings.scale.form
- Model: `l10n_ar.earnings.scale`
- Type: inferred from arch
- Root tag: `form`
- Field references: 7
- Sample fields: `excess_amount`, `fixed_amount`, `from_amount`, `line_ids`, `name`, `percentage`, `to_amount`
- XPath or positional patches: 0

### `view_afip_earnings_table_scale_tree`
- Name: l10n_ar.earnings.scale.tree
- Model: `l10n_ar.earnings.scale`
- Type: inferred from arch
- Root tag: `list`
- Field references: 1
- Sample fields: `name`
- XPath or positional patches: 0

## Actions

- `act_afip_earnings_table_scale`: `act_window` AFIP tax

## Menus

- `menu_action_afip_earnings_table_scale_line`: Earnings Scale

## Navigation

- **Parent:** [[docs/Community Addons/l10n_ar_withholding/Views]]

<!-- GENERATED:VIEWFILE -->
