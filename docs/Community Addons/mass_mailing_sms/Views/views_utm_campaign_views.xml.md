<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/utm_campaign_views.xml

- Module: [[docs/Community Addons/mass_mailing_sms/mass_mailing_sms|mass_mailing_sms]]
- Scope: Community Addons
- Source file: `views/utm_campaign_views.xml`
- Views: 2
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `utm_campaign_view_kanban`
- Name: utm.campaign.view.kanban
- Model: `utm.campaign`
- Type: inferred from arch
- Inherits: `utm.utm_campaign_view_kanban`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `mailing_sms_count`
- XPath or positional patches: 1

### `utm_campaign_view_form`
- Name: utm.campaign.view.form
- Model: `utm.campaign`
- Type: inferred from arch
- Inherits: `utm.utm_campaign_view_form`
- Root tag: `xpath`
- Field references: 14
- Sample fields: `ab_testing_enabled`, `ab_testing_mailings_sms_count`, `bounced`, `calendar_date`, `campaign_id`, `clicked`, `mailing_model_id`, `mailing_sms_count`, `mailing_sms_ids`, `mailing_type`, and 4 more
- Buttons: `action_create_mass_sms`, `action_duplicate`, `action_redirect_to_mailing_sms`
- XPath or positional patches: 5

## Navigation

- **Parent:** [[docs/Community Addons/mass_mailing_sms/Views]]

<!-- GENERATED:VIEWFILE -->
