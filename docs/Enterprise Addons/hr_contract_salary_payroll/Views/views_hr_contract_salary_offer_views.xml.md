---
tags: [odoo, enterprise, generated, views]
---

# views/hr_contract_salary_offer_views.xml

- Module: [[docs/Enterprise Addons/hr_contract_salary_payroll/hr_contract_salary_payroll|hr_contract_salary_payroll]]
- Scope: Enterprise Addons
- Source file: `views/hr_contract_salary_offer_views.xml`
- Views: 2
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `hr_contract_salary_offer_view_form`
- Name: hr.contract.salary.offer.view.form.salary.calculator
- Model: `hr.contract.salary.offer`
- Type: inferred from arch
- Root tag: `form`
- Field references: 15
- Sample fields: `budget_type`, `currency_id`, `final_yearly_costs`, `gross_wage`, `is_simulation_offer`, `monthly_benefits`, `monthly_employer_cost`, `monthly_wage`, `net_wage`, `resource_calendar_id`, and 5 more
- Buttons: `action_open_salary_configurator`
- XPath or positional patches: 0

### `hr_contract_salary_offer_view_form_inherit`
- Name: hr.contract.salary.offer.view.form.inherit.hr.contract.salary.payroll
- Model: `hr.contract.salary.offer`
- Type: inferred from arch
- Inherits: `hr_contract_salary.hr_contract_salary_offer_view_form`
- Root tag: `xpath`
- Field references: 9
- Sample fields: `budget_type`, `final_yearly_costs`, `gross_wage`, `monthly_benefits`, `monthly_employer_cost`, `monthly_wage`, `net_wage`, `yearly_benefits`, `yearly_employer_cost`
- XPath or positional patches: 3

## Actions

- `action_hr_salary_simulator`: `act_window` Gross-Net Salary Calculator

## Navigation

- **Parent:** [[docs/Enterprise Addons/hr_contract_salary_payroll/Views]]

