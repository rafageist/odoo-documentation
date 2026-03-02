<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/partner_view.xml

- Module: [[docs/Enterprise Addons/account_followup/account_followup|account_followup]]
- Scope: Enterprise Addons
- Source file: `views/partner_view.xml`
- Views: 2
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `view_partner_property_form_followup`
- Name: res.partner.property.form.followup
- Model: `res.partner`
- Type: inferred from arch
- Inherits: `account.view_partner_property_form`
- Root tag: `group`
- Field references: 6
- Sample fields: `company_id`, `followup_line_id`, `followup_next_action_date`, `followup_reminder_type`, `followup_responsible_id`, `followup_status`
- XPath or positional patches: 1

### `res_partner_view_form`
- Name: res.partner.view.form
- Model: `res.partner`
- Type: inferred from arch
- Inherits: `base.view_partner_form`
- Root tag: `div`
- Field references: 1
- Sample fields: `total_all_due`
- Buttons: `open_follow_up_report`
- XPath or positional patches: 1

## Navigation

- **Parent:** [[docs/Enterprise Addons/account_followup/Views]]

<!-- GENERATED:VIEWFILE -->
