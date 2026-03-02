<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# hr.version

- Module: [[docs/Enterprise Addons/l10n_be_hr_payroll/l10n_be_hr_payroll|l10n_be_hr_payroll]]
- Scope: Enterprise Addons
- Defined in module: extension only
- Source files: `models/hr_version.py`
- Python classes: `HrVersion`

## Field footprint

- Detected fields: 80
- Field types: `Boolean` x 20, `Char` x 1, `Float` x 9, `Integer` x 17, `Monetary` x 29, `Selection` x 2, `Text` x 2
- Relation fields: 0

## Sample fields

- `car_atn`: `Monetary`
- `commission_on_target`: `Monetary`
- `company_car_total_depreciated_cost`: `Monetary`
- `dependent_children`: `Integer` (compute `_compute_dependent_children`)
- `dependent_juniors`: `Integer` (compute `_compute_dependent_people`)
- `dependent_seniors`: `Integer` (compute `_compute_dependent_people`)
- `disabled_children_bool`: `Boolean`
- `disabled_children_number`: `Integer` (comodel `Number of disabled children`)
- `disabled_spouse_bool`: `Boolean`
- `eco_checks`: `Monetary` (comodel `Eco Vouchers`)
- `employee_age`: `Integer` (comodel `Age of Employee`, compute `_compute_employee_age`)
- `fiscal_voluntarism`: `Monetary`
- `fuel_card`: `Monetary`
- `has_bicycle`: `Boolean`
- `has_hospital_insurance`: `Boolean`
- `has_laptop`: `Boolean`
- `hospital_insurance_amount_per_adult`: `Float`
- `hospital_insurance_amount_per_child`: `Float`
- `insurance_amount`: `Float` (compute `_compute_insurance_amount`)
- `insured_relative_adults`: `Integer`

## Method hints

- Detected methods: 52
- Action methods: `action_work_schedule_change_wizard`
- Compute methods: `_compute_ambulatory_insurance_amount`, `_compute_ambulatory_insured_adults_total`, `_compute_commission_cost`, `_compute_dependent_children`, `_compute_dependent_people`, `_compute_employee_age`, `_compute_final_yearly_costs`, `_compute_insurance_amount`, and 11 more
- Onchange methods: `_onchange_has_hospital_insurance`, `_onchange_l10n_be_has_ambulatory_insurance`, `_onchange_transport_mode`, `_onchange_transport_mode_private_car`

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_be_hr_payroll/Models]]

<!-- GENERATED:MODEL -->
