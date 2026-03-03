---
tags: [odoo, community, generated, views]
---

# views/maintenance_views.xml

- Module: [[docs/Community Addons/maintenance/maintenance|maintenance]]
- Scope: Community Addons
- Source file: `views/maintenance_views.xml`
- Views: 24
- Actions: 12
- Menus: 15
- Rules: 0

## View records

### `maintenance_team_view_search`
- Name: maintenance.team.search
- Model: `maintenance.team`
- Type: inferred from arch
- Root tag: `search`
- Field references: 1
- Sample fields: `name`
- XPath or positional patches: 0

### `maintenance_team_kanban`
- Name: maintenance.team.kanban
- Model: `maintenance.team`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 7
- Sample fields: `color`, `name`, `todo_request_count`, `todo_request_count_block`, `todo_request_count_date`, `todo_request_count_high_priority`, `todo_request_count_unscheduled`
- Buttons: `%(hr_equipment_todo_request_action_from_dashboard)d`
- XPath or positional patches: 0

### `maintenance_team_view_kanban`
- Name: maintenance.team.kanban
- Model: `maintenance.team`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 1
- Sample fields: `name`
- XPath or positional patches: 0

### `maintenance_team_view_tree`
- Name: maintenance.team.list
- Model: `maintenance.team`
- Type: inferred from arch
- Root tag: `list`
- Field references: 3
- Sample fields: `company_id`, `member_ids`, `name`
- XPath or positional patches: 0

### `maintenance_team_view_form`
- Name: maintenance.team.form
- Model: `maintenance.team`
- Type: inferred from arch
- Root tag: `form`
- Field references: 7
- Sample fields: `active`, `alias_domain_id`, `alias_id`, `alias_name`, `company_id`, `member_ids`, `name`
- XPath or positional patches: 0

### `hr_equipment_stage_view_kanban`
- Name: equipment.stage.kanban
- Model: `maintenance.stage`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 1
- Sample fields: `name`
- XPath or positional patches: 0

### `hr_equipment_stage_view_tree`
- Name: equipment.stage.list
- Model: `maintenance.stage`
- Type: inferred from arch
- Root tag: `list`
- Field references: 4
- Sample fields: `done`, `fold`, `name`, `sequence`
- XPath or positional patches: 0

### `hr_equipment_stage_view_search`
- Name: equipment.stage.search
- Model: `maintenance.stage`
- Type: inferred from arch
- Root tag: `search`
- Field references: 1
- Sample fields: `name`
- XPath or positional patches: 0

### `view_maintenance_equipment_category_kanban`
- Name: maintenance.equipment.category.kanban
- Model: `maintenance.equipment.category`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 4
- Sample fields: `equipment_count`, `maintenance_open_count`, `name`, `technician_user_id`
- XPath or positional patches: 0

### `hr_equipment_category_view_search`
- Name: equipment.category.search
- Model: `maintenance.equipment.category`
- Type: inferred from arch
- Root tag: `search`
- Field references: 1
- Sample fields: `name`
- XPath or positional patches: 0

### `hr_equipment_category_view_tree`
- Name: equipment.category.list
- Model: `maintenance.equipment.category`
- Type: inferred from arch
- Root tag: `list`
- Field references: 3
- Sample fields: `company_id`, `name`, `technician_user_id`
- XPath or positional patches: 0

### `hr_equipment_category_view_form`
- Name: equipment.category.form
- Model: `maintenance.equipment.category`
- Type: inferred from arch
- Root tag: `form`
- Field references: 6
- Sample fields: `company_id`, `equipment_count`, `maintenance_open_count`, `name`, `note`, `technician_user_id`
- Buttons: `%(hr_equipment_action_from_category_form)d`, `%(hr_equipment_request_action_link)d`
- XPath or positional patches: 0

### `hr_equipment_view_search`
- Name: equipment.search
- Model: `maintenance.equipment`
- Type: inferred from arch
- Root tag: `search`
- Field references: 3
- Sample fields: `category_id`, `name`, `owner_user_id`
- XPath or positional patches: 0

### `hr_equipment_view_tree`
- Name: equipment.list
- Model: `maintenance.equipment`
- Type: inferred from arch
- Root tag: `list`
- Field references: 10
- Sample fields: `activity_exception_decoration`, `assign_date`, `category_id`, `company_id`, `message_needaction`, `name`, `owner_user_id`, `partner_id`, `serial_no`, `technician_user_id`
- XPath or positional patches: 0

### `hr_equipment_view_kanban`
- Name: equipment.kanban
- Model: `maintenance.equipment`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 7
- Sample fields: `activity_ids`, `color`, `maintenance_open_count`, `model`, `name`, `owner_user_id`, `serial_no`
- XPath or positional patches: 0

