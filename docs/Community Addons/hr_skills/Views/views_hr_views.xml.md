<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/hr_views.xml

- Module: [[docs/Community Addons/hr_skills/hr_skills|hr_skills]]
- Scope: Community Addons
- Source file: `views/hr_views.xml`
- Views: 23
- Actions: 4
- Menus: 7
- Rules: 0

## View records

### `hr_employee_skill_view_search`
- Name: hr.employee.skill.view.search
- Model: `hr.employee.skill`
- Type: inferred from arch
- Root tag: `search`
- Field references: 2
- Sample fields: `employee_id`, `skill_id`
- XPath or positional patches: 0

### `hr_employee_skill_view_list`
- Name: hr.employees.skill.list
- Model: `hr.employee.skill`
- Type: inferred from arch
- Root tag: `list`
- Field references: 6
- Sample fields: `employee_id`, `skill_id`, `skill_level_id`, `skill_type_id`, `valid_from`, `valid_to`
- Buttons: `open_hr_employee_skill_modal`
- XPath or positional patches: 0

### `hr_employee_skill_type_view_form`
- Name: hr.skill.type.form
- Model: `hr.skill.type`
- Type: inferred from arch
- Root tag: `form`
- Field references: 8
- Sample fields: `active`, `color`, `id`, `is_certification`, `name`, `sequence`, `skill_ids`, `skill_level_ids`
- XPath or positional patches: 0

### `hr_skill_type_view_tree`
- Name: hr.skill.type.list
- Model: `hr.skill.type`
- Type: inferred from arch
- Root tag: `list`
- Field references: 5
- Sample fields: `color`, `display_name`, `sequence`, `skill_ids`, `skill_level_ids`
- XPath or positional patches: 0

### `hr_skill_type_view_search`
- Name: hr.skill.type.search
- Model: `hr.skill.type`
- Type: inferred from arch
- Root tag: `search`
- Field references: 4
- Sample fields: `active`, `name`, `skill_ids`, `skill_level_ids`
- XPath or positional patches: 0

### `hr_skill_view_search`
- Name: hr.skill.view.search
- Model: `hr.skill`
- Type: inferred from arch
- Root tag: `search`
- Field references: 2
- Sample fields: `name`, `skill_type_id`
- XPath or positional patches: 0

### `hr_skill_view_form`
- Name: hr.skill.form
- Model: `hr.skill`
- Type: inferred from arch
- Root tag: `form`
- Field references: 2
- Sample fields: `name`, `skill_type_id`
- XPath or positional patches: 0

### `employee_skill_view_inherit_certificate_form`
- Name: hr.employees.skill.inherit.certificate.form
- Model: `hr.employee.skill`
- Type: inferred from arch
- Inherits: `employee_skill_view_form`
- Root tag: `field`
- Field references: 1
- Sample fields: `skill_type_id`
- XPath or positional patches: 0

### `employee_skill_view_form`
- Name: hr.employees.skill.form
- Model: `hr.employee.skill`
- Type: inferred from arch
- Root tag: `form`
- Field references: 6
- Sample fields: `employee_id`, `skill_id`, `skill_level_id`, `skill_type_id`, `valid_from`, `valid_to`
- XPath or positional patches: 0

### `employee_skill_level_view_form`
- Name: hr.skill.level.form
- Model: `hr.skill.level`
- Type: inferred from arch
- Root tag: `form`
- Field references: 2
- Sample fields: `level_progress`, `name`
- XPath or positional patches: 0

### `employee_skill_view_tree`
- Name: hr.skill.list
- Model: `hr.skill`
- Type: inferred from arch
- Root tag: `list`
- Field references: 2
- Sample fields: `name`, `skill_type_id`
- XPath or positional patches: 0

### `employee_skill_level_view_tree`
- Name: hr.skill.level.list
- Model: `hr.skill.level`
- Type: inferred from arch
- Root tag: `list`
- Field references: 4
- Sample fields: `default_level`, `level_progress`, `name`, `technical_is_new_default`
- XPath or positional patches: 0

### `view_resume_lines_filter`
- Name: hr.resume.line.search
- Model: `hr.resume.line`
- Type: inferred from arch
- Root tag: `search`
- Field references: 2
- Sample fields: `company_id`, `department_id`
- XPath or positional patches: 0

