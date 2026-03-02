<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/utm_campaign_views.xml

- Module: [[docs/Community Addons/mass_mailing/mass_mailing|mass_mailing]]
- Scope: Community Addons
- Source file: `views/utm_campaign_views.xml`
- Views: 2
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `utm_campaign_view_kanban`
- Name: utm.campaign.view.kanban
- Model: `utm.campaign`
- Type: inferred from arch
- Inherits: `utm.utm_campaign_view_kanban`
- Root tag: `xpath`
- Field references: 2
- Sample fields: `is_mailing_campaign_activated`, `mailing_mail_ids`
- XPath or positional patches: 2

### `utm_campaign_view_form`
- Name: utm.campaign.view.form
- Model: `utm.campaign`
- Type: inferred from arch
- Inherits: `utm.utm_campaign_view_form`
- Root tag: `xpath`
- Field references: 19
- Sample fields: `ab_testing_completed`, `ab_testing_enabled`, `ab_testing_mailings_count`, `ab_testing_schedule_datetime`, `ab_testing_winner_selection`, `bounced_ratio`, `calendar_date`, `campaign_id`, `clicks_ratio`, `is_mailing_campaign_activated`, and 9 more
- Buttons: `%(action_create_mass_mailings_from_campaign)d`, `%(action_view_mass_mailings_from_campaign)d`, `action_duplicate`
- XPath or positional patches: 4

## Actions

- `action_view_utm_campaigns`: `act_window` Campaigns

## Navigation

- **Parent:** [[docs/Community Addons/mass_mailing/Views]]

<!-- GENERATED:VIEWFILE -->
