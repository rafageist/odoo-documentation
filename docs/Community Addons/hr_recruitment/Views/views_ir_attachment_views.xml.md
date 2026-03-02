<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/ir_attachment_views.xml

- Module: [[docs/Community Addons/hr_recruitment/hr_recruitment|hr_recruitment]]
- Scope: Community Addons
- Source file: `views/ir_attachment_views.xml`
- Views: 2
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `ir_attachment_hr_recruitment_list_view`
- Name: unnamed
- Model: `ir.attachment`
- Type: inferred from arch
- Root tag: `list`
- Field references: 6
- Sample fields: `create_date`, `datas`, `name`, `res_id`, `res_model`, `res_name`
- XPath or positional patches: 0

### `ir_attachment_view_search_inherit_hr_recruitment`
- Name: ir.attachment.search.inherit.recruitment
- Model: `ir.attachment`
- Type: inferred from arch
- Inherits: `base.view_attachment_search`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `index_content`
- XPath or positional patches: 4

## Navigation

- **Parent:** [[docs/Community Addons/hr_recruitment/Views]]

<!-- GENERATED:VIEWFILE -->
