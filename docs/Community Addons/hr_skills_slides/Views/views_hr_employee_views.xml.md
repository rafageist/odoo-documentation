<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/hr_employee_views.xml

- Module: [[docs/Community Addons/hr_skills_slides/hr_skills_slides|hr_skills_slides]]
- Scope: Community Addons
- Source file: `views/hr_employee_views.xml`
- Views: 3
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `hr_employee_resume_view_form_inherit`
- Name: hr.employee.view.form.inherit.resume.slides
- Model: `hr.employee`
- Type: inferred from arch
- Inherits: `hr_skills.hr_employee_view_form`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `course_url`
- XPath or positional patches: 1

### `hr_employee_public_resume_view_form_inherit`
- Name: hr.employee.view.form.inherit.resume.slides
- Model: `hr.employee.public`
- Type: inferred from arch
- Inherits: `hr_skills.hr_employee_public_view_form_inherit`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `course_url`
- XPath or positional patches: 1

### `hr_employee_view_form`
- Name: hr.employee.view.form.inherit.resume.slides
- Model: `hr.employee`
- Type: inferred from arch
- Inherits: `hr.view_employee_form`
- Root tag: `button`
- Field references: 2
- Sample fields: `courses_completion_text`, `has_subscribed_courses`
- Buttons: `action_open_courses`, `action_open_versions`
- XPath or positional patches: 0

## Navigation

- **Parent:** [[docs/Community Addons/hr_skills_slides/Views]]

<!-- GENERATED:VIEWFILE -->