### `hr_resume_line_calendar_view`
- Name: hr.resume.line.calendar.view
- Model: `hr.resume.line`
- Type: inferred from arch
- Root tag: `calendar`
- Field references: 1
- Sample fields: `course_type`
- XPath or positional patches: 0

### `hr_resume_line_kanban_view`
- Name: hr.resume.line.kanban.view
- Model: `hr.resume.line`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 4
- Sample fields: `course_type`, `date_start`, `employee_id`, `name`
- XPath or positional patches: 0

### `hr_resume_line_list_view`
- Name: hr.resume.line.list.view
- Model: `hr.resume.line`
- Type: inferred from arch
- Root tag: `list`
- Field references: 11
- Sample fields: `certificate_file`, `certificate_filename`, `course_type`, `date_start`, `description`, `duration`, `employee_id`, `external_url`, `line_type_id`, `name`, and 1 more
- XPath or positional patches: 0

### `hr_resume_line_type_tree_view`
- Name: hr.resume.line.type.list.view
- Model: `hr.resume.line.type`
- Type: inferred from arch
- Root tag: `list`
- Field references: 3
- Sample fields: `is_course`, `name`, `sequence`
- XPath or positional patches: 0

### `hr_employee_public_view_form_inherit`
- Name: hr.employee.public.view.form.inherit.resume
- Model: `hr.employee.public`
- Type: inferred from arch
- Inherits: `hr.hr_employee_public_view_form`
- Root tag: `page`
- Field references: 18
- Sample fields: `certification_ids`, `current_employee_skill_ids`, `date_end`, `date_start`, `description`, `duration`, `employee_id`, `external_url`, `is_course`, `level_progress`, and 8 more
- XPath or positional patches: 2

### `hr_employee_view_form`
- Name: hr.employee.view.form.inherit.resume
- Model: `hr.employee`
- Type: inferred from arch
- Inherits: `hr.view_employee_form`
- Root tag: `div`
- Field references: 19
- Sample fields: `certification_ids`, `current_employee_skill_ids`, `date_end`, `date_start`, `description`, `duration`, `employee_id`, `external_url`, `is_certification`, `is_course`, and 9 more
- XPath or positional patches: 3

### `resume_line_view_form_inherit`
- Name: hr.resume.line.inherit.form
- Model: `hr.resume.line`
- Type: inferred from arch
- Inherits: `hr_skills.resume_line_view_form`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `employee_id`
- XPath or positional patches: 2

### `resume_line_view_form`
- Name: hr.resume.line.form
- Model: `hr.resume.line`
- Type: inferred from arch
- Root tag: `form`
- Field references: 11
- Sample fields: `certificate_file`, `certificate_filename`, `course_type`, `date_end`, `date_start`, `description`, `duration`, `external_url`, `line_type_id`, `name`, and 1 more
- XPath or positional patches: 0

### `hr_employee_public_view_search`
- Name: hr.employee.public.skill.search
- Model: `hr.employee.public`
- Type: inferred from arch
- Inherits: `hr.hr_employee_public_view_search`
- Root tag: `xpath`
- Field references: 2
- Sample fields: `employee_skill_ids`, `resume_line_ids`
- XPath or positional patches: 1

### `hr_employee_view_search`
- Name: hr.employee.skill.search
- Model: `hr.employee`
- Type: inferred from arch
- Inherits: `hr.view_employee_filter`
- Root tag: `xpath`
- Field references: 2
- Sample fields: `employee_skill_ids`, `resume_line_ids`
- XPath or positional patches: 1

## Actions

- `action_hr_employee_skill_certification`: `act_window` Certifications
- `hr_skill_type_action`: `act_window` Skill Types
- `hr_resume_lines_training_action`: `act_window` Training Attendances
- `hr_resume_type_action`: `act_window` Resume Sections

## Menus

- `menu_learnings_training_attendances`: Training Attendances
- `hr_certification_menu`: Certifications
- `hr_skill_learning_menu`: Learning
- `hr_employee_skill_report_menu`: Skills
- `hr_skill_type_menu`: Skill Types
- `hr_resume_line_type_menu`: Sections
- `menu_human_resources_configuration_resume`: Resume

## Navigation

- **Parent:** [[docs/Community Addons/hr_skills/Views]]

<!-- GENERATED:VIEWFILE -->
