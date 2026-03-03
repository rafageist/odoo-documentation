---
tags: [odoo, community, generated, views]
---

# views/rating_rating_views.xml

- Module: [[docs/Community Addons/website_slides/website_slides|website_slides]]
- Scope: Community Addons
- Source file: `views/rating_rating_views.xml`
- Views: 5
- Actions: 6
- Menus: 0
- Rules: 0

## View records

### `rating_rating_view_form_slides`
- Name: rating.rating.view.form.slides
- Model: `rating.rating`
- Type: inferred from arch
- Root tag: `form`
- Field references: 6
- Sample fields: `feedback`, `is_internal`, `partner_id`, `rated_on`, `rating`, `resource_ref`
- XPath or positional patches: 0

### `rating_rating_view_tree_slide_channel`
- Name: rating.rating.view.list.slides
- Model: `rating.rating`
- Type: inferred from arch
- Root tag: `list`
- Field references: 5
- Sample fields: `feedback`, `partner_id`, `rated_on`, `rating`, `res_name`
- XPath or positional patches: 0

### `rating_rating_view_pivot_slide_channel`
- Name: rating.rating.view.pivot.slides
- Model: `rating.rating`
- Type: inferred from arch
- Root tag: `pivot`
- Field references: 3
- Sample fields: `rating`, `rating_text`, `res_name`
- XPath or positional patches: 0

### `rating_rating_view_graph_slide_channel`
- Name: rating.rating.view.graph.slides
- Model: `rating.rating`
- Type: inferred from arch
- Root tag: `graph`
- Field references: 4
- Sample fields: `parent_res_id`, `rating`, `res_id`, `res_name`
- XPath or positional patches: 0

### `rating_rating_view_search_slide_channel`
- Name: rating.rating.view.search.slides
- Model: `rating.rating`
- Type: inferred from arch
- Inherits: `rating.rating_rating_view_search`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 5

## Actions

- `rating_rating_action_slide_channel_view_form`: `view`
- `rating_rating_action_slide_channel_view_tree`: `view`
- `rating_rating_action_slide_channel_view_pivot`: `view`
- `rating_rating_action_slide_channel_view_graph`: `view`
- `rating_rating_action_slide_channel_view_kanban`: `view`
- `rating_rating_action_slide_channel`: `act_window` Reviews

## Navigation

- **Parent:** [[docs/Community Addons/website_slides/Views]]

