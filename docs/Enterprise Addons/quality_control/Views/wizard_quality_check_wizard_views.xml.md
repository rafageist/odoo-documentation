---
tags: [odoo, enterprise, generated, views]
---

# wizard/quality_check_wizard_views.xml

- Module: [[docs/Enterprise Addons/quality_control/quality_control|quality_control]]
- Scope: Enterprise Addons
- Source file: `wizard/quality_check_wizard_views.xml`
- Views: 2
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `quality_check_wizard_form_failure`
- Name: quality.check.wizard.form.failure
- Model: `quality.check.wizard`
- Type: inferred from arch
- Root tag: `form`
- Field references: 13
- Sample fields: `failure_location_id`, `failure_message`, `lot_line_id`, `lot_name`, `measure_on`, `potential_failure_location_ids`, `product_id`, `product_tracking`, `qty_failed`, `show_lot_text`, and 3 more
- Buttons: `action_generate_previous_window`, `confirm_fail`, `confirm_measure`, `correct_measure`
- XPath or positional patches: 0

### `view_quality_check_wizard`
- Name: quality_check_wizard
- Model: `quality.check.wizard`
- Type: inferred from arch
- Root tag: `form`
- Field references: 20
- Sample fields: `additional_note`, `current_check_id`, `is_last_check`, `is_lot_tested_fractionally`, `measure`, `measure_on`, `nb_checks`, `norm_unit`, `note`, `picture`, and 10 more
- Buttons: `action_generate_next_window`, `action_generate_previous_window`, `action_open_spreadsheet`, `do_fail`, `do_measure`, `do_pass`
- XPath or positional patches: 0

## Actions

- `action_quality_check_wizard`: `act_window` Quality Check

## Navigation

- **Parent:** [[docs/Enterprise Addons/quality_control/Views]]

