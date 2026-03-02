<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# l10n_be.281_10

- Module: [[docs/Enterprise Addons/l10n_be_hr_payroll/l10n_be_hr_payroll|l10n_be_hr_payroll]]
- Scope: Enterprise Addons
- Defined in module: yes
- Source files: `models/l10n_be_281_10.py`
- Python classes: `L10n_Be281_10`
- Description: HR Payroll 281.10 Wizard
- Inherits: `hr.payroll.declaration.mixin`

## Field footprint

- Detected fields: 8
- Field types: `Binary` x 1, `Boolean` x 1, `Char` x 2, `Selection` x 4
- Relation fields: 0

## Sample fields

- `error_message`: `Char` (comodel `Error Message`, compute `_compute_validation_state`, store `True`)
- `is_test`: `Boolean`
- `state`: `Selection`
- `type_sending`: `Selection`
- `type_treatment`: `Selection`
- `xml_file`: `Binary` (comodel `XML File`)
- `xml_filename`: `Char`
- `xml_validation_state`: `Selection` (compute `_compute_validation_state`, store `True`)

## Method hints

- Detected methods: 13
- Action methods: `action_generate_declarations`, `action_generate_xml`
- Compute methods: `_compute_display_name`, `_compute_validation_state`
- Onchange methods: none

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_be_hr_payroll/Models]]

<!-- GENERATED:MODEL -->
