---
tags: [odoo, enterprise, generated, views]
---

# views/quality_views.xml

- Module: [[docs/Enterprise Addons/quality_control/quality_control|quality_control]]
- Scope: Enterprise Addons
- Source file: `views/quality_views.xml`
- Views: 28
- Actions: 15
- Menus: 14
- Rules: 0

## View records

### `quality_point_view_form_inherit_quality_control`
- Name: quality.point.view.form.inherit.quality.control
- Model: `quality.point`
- Type: inferred from arch
- Inherits: `quality.quality_point_view_form`
- Root tag: `xpath`
- Field references: 16
- Sample fields: `average`, `check_count`, `failure_message`, `measure_frequency_type`, `measure_frequency_unit`, `measure_frequency_unit_value`, `measure_frequency_value`, `measure_on`, `norm`, `norm_unit`, and 6 more
- Buttons: `action_see_quality_checks`, `action_see_spc_control`
- XPath or positional patches: 4

### `view_quality_point_kanban`
- Name: quality.point.kanban
- Model: `quality.point`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 7
- Sample fields: `company_id`, `measure_on`, `name`, `team_id`, `test_type_id`, `title`, `user_id`
- XPath or positional patches: 0

### `quality_point_view_search`
- Name: quality.point.view.search
- Model: `quality.point`
- Type: inferred from arch
- Root tag: `search`
- Field references: 4
- Sample fields: `name`, `picking_type_ids`, `product_ids`, `test_type_id`
- XPath or positional patches: 0

### `quality_point_view_tree`
- Name: quality.point.view.list.inherit.quality.control
- Model: `quality.point`
- Type: inferred from arch
- Inherits: `quality.quality_point_view_tree`
- Root tag: `xpath`
- Field references: 4
- Sample fields: `is_lot_tested_fractionally`, `measure_frequency_type`, `measure_on`, `testing_percentage_within_lot`
- XPath or positional patches: 1

### `view_quality_alert_stage_kanban`
- Name: quality.alert.stage.kanban
- Model: `quality.alert.stage`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 1
- Sample fields: `name`
- XPath or positional patches: 0

### `quality_alert_stage_view_tree`
- Name: quality.alert.stage.list
- Model: `quality.alert.stage`
- Type: inferred from arch
- Root tag: `list`
- Field references: 5
- Sample fields: `done`, `folded`, `name`, `sequence`, `team_ids`
- XPath or positional patches: 0

### `quality_tag_view_tree`
- Name: quality.tag.view.list
- Model: `quality.tag`
- Type: inferred from arch
- Root tag: `list`
- Field references: 1
- Sample fields: `name`
- XPath or positional patches: 0

### `quality_tag_view_search`
- Name: quality.tag.view.search
- Model: `quality.tag`
- Type: inferred from arch
- Root tag: `search`
- Field references: 1
- Sample fields: `name`
- XPath or positional patches: 0

### `quality_spreadsheet_template_view_list`
- Name: quality.spreadsheet.template.list
- Model: `quality.spreadsheet.template`
- Type: inferred from arch
- Root tag: `list`
- Field references: 5
- Sample fields: `check_cell`, `company_id`, `name`, `spreadsheet_binary_data`, `spreadsheet_file_name`
- Buttons: `action_open_spreadsheet`
- XPath or positional patches: 0

### `quality_alert_team_view_kanban`
- Name: quality.alert.team.view.kanban
- Model: `quality.alert.team`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 1
- Sample fields: `name`
- XPath or positional patches: 0

### `quality_alert_team_view_tree`
- Name: quality.alert.team.view.list
- Model: `quality.alert.team`
- Type: inferred from arch
- Root tag: `list`
- Field references: 3
- Sample fields: `company_id`, `name`, `sequence`
- XPath or positional patches: 0

### `quality_alert_team_view_form`
- Name: quality.alert.team.view.form
- Model: `quality.alert.team`
- Type: inferred from arch
- Root tag: `form`
- Field references: 6
- Sample fields: `alias_contact`, `alias_domain_id`, `alias_id`, `alias_name`, `company_id`, `name`
- XPath or positional patches: 0

### `quality_alert_team_dashboard_view_kanban`
- Name: quality.alert.team.view.kanban
- Model: `quality.alert.team`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 6
- Sample fields: `alert_count`, `alias_email`, `alias_id`, `check_count`, `color`, `name`
- Buttons: `%(quality_alert_action_team)d`
- XPath or positional patches: 0

### `product_product_form_view_quality_control`
- Name: product.product.quality
- Model: `product.product`
- Type: inferred from arch
- Inherits: `stock.product_form_view_procurement_button`
- Root tag: `xpath`
- Field references: 3
- Sample fields: `quality_control_point_qty`, `quality_fail_qty`, `quality_pass_qty`
- Buttons: `action_see_quality_checks`, `action_see_quality_control_points`
- XPath or positional patches: 1

### `product_template_form_view_quality_control`
- Name: product.template.quality
- Model: `product.template`
- Type: inferred from arch
- Inherits: `stock.product_template_form_view_procurement_button`
- Root tag: `xpath`
- Field references: 3
- Sample fields: `quality_control_point_qty`, `quality_fail_qty`, `quality_pass_qty`
- Buttons: `action_see_quality_checks`, `action_see_quality_control_points`
- XPath or positional patches: 1

### `quality_check_view_search`
- Name: quality.check.view.search
- Model: `quality.check`
- Type: inferred from arch
- Root tag: `search`
- Field references: 4
- Sample fields: `lot_ids`, `picking_id`, `product_id`, `team_id`
- XPath or positional patches: 0

