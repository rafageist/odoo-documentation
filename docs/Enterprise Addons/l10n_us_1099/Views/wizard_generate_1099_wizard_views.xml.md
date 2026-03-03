---
tags: [odoo, enterprise, generated, views]
---

# wizard/generate_1099_wizard_views.xml

- Module: [[docs/Enterprise Addons/l10n_us_1099/l10n_us_1099|l10n_us_1099]]
- Scope: Enterprise Addons
- Source file: `wizard/generate_1099_wizard_views.xml`
- Views: 1
- Actions: 1
- Menus: 1
- Rules: 0

## View records

### `view_l10n_us_1099_wizard`
- Name: Update the current value of the Goal
- Model: `l10n_us_1099.wizard`
- Type: inferred from arch
- Root tag: `form`
- Field references: 11
- Sample fields: `account_id`, `credit`, `date`, `debit`, `end_date`, `journal_id`, `lines_to_export`, `move_id`, `name`, `partner_id`, and 1 more
- Buttons: `action_generate`
- XPath or positional patches: 0

## Actions

- `view_l10n_us_1099_wizard_act_window`: `act_window` 1099 Report

## Menus

- `menu_action_view_l10n_us_1099_wizard`: 1099 Report…

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_us_1099/Views]]

