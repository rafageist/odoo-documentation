<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/hr_employee_views.xml

- Module: [[docs/Community Addons/hr/hr|hr]]
- Scope: Community Addons
- Source file: `views/hr_employee_views.xml`
- Views: 10
- Actions: 12
- Menus: 0
- Rules: 0

## View records

### `hr_employee_view_activity`
- Name: hr.employee.activity
- Model: `hr.employee`
- Type: inferred from arch
- Root tag: `activity`
- Field references: 3
- Sample fields: `id`, `job_id`, `name`
- XPath or positional patches: 0

### `view_employee_form_smartbutton_inherited`
- Name: view.employee.form.smartbutton.inherited
- Model: `hr.employee`
- Type: inferred from arch
- Inherits: `view_employee_form`
- Root tag: `button`
- Field references: 1
- Sample fields: `related_partners_count`
- Buttons: `action_open_versions`, `action_related_contacts`
- XPath or positional patches: 0

### `hr_kanban_view_employees`
- Name: hr.employee.kanban
- Model: `hr.employee`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 17
- Sample fields: `activity_ids`, `avatar_128`, `birthday_public_display_string`, `category_ids`, `company_id`, `contract_date_end`, `contract_date_start`, `employee_properties`, `hr_icon_display`, `image_1024`, and 7 more
- XPath or positional patches: 0

### `hr_employee_list_activites_view`
- Name: hr.employee.list.activites.view
- Model: `hr.employee`
- Type: inferred from arch
- Root tag: `list`
- Field references: 26
- Sample fields: `active`, `activity_date_deadline`, `activity_ids`, `activity_user_id`, `address_id`, `avatar_128`, `birthday`, `category_ids`, `coach_id`, `company_id`, and 16 more
- XPath or positional patches: 0

### `hr_employee_list_view`
- Name: hr.employee.list
- Model: `hr.employee`
- Type: inferred from arch
- Root tag: `list`
- Field references: 7
- Sample fields: `company_id`, `contract_date_start`, `department_id`, `job_id`, `name`, `parent_id`, `resource_calendar_id`
- XPath or positional patches: 0

### `view_employee_tree`
- Name: hr.employee.list
- Model: `hr.employee`
- Type: inferred from arch
- Root tag: `list`
- Field references: 27
- Sample fields: `active`, `activity_date_deadline`, `activity_ids`, `activity_user_id`, `address_id`, `avatar_128`, `birthday`, `category_ids`, `coach_id`, `company_id`, and 17 more
- Buttons: `%(plan_wizard_action)d`
- XPath or positional patches: 0

### `hr_employee_view_pivot`
- Name: hr.employee.view.pivot
- Model: `hr.employee`
- Type: inferred from arch
- Root tag: `pivot`
- Field references: 7
- Sample fields: `children`, `color`, `contract_date_start`, `distance_home_work`, `id`, `job_id`, `km_home_work`
- XPath or positional patches: 0

### `hr_employee_view_graph`
- Name: hr.employee.view.graph
- Model: `hr.employee`
- Type: inferred from arch
- Root tag: `graph`
- Field references: 6
- Sample fields: `children`, `color`, `contract_date_start`, `distance_home_work`, `id`, `km_home_work`
- XPath or positional patches: 0

### `view_employee_form`
- Name: hr.employee.form
- Model: `hr.employee`
- Type: inferred from arch
- Root tag: `form`
- Field references: 72
- Sample fields: `additional_note`, `address_id`, `bank_account_ids`, `barcode`, `birthday`, `birthday_public_display`, `category_ids`, `certificate`, `children`, `company_id`, and 62 more
- Buttons: `%(hr_employee_print_badge)d`, `%(hr_version_wizard_action)d`, `%(plan_wizard_action)d`, `action_create_user`, `action_open_allocation_wizard`, `action_open_versions`, `action_toggle_primary_bank_account_trust`, `generate_random_barcode`
- XPath or positional patches: 0

### `view_employee_filter`
- Name: hr.employee.search
- Model: `hr.employee`
- Type: inferred from arch
- Root tag: `search`
- Field references: 10
- Sample fields: `category_ids`, `coach_id`, `company_id`, `contract_date_start`, `department_id`, `job_id`, `name`, `parent_id`, `private_car_plate`, `resource_calendar_id`
- XPath or positional patches: 0

## Actions

- `action_hr_employee_create_users`: `server` Create User
- `action_hr_employee_create_users_confirmation`: `server` Create User
- `action_hr_employee_all_activities`: `act_window` All activities
- `open_view_employee_list`: `act_window` Employees
- `act_hr_employee_pivot_view`: `view`
- `act_hr_employee_graph_view`: `view`
- `act_hr_employee_activity_view`: `view`
- `act_hr_employee_form_view`: `view`
- `act_hr_employee_tree_view`: `view`
- `act_hr_employee_kanban_view`: `view`
- `open_view_employee_list_my`: `act_window` Employees
- `action_hr_employee_load_demo_data`: `server` Load Sample Data

## Navigation

- **Parent:** [[docs/Community Addons/hr/Views]]

<!-- GENERATED:VIEWFILE -->
