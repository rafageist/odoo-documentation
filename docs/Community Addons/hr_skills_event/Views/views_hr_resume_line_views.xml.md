<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/hr_resume_line_views.xml

- Module: [[docs/Community Addons/hr_skills_event/hr_skills_event|hr_skills_event]]
- Scope: Community Addons
- Source file: `views/hr_resume_line_views.xml`
- Views: 3
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `resume_slides_line_view_kanban`
- Name: hr.resume.line.kanban.view.inherited
- Model: `hr.resume.line`
- Type: inferred from arch
- Inherits: `hr_skills.hr_resume_line_kanban_view`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

### `resume_slides_line_view_list`
- Name: hr.resume.line.list
- Model: `hr.resume.line`
- Type: inferred from arch
- Inherits: `hr_skills.hr_resume_line_list_view`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `event_id`
- XPath or positional patches: 3

### `resume_slides_line_view_form`
- Name: hr.resume.line.form
- Model: `hr.resume.line`
- Type: inferred from arch
- Inherits: `hr_skills.resume_line_view_form`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `event_id`
- XPath or positional patches: 4

## Navigation

- **Parent:** [[docs/Community Addons/hr_skills_event/Views]]

<!-- GENERATED:VIEWFILE -->
