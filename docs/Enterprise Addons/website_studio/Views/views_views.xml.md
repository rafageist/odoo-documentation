<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/views.xml

- Module: [[docs/Enterprise Addons/website_studio/website_studio|website_studio]]
- Scope: Enterprise Addons
- Source file: `views/views.xml`
- Views: 3
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `select_simple_ir_model`
- Name: select_simple_ir_model
- Model: `ir.model`
- Type: `list`
- Root tag: `list`
- Field references: 3
- Sample fields: `model`, `name`, `state`
- XPath or positional patches: 0

### `website_controller_page_form_dialog_new`
- Name: website_controller_page_form_dialog_new
- Model: `website.controller.page`
- Type: `form`
- Inherits: `website_studio.website_controller_page_form_dialog`
- Root tag: `xpath`
- Field references: 3
- Sample fields: `auto_single_page`, `model`, `use_menu`
- XPath or positional patches: 2

### `website_controller_page_form_dialog`
- Name: website_page_form
- Model: `website.controller.page`
- Type: `form`
- Root tag: `form`
- Field references: 8
- Sample fields: `is_published`, `model_id`, `name`, `name_slugified`, `record_domain`, `record_view_id`, `view_id`, `website_id`
- XPath or positional patches: 0

## Navigation

- **Parent:** [[docs/Enterprise Addons/website_studio/Views]]

<!-- GENERATED:VIEWFILE -->
