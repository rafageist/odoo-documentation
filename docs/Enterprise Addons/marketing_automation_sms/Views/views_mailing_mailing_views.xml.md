---
tags: [odoo, enterprise, generated, views]
---

# views/mailing_mailing_views.xml

- Module: [[docs/Enterprise Addons/marketing_automation_sms/marketing_automation_sms|marketing_automation_sms]]
- Scope: Enterprise Addons
- Source file: `views/mailing_mailing_views.xml`
- Views: 2
- Actions: 4
- Menus: 0
- Rules: 0

## View records

### `mailing_mailing_view_tree_marketing_automation_sms`
- Name: mailing.mailing.view.list.marketing.automation
- Model: `mailing.mailing`
- Type: inferred from arch
- Inherits: `marketing_automation.mailing_mailing_view_tree_marketing_automation`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `sms_subject`
- XPath or positional patches: 4

### `mailing_mailing_view_form_marketing_automation`
- Name: mailing.mailing.view.form.marketing.activity.inherit.sms
- Model: `mailing.mailing`
- Type: inferred from arch
- Inherits: `marketing_automation.mailing_mailing_view_form_marketing_automation`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 5

## Actions

- `mail_mass_mailing_action_marketing_automation_sms_form`: `view`
- `mail_mass_mailing_action_marketing_automation_sms_tree`: `view`
- `mail_mass_mailing_action_marketing_automation_sms`: `act_window` Marketing Automation SMS
- `mass_mailing_sms.mailing_mailing_action_sms`: `act_window`

## Navigation

- **Parent:** [[docs/Enterprise Addons/marketing_automation_sms/Views]]

