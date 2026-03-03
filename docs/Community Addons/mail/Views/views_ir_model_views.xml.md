---
tags: [odoo, community, generated, views]
---

# views/ir_model_views.xml

- Module: [[docs/Community Addons/mail/mail|mail]]
- Scope: Community Addons
- Source file: `views/ir_model_views.xml`
- Views: 3
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `field_form_view`
- Name: unnamed
- Model: `ir.model.fields`
- Type: inferred from arch
- Inherits: `base.view_model_fields_form`
- Root tag: `field`
- Field references: 3
- Sample fields: `copied`, `state`, `tracking`
- XPath or positional patches: 0

### `model_search_view`
- Name: unnamed
- Model: `ir.model`
- Type: inferred from arch
- Inherits: `base.view_model_search`
- Root tag: `field`
- Field references: 1
- Sample fields: `model`
- XPath or positional patches: 0

### `model_form_view`
- Name: unnamed
- Model: `ir.model`
- Type: inferred from arch
- Inherits: `base.view_model_form`
- Root tag: `field`
- Field references: 6
- Sample fields: `is_mail_activity`, `is_mail_blacklist`, `is_mail_thread`, `state`, `tracking`, `transient`
- XPath or positional patches: 1

## Navigation

- **Parent:** [[docs/Community Addons/mail/Views]]

