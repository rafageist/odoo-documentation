---
tags: [odoo, community, generated, views]
---

# views/rating_rating_views.xml

- Module: [[docs/Community Addons/rating/rating|rating]]
- Scope: Community Addons
- Source file: `views/rating_rating_views.xml`
- Views: 8
- Actions: 3
- Menus: 1
- Rules: 0

## View records

### `rating_rating_view_search`
- Name: rating.rating.search
- Model: `rating.rating`
- Type: inferred from arch
- Root tag: `search`
- Field references: 6
- Sample fields: `parent_res_name`, `partner_id`, `rated_partner_id`, `rating`, `res_id`, `res_name`
- XPath or positional patches: 0

### `rating_rating_view_graph`
- Name: rating.rating.graph
- Model: `rating.rating`
- Type: inferred from arch
- Root tag: `graph`
- Field references: 4
- Sample fields: `parent_res_id`, `rated_on`, `rating`, `res_id`
- XPath or positional patches: 0

### `rating_rating_view_pivot`
- Name: rating.rating.pivot
- Model: `rating.rating`
- Type: inferred from arch
- Root tag: `pivot`
- Field references: 5
- Sample fields: `parent_res_id`, `rated_on`, `rated_partner_id`, `rating`, `res_id`
- XPath or positional patches: 0

### `rating_rating_view_kanban_stars`
- Name: rating.rating.view.kanban.stars
- Model: `rating.rating`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 5
- Sample fields: `feedback`, `partner_id`, `rated_on`, `rating`, `res_name`
- XPath or positional patches: 0

### `rating_rating_view_kanban`
- Name: rating.rating.kanban
- Model: `rating.rating`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 6
- Sample fields: `feedback`, `partner_id`, `rated_on`, `rated_partner_name`, `rating_image`, `res_name`
- XPath or positional patches: 0

### `rating_rating_view_form_text`
- Name: rating.rating.view.form.text
- Model: `rating.rating`
- Type: inferred from arch
- Inherits: `rating.rating_rating_view_form`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `rating_text`
- XPath or positional patches: 1

### `rating_rating_view_form`
- Name: rating.rating.form
- Model: `rating.rating`
- Type: inferred from arch
- Root tag: `form`
- Field references: 13
- Sample fields: `consumed`, `feedback`, `is_internal`, `parent_ref`, `parent_res_name`, `partner_id`, `rated_on`, `rated_partner_id`, `rating`, `rating_image`, and 3 more
- XPath or positional patches: 0

### `rating_rating_view_tree`
- Name: rating.rating.list
- Model: `rating.rating`
- Type: inferred from arch
- Root tag: `list`
- Field references: 7
- Sample fields: `create_date`, `feedback`, `parent_res_name`, `partner_id`, `rated_partner_id`, `rating_text`, `res_name`
- XPath or positional patches: 0

## Actions

- `rating_rating_action_view_form`: `view`
- `rating_rating_action_view_kanban`: `view`
- `rating_rating_action`: `act_window` Ratings

## Menus

- `rating_rating_menu_technical`: Ratings

## Navigation

- **Parent:** [[docs/Community Addons/rating/Views]]