### `hr_equipment_view_form`
- Name: equipment.form
- Model: `maintenance.equipment`
- Type: inferred from arch
- Root tag: `form`
- Field references: 24
- Sample fields: `active`, `assign_date`, `category_id`, `company_id`, `cost`, `effective_date`, `equipment_properties`, `estimated_next_failure`, `expected_mtbf`, `latest_failure_date`, and 14 more
- Buttons: `%(hr_equipment_request_action_from_equipment)d`
- XPath or positional patches: 0

### `hr_equipment_view_calendar`
- Name: equipment.request.calendar
- Model: `maintenance.request`
- Type: inferred from arch
- Root tag: `calendar`
- Field references: 11
- Sample fields: `archive`, `done`, `duration`, `maintenance_type`, `priority`, `recurring_maintenance`, `repeat_interval`, `repeat_type`, `repeat_unit`, `repeat_until`, and 1 more
- XPath or positional patches: 0

### `hr_equipment_request_view_pivot`
- Name: equipment.request.pivot
- Model: `maintenance.request`
- Type: inferred from arch
- Root tag: `pivot`
- Field references: 3
- Sample fields: `color`, `stage_id`, `user_id`
- XPath or positional patches: 0

### `hr_equipment_request_view_graph`
- Name: equipment.request.graph
- Model: `maintenance.request`
- Type: inferred from arch
- Root tag: `graph`
- Field references: 5
- Sample fields: `color`, `duration`, `repeat_interval`, `stage_id`, `user_id`
- XPath or positional patches: 0

### `hr_equipment_request_view_tree`
- Name: equipment.request.list
- Model: `maintenance.request`
- Type: inferred from arch
- Root tag: `list`
- Field references: 9
- Sample fields: `activity_exception_decoration`, `category_id`, `company_id`, `message_needaction`, `name`, `owner_user_id`, `request_date`, `stage_id`, `user_id`
- XPath or positional patches: 0

### `hr_equipment_request_view_kanban`
- Name: equipment.request.kanban
- Model: `maintenance.request`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 11
- Sample fields: `activity_ids`, `archive`, `category_id`, `color`, `equipment_id`, `kanban_state`, `name`, `owner_user_id`, `priority`, `schedule_date`, and 1 more
- XPath or positional patches: 0

### `hr_equipment_request_view_form`
- Name: equipment.request.form
- Model: `maintenance.request`
- Type: inferred from arch
- Root tag: `form`
- Field references: 28
- Sample fields: `archive`, `category_id`, `close_date`, `company_id`, `description`, `done`, `email_cc`, `equipment_id`, `instruction_google_slide`, `instruction_pdf`, and 18 more
- Buttons: `archive_equipment_request`, `reset_equipment_request`
- XPath or positional patches: 0

### `maintenance_request_view_activity`
- Name: maintenance.request.view.activity
- Model: `maintenance.request`
- Type: inferred from arch
- Root tag: `activity`
- Field references: 3
- Sample fields: `equipment_id`, `name`, `user_id`
- XPath or positional patches: 0

### `hr_equipment_request_view_search`
- Name: equipment.request.search
- Model: `maintenance.request`
- Type: inferred from arch
- Root tag: `search`
- Field references: 7
- Sample fields: `category_id`, `equipment_id`, `maintenance_team_id`, `name`, `owner_user_id`, `stage_id`, `user_id`
- XPath or positional patches: 0

## Actions

- `maintenance_dashboard_action`: `act_window` Maintenance Teams
- `maintenance_team_action_settings`: `act_window` Teams
- `hr_equipment_stage_action`: `act_window` Stages
- `hr_equipment_category_action`: `act_window` Equipment Categories
- `hr_equipment_action_from_category_form`: `act_window` Equipment
- `hr_equipment_action`: `act_window` Equipment
- `maintenance_request_action_reports`: `act_window` Maintenance Requests Analysis
- `hr_equipment_request_action_cal`: `act_window` Maintenance Requests
- `hr_equipment_todo_request_action_from_dashboard`: `act_window` Maintenance Requests
- `hr_equipment_request_action_from_equipment`: `act_window` Maintenance Requests
- `hr_equipment_request_action_link`: `act_window` Maintenance Requests
- `hr_equipment_request_action`: `act_window` Maintenance Requests

## Menus

- `menu_maintenance_stage_configuration`: Maintenance Stages
- `menu_maintenance_cat`: Equipment Categories
- `menu_maintenance_teams`: Maintenance Teams
- `menu_maintenance_configuration`: Configuration
- `maintenance_request_reporting`: unnamed
- `maintenance_reporting`: Reporting
- `menu_m_reports_losses`: Losses Analysis
- `menu_m_reports_oee`: Overall Equipment Effectiveness (OEE)
- `menu_m_reports`: Reporting
- `menu_equipment_form`: Equipment
- `menu_m_request_calendar`: Maintenance Calendar
- `menu_m_request_form`: Maintenance Requests
- `menu_m_request`: Maintenance
- `menu_m_dashboard`: Dashboard
- `menu_maintenance_title`: Maintenance

## Navigation

- **Parent:** [[docs/Community Addons/maintenance/Views]]

