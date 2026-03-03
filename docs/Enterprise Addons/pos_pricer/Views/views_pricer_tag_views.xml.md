---
tags: [odoo, enterprise, generated, views]
---

# views/pricer_tag_views.xml

- Module: [[docs/Enterprise Addons/pos_pricer/pos_pricer|pos_pricer]]
- Scope: Enterprise Addons
- Source file: `views/pricer_tag_views.xml`
- Views: 2
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `pricer_pricer_tag_form_view`
- Name: pricer_tag.form
- Model: `pricer.tag`
- Type: inferred from arch
- Root tag: `form`
- Field references: 1
- Sample fields: `name`
- XPath or positional patches: 0

### `pricer_pricer_tag_view_list`
- Name: pricer_tag.list
- Model: `pricer.tag`
- Type: inferred from arch
- Root tag: `list`
- Field references: 3
- Sample fields: `name`, `pricer_store_id`, `product_id`
- XPath or positional patches: 0

## Actions

- `action_open_pricer_tags`: `act_window` Pricer Tags

## Navigation

- **Parent:** [[docs/Enterprise Addons/pos_pricer/Views]]

