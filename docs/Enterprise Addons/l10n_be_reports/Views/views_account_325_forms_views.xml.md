<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/account_325_forms_views.xml

- Module: [[docs/Enterprise Addons/l10n_be_reports/l10n_be_reports|l10n_be_reports]]
- Scope: Enterprise Addons
- Source file: `views/account_325_forms_views.xml`
- Views: 3
- Actions: 2
- Menus: 1
- Rules: 0

## View records

### `form_281_50_view_form`
- Name: l10n_be.form.281.50.view.form
- Model: `l10n_be.form.281.50`
- Type: inferred from arch
- Root tag: `form`
- Field references: 17
- Sample fields: `atn`, `commissions`, `country_id`, `exposed_expenses`, `fees`, `paid_amount`, `partner_address`, `partner_bce_number`, `partner_citizen_identification`, `partner_city`, and 7 more
- Buttons: `action_download_281_50_individual_pdf`
- XPath or positional patches: 0

### `form_325_view_form`
- Name: l10n_be.form.325.view.form
- Model: `l10n_be.form.325`
- Type: inferred from arch
- Root tag: `form`
- Field references: 20
- Sample fields: `atn`, `commissions`, `debtor_id`, `exposed_expenses`, `fees`, `form_281_50_count`, `form_281_50_ids`, `form_281_50_total_amount`, `is_test`, `official_id`, and 10 more
- Buttons: `action_generate_281_50_form_pdf`, `action_generate_281_50_form_xml`, `action_generate_325_form_pdf`, `action_open_281_50_view_form`
- XPath or positional patches: 0

### `form_325_view_tree`
- Name: l10n_be.form.325.view.list
- Model: `l10n_be.form.325`
- Type: inferred from arch
- Root tag: `list`
- Field references: 8
- Sample fields: `debtor_id`, `form_281_50_count`, `is_test`, `reference_year`, `sender_id`, `sending_type`, `state`, `treatment_type`
- XPath or positional patches: 0

## Actions

- `action_open_325_tree_view`: `act_window` 325 forms
- `action_open_create_325_form`: `act_window` Create 325 form

## Menus

- `menu_action_open_325_tree_view`: Open 325 forms

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_be_reports/Views]]

<!-- GENERATED:VIEWFILE -->
