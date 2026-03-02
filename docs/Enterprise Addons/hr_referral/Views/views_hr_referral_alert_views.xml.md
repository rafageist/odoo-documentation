<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/hr_referral_alert_views.xml

- Module: [[docs/Enterprise Addons/hr_referral/hr_referral|hr_referral]]
- Scope: Enterprise Addons
- Source file: `views/hr_referral_alert_views.xml`
- Views: 3
- Actions: 1
- Menus: 1
- Rules: 0

## View records

### `hr_referral_alert_view_search`
- Name: hr.referral.alert.view.search
- Model: `hr.referral.alert`
- Type: inferred from arch
- Root tag: `search`
- Field references: 1
- Sample fields: `name`
- XPath or positional patches: 0

### `view_hr_referral_alert_tree`
- Name: hr.referral.alert.list
- Model: `hr.referral.alert`
- Type: inferred from arch
- Root tag: `list`
- Field references: 3
- Sample fields: `date_from`, `date_to`, `name`
- XPath or positional patches: 0

### `view_hr_referral_alert_form`
- Name: hr.referral.alert.form
- Model: `hr.referral.alert`
- Type: inferred from arch
- Root tag: `form`
- Field references: 7
- Sample fields: `active`, `company_id`, `date_from`, `date_to`, `name`, `onclick`, `url`
- Buttons: `%(hr_referral_alert_mail_wizard_action)d`
- XPath or positional patches: 0

## Actions

- `action_hr_referral_alert_configuration`: `act_window` Alerts

## Menus

- `menu_hr_referral_alert_configuration`: unnamed

## Navigation

- **Parent:** [[docs/Enterprise Addons/hr_referral/Views]]

<!-- GENERATED:VIEWFILE -->
