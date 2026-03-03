---
tags: [odoo, enterprise, generated, views]
---

# views/mailing_mailing_views.xml

- Module: [[docs/Enterprise Addons/marketing_automation/marketing_automation|marketing_automation]]
- Scope: Enterprise Addons
- Source file: `views/mailing_mailing_views.xml`
- Views: 2
- Actions: 5
- Menus: 0
- Rules: 0

## View records

### `mailing_mailing_view_form_marketing_automation`
- Name: mailing.mailing.view.form.marketing.automation
- Model: `mailing.mailing`
- Type: inferred from arch
- Inherits: `mass_mailing.view_mail_mass_mailing_form`
- Root tag: `xpath`
- Field references: 4
- Sample fields: `body_arch`, `is_body_empty`, `mailing_domain`, `marketing_activity_ids`
- XPath or positional patches: 16

### `mailing_mailing_view_tree_marketing_automation`
- Name: mailing.mailing.view.list.marketing.automation
- Model: `mailing.mailing`
- Type: inferred from arch
- Inherits: `mass_mailing.view_mail_mass_mailing_tree`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `marketing_activity_ids`
- XPath or positional patches: 2

## Actions

- `mailing_mailing_action_view_form`: `act_window` Marketing Automation Mailings
- `mail_mass_mailing_action_marketing_automation_form`: `view`
- `mail_mass_mailing_action_marketing_automation_tree`: `view`
- `mail_mass_mailing_action_marketing_automation`: `act_window` Marketing Automation Mailings
- `mass_mailing.mailing_mailing_action_mail`: `act_window`

## Navigation

- **Parent:** [[docs/Enterprise Addons/marketing_automation/Views]]

