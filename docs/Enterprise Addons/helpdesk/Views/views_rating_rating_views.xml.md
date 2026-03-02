<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/rating_rating_views.xml

- Module: [[docs/Enterprise Addons/helpdesk/helpdesk|helpdesk]]
- Scope: Enterprise Addons
- Source file: `views/rating_rating_views.xml`
- Views: 9
- Actions: 6
- Menus: 0
- Rules: 0

## View records

### `rating_rating_view_form_inherit_helpdesk`
- Name: rating.rating.form.helpdesk
- Model: `rating.rating`
- Type: inferred from arch
- Inherits: `rating.rating_rating_view_form`
- Root tag: `field`
- Field references: 8
- Sample fields: `feedback`, `is_internal`, `parent_ref`, `partner_id`, `rated_on`, `rated_partner_id`, `rating_text`, `resource_ref`
- XPath or positional patches: 1

### `rating_rating_view_search_inherit_helpdesk`
- Name: rating.rating.search.helpdesk
- Model: `rating.rating`
- Type: inferred from arch
- Inherits: `rating.rating_rating_view_search`
- Root tag: `field`
- Field references: 4
- Sample fields: `feedback`, `parent_res_name`, `rated_partner_id`, `res_name`
- XPath or positional patches: 6

### `rating_rating_view_seven_days_graph_inherit_helpdesk`
- Name: rating.rating.graph.seven.days.helpdesk
- Model: `rating.rating`
- Type: inferred from arch
- Inherits: `rating_rating_view_graph_inherit_helpdesk`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

### `rating_rating_view_today_graph_inherit_helpdesk`
- Name: rating.rating.graph.today.helpdesk
- Model: `rating.rating`
- Type: inferred from arch
- Inherits: `rating_rating_view_graph_inherit_helpdesk`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

### `rating_rating_view_graph_inherit_helpdesk`
- Name: rating.rating.graph.helpdesk
- Model: `rating.rating`
- Type: inferred from arch
- Inherits: `rating.rating_rating_view_graph`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 2

### `rating_rating_view_seven_days_pivot_inherit_helpdesk`
- Name: rating.rating.seven.days.pivot.helpdesk
- Model: `rating.rating`
- Type: inferred from arch
- Inherits: `rating_rating_pivot_inherit_helpdesk`
- Root tag: `field`
- Field references: 1
- Sample fields: `rated_on`
- XPath or positional patches: 1

### `rating_rating_view_today_pivot_inherit_helpdesk`
- Name: rating.rating.today.pivot.helpdesk
- Model: `rating.rating`
- Type: inferred from arch
- Inherits: `rating_rating_pivot_inherit_helpdesk`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `rated_on`
- XPath or positional patches: 1

### `rating_rating_pivot_inherit_helpdesk`
- Name: rating.rating.pivot.inherit.helpdesk
- Model: `rating.rating`
- Type: inferred from arch
- Inherits: `rating.rating_rating_view_pivot`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

### `rating_rating_view_tree_inherit_helpdesk`
- Name: rating.rating.list.helpdesk
- Model: `rating.rating`
- Type: inferred from arch
- Inherits: `rating.rating_rating_view_tree`
- Root tag: `field`
- Field references: 3
- Sample fields: `parent_res_name`, `rated_partner_id`, `res_name`
- XPath or positional patches: 0

## Actions

- `rating_rating_action_helpdesk_graph`: `view`
- `rating_rating_action_helpdesk_pivot`: `view`
- `rating_rating_action_helpdesk_form`: `view`
- `rating_rating_action_helpdesk_tree`: `view`
- `rating_rating_action_helpdesk_kanban`: `view`
- `rating_rating_action_helpdesk`: `act_window` Customer Ratings

## Navigation

- **Parent:** [[docs/Enterprise Addons/helpdesk/Views]]

<!-- GENERATED:VIEWFILE -->
