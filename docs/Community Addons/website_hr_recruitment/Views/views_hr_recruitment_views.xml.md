---
tags: [odoo, community, generated, views]
---

# views/hr_recruitment_views.xml

- Module: [[docs/Community Addons/website_hr_recruitment/website_hr_recruitment|website_hr_recruitment]]
- Scope: Community Addons
- Source file: `views/hr_recruitment_views.xml`
- Views: 4
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `view_hr_job_tree_inherit_website`
- Name: hr.job.list
- Model: `hr.job`
- Type: inferred from arch
- Inherits: `hr_recruitment.hr_job_view_tree_inherit`
- Root tag: `field`
- Field references: 3
- Sample fields: `is_published`, `no_of_employee`, `website_id`
- XPath or positional patches: 1

### `view_hr_job_form_inherit_website`
- Name: hr.job.form
- Model: `hr.job`
- Type: inferred from arch
- Inherits: `hr.view_hr_job_form`
- Root tag: `field`
- Field references: 1
- Sample fields: `description`
- XPath or positional patches: 0

### `view_hr_job_form_website_published_button`
- Name: hr.job.form.inherit.published.button
- Model: `hr.job`
- Type: inferred from arch
- Inherits: `hr_recruitment.hr_job_survey`
- Root tag: `div`
- Field references: 3
- Sample fields: `is_published`, `website_id`, `website_published`
- XPath or positional patches: 3

### `view_hr_recruitment_tree_url`
- Name: hr.recruitment.list.inherit.url
- Model: `hr.recruitment.source`
- Type: inferred from arch
- Inherits: `hr_recruitment.hr_recruitment_source_tree`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `url`
- XPath or positional patches: 1

## Navigation

- **Parent:** [[docs/Community Addons/website_hr_recruitment/Views]]

