<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/utm_campaign_views.xml

- Module: [[docs/Community Addons/sale/sale|sale]]
- Scope: Community Addons
- Source file: `views/utm_campaign_views.xml`
- Views: 2
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `utm_campaign_view_form`
- Name: utm.campaign.view.form
- Model: `utm.campaign`
- Type: inferred from arch
- Inherits: `utm.utm_campaign_view_form`
- Root tag: `xpath`
- Field references: 2
- Sample fields: `invoiced_amount`, `quotation_count`
- Buttons: `action_redirect_to_invoiced`, `action_redirect_to_quotations`
- XPath or positional patches: 1

### `utm_campaign_view_kanban`
- Name: utm.campaign.view.kanban
- Model: `utm.campaign`
- Type: inferred from arch
- Inherits: `utm.utm_campaign_view_kanban`
- Root tag: `xpath`
- Field references: 3
- Sample fields: `currency_id`, `invoiced_amount`, `quotation_count`
- XPath or positional patches: 1

## Navigation

- **Parent:** [[docs/Community Addons/sale/Views]]

<!-- GENERATED:VIEWFILE -->
