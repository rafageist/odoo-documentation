<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# hr.employee

- Module: [[docs/Enterprise Addons/hr_contract_salary/hr_contract_salary|hr_contract_salary]]
- Scope: Enterprise Addons
- Defined in module: extension only
- Source files: `models/hr_employee.py`
- Python classes: `HrEmployee`

## Field footprint

- Detected fields: 4
- Field types: `Monetary` x 4
- Relation fields: 0

## Sample fields

- `final_yearly_costs`: `Monetary` (related `version_id.final_yearly_costs`)
- `monthly_yearly_costs`: `Monetary` (related `version_id.monthly_yearly_costs`)
- `wage_on_signature`: `Monetary` (related `version_id.wage_on_signature`)
- `wage_with_holidays`: `Monetary` (related `version_id.wage_with_holidays`)

## Method hints

- Detected methods: 6
- Action methods: `action_generate_offer`, `action_show_contract_reviews`, `action_show_offers`
- Compute methods: none
- Onchange methods: `_onchange_final_yearly_costs`, `_onchange_wage_with_holidays`

## Navigation

- **Parent:** [[docs/Enterprise Addons/hr_contract_salary/Models]]

<!-- GENERATED:MODEL -->
