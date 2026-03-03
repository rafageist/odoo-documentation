---
tags: [odoo, community, generated, views]
---

# views/website_pages_views.xml

- Module: [[docs/Community Addons/website_hr_recruitment/website_hr_recruitment|website_hr_recruitment]]
- Scope: Community Addons
- Source file: `views/website_pages_views.xml`
- Views: 2
- Actions: 1
- Menus: 1
- Rules: 0

## View records

### `job_pages_kanban_view`
- Name: Job Pages Kanban
- Model: `hr.job`
- Type: inferred from arch
- Inherits: `hr_job_website_inherit`
- Root tag: `kanban`
- Field references: 0
- XPath or positional patches: 1

### `job_pages_tree_view`
- Name: Job Pages List
- Model: `hr.job`
- Type: inferred from arch
- Inherits: `hr.view_hr_job_tree`
- Root tag: `xpath`
- Field references: 6
- Sample fields: `company_id`, `is_published`, `is_seo_optimized`, `name`, `website_id`, `website_url`
- XPath or positional patches: 2

## Actions

- `action_job_pages_list`: `act_window` Job Pages

## Menus

- `menu_job_pages`: Jobs

## Navigation

- **Parent:** [[docs/Community Addons/website_hr_recruitment/Views]]

