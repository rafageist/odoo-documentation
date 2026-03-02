<!-- GENERATED:CONTROLLER -->
---
tags: [odoo, enterprise, generated, controller]
---

# HrContractSalary

- Module: [[docs/Enterprise Addons/hr_contract_salary/hr_contract_salary|hr_contract_salary]]
- Scope: Enterprise Addons
- Source file: `controllers/main.py`
- Base classes: `http.Controller`
- Routes: 8

## Routes

### `salary_package_deprecated`
- Paths: `/salary_package/simulation/version/<int:version_id>`
- Type: `http`
- Auth: `public`
- Website route: `True`

### `salary_package`
- Paths: `/salary_package/simulation/offer/<int:offer_id>`
- Type: `http`
- Auth: `public`
- Website route: `True`

### `salary_package_thank_you`
- Paths: `/salary_package/thank_you/<int:offer_id>`
- Type: `http`
- Auth: `public`
- Website route: `True`

### `update_salary`
- Paths: `/salary_package/update_salary`
- Type: `jsonrpc`
- Auth: `public`

### `onchange_benefit`
- Paths: `/salary_package/onchange_benefit`
- Type: `jsonrpc`
- Auth: `public`

### `onchange_personal_info`
- Paths: `/salary_package/onchange_personal_info`
- Type: `jsonrpc`
- Auth: `public`

### `submit`
- Paths: `/salary_package/submit`
- Type: `jsonrpc`
- Auth: `public`

### `refuse`
- Paths: `/salary_package/post_feedback`
- Type: `jsonrpc`
- Auth: `public`

## Navigation

- **Parent:** [[docs/Enterprise Addons/hr_contract_salary/Controllers]]

<!-- GENERATED:CONTROLLER -->
