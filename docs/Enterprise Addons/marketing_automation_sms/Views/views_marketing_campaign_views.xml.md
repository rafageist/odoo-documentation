<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/marketing_campaign_views.xml

- Module: [[docs/Enterprise Addons/marketing_automation_sms/marketing_automation_sms|marketing_automation_sms]]
- Scope: Enterprise Addons
- Source file: `views/marketing_campaign_views.xml`
- Views: 2
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `marketing_campaign_view_tree`
- Name: marketing.campaign.view.list.inherit.marketing.automation.sms
- Model: `marketing.campaign`
- Type: inferred from arch
- Inherits: `marketing_automation.marketing_campaign_view_tree`
- Root tag: `field`
- Field references: 2
- Sample fields: `mailing_sms_count`, `mass_mailing_count`
- XPath or positional patches: 0

### `marketing_campaign_view_form`
- Name: marketing.campaign.view.form
- Model: `marketing.campaign`
- Type: inferred from arch
- Inherits: `marketing_automation.marketing_campaign_view_form`
- Root tag: `xpath`
- Field references: 2
- Sample fields: `mailing_sms_count`, `total_sent`
- Buttons: `action_view_sms`
- XPath or positional patches: 5

## Navigation

- **Parent:** [[docs/Enterprise Addons/marketing_automation_sms/Views]]

<!-- GENERATED:VIEWFILE -->
