---
tags: [odoo, community, generated, views]
---

# views/utm_campaign_views.xml

- Module: [[docs/Community Addons/link_tracker/link_tracker|link_tracker]]
- Scope: Community Addons
- Source file: `views/utm_campaign_views.xml`
- Views: 2
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `utm_campaign_view_kanban`
- Name: utm.campaign.view.form
- Model: `utm.campaign`
- Type: inferred from arch
- Inherits: `utm.utm_campaign_view_kanban`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `click_count`
- XPath or positional patches: 1

### `utm_campaign_view_form`
- Name: utm.campaign.view.form
- Model: `utm.campaign`
- Type: inferred from arch
- Inherits: `utm.utm_campaign_view_form`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `click_count`
- Buttons: `%(link_tracker_action_campaign)d`
- XPath or positional patches: 1

## Navigation

- **Parent:** [[docs/Community Addons/link_tracker/Views]]

