---
tags: [odoo, enterprise, generated, views]
---

# views/hr_referral_onboarding_views.xml

- Module: [[docs/Enterprise Addons/hr_referral/hr_referral|hr_referral]]
- Scope: Enterprise Addons
- Source file: `views/hr_referral_onboarding_views.xml`
- Views: 2
- Actions: 1
- Menus: 1
- Rules: 0

## View records

### `view_hr_referral_onboarding_tree`
- Name: hr.referral.onboarding.list
- Model: `hr.referral.onboarding`
- Type: inferred from arch
- Root tag: `list`
- Field references: 4
- Sample fields: `company_id`, `image`, `sequence`, `text`
- Buttons: `action_relaunch_onboarding`
- XPath or positional patches: 0

### `view_hr_referral_onboarding_form`
- Name: hr.referral.onboarding.form
- Model: `hr.referral.onboarding`
- Type: inferred from arch
- Root tag: `form`
- Field references: 4
- Sample fields: `company_id`, `image`, `sequence`, `text`
- XPath or positional patches: 0

## Actions

- `action_hr_referral_onboarding_configuration`: `act_window` Onboarding

## Menus

- `menu_hr_referral_onboarding_configuration`: unnamed

## Navigation

- **Parent:** [[docs/Enterprise Addons/hr_referral/Views]]

