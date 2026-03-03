---
tags: [odoo, community, generated, views]
---

# views/rating_rating_views.xml

- Module: [[docs/Community Addons/project/project|project]]
- Scope: Community Addons
- Source file: `views/rating_rating_views.xml`
- Views: 5
- Actions: 18
- Menus: 0
- Rules: 0

## View records

### `rating_rating_view_search_project`
- Name: rating.rating.search.project
- Model: `rating.rating`
- Type: inferred from arch
- Inherits: `rating.rating_rating_view_search`
- Root tag: `xpath`
- Field references: 2
- Sample fields: `parent_res_name`, `res_name`
- XPath or positional patches: 12

### `rating_rating_view_graph`
- Name: rating.rating.view.graph.project
- Model: `rating.rating`
- Type: inferred from arch
- Inherits: `rating.rating_rating_view_graph`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

### `rating_rating_view_pivot`
- Name: rating.rating.view.pivot.project
- Model: `rating.rating`
- Type: inferred from arch
- Inherits: `rating.rating_rating_view_pivot`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 2

### `rating_rating_view_form_project`
- Name: rating.rating.form.project
- Model: `rating.rating`
- Type: inferred from arch
- Inherits: `rating.rating_rating_view_form_text`
- Root tag: `xpath`
- Field references: 8
- Sample fields: `feedback`, `parent_ref`, `parent_res_name`, `partner_id`, `rated_on`, `rated_partner_id`, `res_name`, `resource_ref`
- XPath or positional patches: 2

### `rating_rating_view_tree_project`
- Name: rating.rating.list.project
- Model: `rating.rating`
- Type: inferred from arch
- Inherits: `rating.rating_rating_view_tree`
- Root tag: `field`
- Field references: 3
- Sample fields: `parent_res_name`, `rated_partner_id`, `res_name`
- XPath or positional patches: 0

## Actions

- `rating_rating_action_project_report_graph`: `view`
- `rating_rating_action_project_report_pivot`: `view`
- `rating_rating_action_project_report_form`: `view`
- `rating_rating_action_project_report_tree`: `view`
- `rating_rating_action_project_report_kanban`: `view`
- `rating_rating_action_project_report`: `act_window` Customer Ratings
- `rating_rating_action_task_graph`: `view`
- `rating_rating_action_task_pivot`: `view`
- `rating_rating_action_task_form`: `view`
- `rating_rating_action_task_tree`: `view`
- `rating_rating_action_task_kanban`: `view`
- `rating_rating_action_task`: `act_window` Ratings
- `rating_rating_action_view_project_rating_graph`: `view`
- `rating_rating_action_view_project_rating_pivot`: `view`
- `rating_rating_action_view_project_rating_form`: `view`
- `rating_rating_action_view_project_rating_tree`: `view`
- `rating_rating_action_view_project_rating_kanban`: `view`
- `rating_rating_action_view_project_rating`: `act_window` Ratings

## Navigation

- **Parent:** [[docs/Community Addons/project/Views]]

