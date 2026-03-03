---
tags: [odoo, enterprise, generated, views]
---

# wizard/import_wizard_view.xml

- Module: [[docs/Enterprise Addons/account_saft_import/account_saft_import|account_saft_import]]
- Scope: Enterprise Addons
- Source file: `wizard/import_wizard_view.xml`
- Views: 1
- Actions: 2
- Menus: 0
- Rules: 0

## View records

### `account_saft_import_form`
- Name: account_saft.import.form
- Model: `account.saft.import.wizard`
- Type: inferred from arch
- Root tag: `form`
- Field references: 3
- Sample fields: `attachment_id`, `attachment_name`, `import_opening_balance`
- Buttons: `action_import`
- XPath or positional patches: 0

## Actions

- `account_saft_import_action`: `server` SAF-T Import
- `open_saft_import_wizard`: `act_window` SAF-T Import

## Navigation

- **Parent:** [[docs/Enterprise Addons/account_saft_import/Views]]

