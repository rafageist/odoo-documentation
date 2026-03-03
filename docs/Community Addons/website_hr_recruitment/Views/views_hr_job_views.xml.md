---
tags: [odoo, community, generated, views]
---

# views/hr_job_views.xml

- Module: [[docs/Community Addons/website_hr_recruitment/website_hr_recruitment|website_hr_recruitment]]
- Scope: Community Addons
- Source file: `views/hr_job_views.xml`
- Views: 4
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `hr_job_search_view_inherit`
- Name: unnamed
- Model: `hr.job`
- Type: inferred from arch
- Inherits: `hr.view_job_filter`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 2

### `view_hr_job_kanban_referal_extends`
- Name: hr.job.view.kanban
- Model: `hr.job`
- Type: inferred from arch
- Inherits: `hr_recruitment.view_hr_job_kanban`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `full_url`
- XPath or positional patches: 1

### `hr_job_form_inherit`
- Name: hr.job.form.inherit
- Model: `hr.job`
- Type: inferred from arch
- Inherits: `hr.view_hr_job_form`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `job_details`
- XPath or positional patches: 1

### `hr_job_website_inherit`
- Name: hr.job.kanban.inherit
- Model: `hr.job`
- Type: inferred from arch
- Inherits: `hr_recruitment.view_hr_job_kanban`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `website_published`
- XPath or positional patches: 3

## Navigation

- **Parent:** [[docs/Community Addons/website_hr_recruitment/Views]]

