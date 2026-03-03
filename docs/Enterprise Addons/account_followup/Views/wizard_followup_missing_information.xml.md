---
tags: [odoo, enterprise, generated, views]
---

# wizard/followup_missing_information.xml

- Module: [[docs/Enterprise Addons/account_followup/account_followup|account_followup]]
- Scope: Enterprise Addons
- Source file: `wizard/followup_missing_information.xml`
- Views: 2
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `missing_information_view_tree`
- Name: missing.information.view.list
- Model: `res.partner`
- Type: inferred from arch
- Root tag: `list`
- Field references: 7
- Sample fields: `city`, `country_id`, `email`, `name`, `phone`, `street`, `zip`
- XPath or positional patches: 0

### `missing_information_view_form`
- Name: missing.information.view.form
- Model: `account_followup.missing.information.wizard`
- Type: inferred from arch
- Root tag: `form`
- Field references: 0
- Buttons: `view_partners_action`
- XPath or positional patches: 0

## Navigation

- **Parent:** [[docs/Enterprise Addons/account_followup/Views]]