### `quality_check_view_pivot`
- Name: quality.check.view.pivot
- Model: `quality.check`
- Type: inferred from arch
- Root tag: `pivot`
- Field references: 2
- Sample fields: `control_date`, `product_id`
- XPath or positional patches: 0

### `quality_check_view_graph`
- Name: quality.check.view.graph
- Model: `quality.check`
- Type: inferred from arch
- Root tag: `graph`
- Field references: 2
- Sample fields: `control_date`, `quality_state`
- XPath or positional patches: 0

### `quality_check_view_tree`
- Name: quality.check.view.list
- Model: `quality.check`
- Type: inferred from arch
- Root tag: `list`
- Field references: 13
- Sample fields: `company_id`, `control_date`, `lot_ids`, `lot_name`, `measure_on`, `name`, `picking_id`, `point_id`, `product_id`, `quality_state`, and 3 more
- XPath or positional patches: 0

### `quality_check_view_kanban`
- Name: quality.check.view.kanban
- Model: `quality.check`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 5
- Sample fields: `lot_ids`, `name`, `product_id`, `quality_state`, `user_id`
- XPath or positional patches: 0

### `quality_check_view_form`
- Name: quality.check.view.form
- Model: `quality.check`
- Type: inferred from arch
- Root tag: `form`
- Field references: 31
- Sample fields: `additional_note`, `alert_count`, `alert_ids`, `company_id`, `control_date`, `failure_location_id`, `is_lot_tested_fractionally`, `lot_ids`, `lot_name`, `measure`, and 21 more
- Buttons: `action_open_spreadsheet`, `action_see_alerts`, `do_alert`, `do_fail`, `do_measure`, `do_pass`
- XPath or positional patches: 0

### `quality_alert_view_calendar`
- Name: quality.alert.view.calendar
- Model: `quality.alert`
- Type: inferred from arch
- Root tag: `calendar`
- Field references: 5
- Sample fields: `partner_id`, `product_id`, `reason_id`, `team_id`, `user_id`
- XPath or positional patches: 0

### `quality_alert_view_graph`
- Name: quality.alert.view.graph
- Model: `quality.alert`
- Type: inferred from arch
- Root tag: `graph`
- Field references: 2
- Sample fields: `reason_id`, `stage_id`
- XPath or positional patches: 0

### `quality_alert_view_pivot`
- Name: quality.alert.view.pivot
- Model: `quality.alert`
- Type: inferred from arch
- Root tag: `pivot`
- Field references: 2
- Sample fields: `stage_id`, `team_id`
- XPath or positional patches: 0

### `quality_alert_view_tree`
- Name: quality.alert.view.list.inherit.quality.control
- Model: `quality.alert`
- Type: inferred from arch
- Inherits: `quality.quality_alert_view_tree`
- Root tag: `field`
- Field references: 8
- Sample fields: `activity_exception_decoration`, `check_id`, `company_id`, `date_assign`, `description`, `partner_id`, `priority`, `user_id`
- XPath or positional patches: 0

### `quality_alert_view_form`
- Name: quality.alert.view.form
- Model: `quality.alert`
- Type: inferred from arch
- Root tag: `form`
- Field references: 21
- Sample fields: `action_corrective`, `action_preventive`, `check_id`, `company_id`, `date_assign`, `date_close`, `description`, `email_cc`, `lot_ids`, `name`, and 11 more
- Buttons: `action_see_check`
- XPath or positional patches: 0

### `quality_alert_view_kanban`
- Name: quality.alert.view.kanban
- Model: `quality.alert`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 6
- Sample fields: `activity_ids`, `display_name`, `priority`, `product_tmpl_id`, `tag_ids`, `user_id`
- XPath or positional patches: 0

### `quality_alert_view_search_inherit_quality_control`
- Name: quality.alert.view.search.inherit.quality.control
- Model: `quality.alert`
- Type: inferred from arch
- Inherits: `quality.quality_alert_view_search`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `title`
- XPath or positional patches: 1

## Actions

- `quality_point_action`: `act_window` Control Points
- `quality_alert_stage_action`: `act_window` Quality Alert Stages
- `quality_tag_action`: `act_window` Quality Tags
- `quality_spreadsheet_template_action_config`: `act_window` Quality Spreadsheet Templates
- `quality_alert_team_action_config`: `act_window` Quality Teams
- `quality_alert_team_action`: `act_window` Quality Overview
- `quality_check_action_report`: `act_window` Quality Check Analysis
- `quality_check_action_main`: `act_window` Quality Checks
- `quality_check_action_production_lot`: `act_window` Quality Checks
- `quality_check_action_picking`: `act_window` Quality Checks
- `quality_check_action_team`: `act_window` Quality Checks
- `quality_check_action_spc`: `act_window` Quality Checks SPC
- `quality_alert_action_report`: `act_window` Quality Alerts Analysis
- `quality_alert_action_check`: `act_window` Quality Alerts
- `quality_alert_action_team`: `act_window` Quality Alerts

## Menus

- `menu_quality_check_report`: unnamed
- `menu_quality_alert_report`: unnamed
- `menu_quality_reporting`: Reporting
- `menu_config_quality_spreadsheet_template`: Quality Spreadsheet Templates
- `menu_config_quality_tags`: Quality Tags
- `menu_quality_config_alert_stage`: Quality Alert Stages
- `menu_quality_config_alert_team`: Quality Teams
- `menu_quality_configuration`: Configuration
- `menu_quality_alert`: Quality Alerts
- `menu_quality_checks`: Quality Checks
- `menu_quality_control_points`: Control Points
- `menu_quality_control`: Quality Control
- `menu_quality_dashboard`: Overview
- `menu_quality_root`: Quality

## Navigation

- **Parent:** [[docs/Enterprise Addons/quality_control/Views]]

