---
tags: [odoo, community, generated, views]
---

# views/card_campaign_views.xml

- Module: [[docs/Community Addons/marketing_card/marketing_card|marketing_card]]
- Scope: Community Addons
- Source file: `views/card_campaign_views.xml`
- Views: 4
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `card_campaign_view_search`
- Name: card.campaign.view.search
- Model: `card.campaign`
- Type: inferred from arch
- Root tag: `search`
- Field references: 2
- Sample fields: `name`, `tag_ids`
- XPath or positional patches: 0

### `card_campaign_view_tree`
- Name: card.campaign.view.list
- Model: `card.campaign`
- Type: inferred from arch
- Root tag: `list`
- Field references: 6
- Sample fields: `create_date`, `name`, `res_model`, `tag_ids`, `target_url`, `user_id`
- XPath or positional patches: 0

### `card_campaign_view_kanban`
- Name: card.campaign.view.kanban
- Model: `card.campaign`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 5
- Sample fields: `card_share_count`, `name`, `tag_ids`, `target_url_click_count`, `user_id`
- XPath or positional patches: 0

### `card_campaign_view_form`
- Name: card.campaign.view.form
- Model: `card.campaign`
- Type: inferred from arch
- Root tag: `form`
- Field references: 39
- Sample fields: `card_click_count`, `card_count`, `card_share_count`, `card_template_id`, `content_background`, `content_button`, `content_header`, `content_header_color`, `content_header_dyn`, `content_header_path`, and 29 more
- Buttons: `action_preview`, `action_share`, `action_view_cards`, `action_view_cards_clicked`, `action_view_cards_shared`, `action_view_mailings`
- XPath or positional patches: 0

## Actions

- `card_campaign_action`: `act_window` Card Campaign

## Navigation

- **Parent:** [[docs/Community Addons/marketing_card/Views]]

