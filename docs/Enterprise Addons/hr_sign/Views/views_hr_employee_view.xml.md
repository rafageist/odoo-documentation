<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/hr_employee_view.xml

- Module: [[docs/Enterprise Addons/hr_sign/hr_sign|hr_sign]]
- Scope: Enterprise Addons
- Source file: `views/hr_employee_view.xml`
- Views: 1
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `hr_employee_sign_view_form`
- Name: hr.employee.form
- Model: `hr.employee`
- Type: inferred from arch
- Inherits: `hr.view_employee_form`
- Root tag: `xpath`
- Field references: 2
- Sample fields: `sign_request_count`, `sign_request_ids`
- Buttons: `%(sign_contract_wizard_action)d`, `action_open_versions`, `open_employee_sign_requests`
- XPath or positional patches: 2

## Actions

- `action_signature_request_multi`: `server` Signature Request

## Navigation

- **Parent:** [[docs/Enterprise Addons/hr_sign/Views]]

<!-- GENERATED:VIEWFILE -->
