<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/hr_talent_pool_views.xml

- Module: [[docs/Community Addons/hr_recruitment/hr_recruitment|hr_recruitment]]
- Scope: Community Addons
- Source file: `views/hr_talent_pool_views.xml`
- Views: 3
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `hr_talent_pool_view_kanban`
- Name: hr.talent.pool.view.kanban
- Model: `hr.talent.pool`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 5
- Sample fields: `color`, `company_id`, `name`, `no_of_talents`, `pool_manager`
- Buttons: `action_talent_pool_add_talents`
- XPath or positional patches: 0

### `hr_talent_pool_view_list`
- Name: hr.talent.pool.view.list
- Model: `hr.talent.pool`
- Type: inferred from arch
- Root tag: `list`
- Field references: 5
- Sample fields: `categ_ids`, `company_id`, `name`, `no_of_talents`, `pool_manager`
- XPath or positional patches: 0

### `hr_talent_pool_view_form`
- Name: hr.talent.pool.view.form
- Model: `hr.talent.pool`
- Type: inferred from arch
- Root tag: `form`
- Field references: 6
- Sample fields: `categ_ids`, `color`, `company_id`, `description`, `name`, `pool_manager`
- XPath or positional patches: 0

## Actions

- `action_hr_talent_pool`: `act_window` Talent Pool

## Navigation

- **Parent:** [[docs/Community Addons/hr_recruitment/Views]]

<!-- GENERATED:VIEWFILE -->
