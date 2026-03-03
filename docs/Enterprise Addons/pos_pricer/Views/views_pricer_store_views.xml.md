---
tags: [odoo, enterprise, generated, views]
---

# views/pricer_store_views.xml

- Module: [[docs/Enterprise Addons/pos_pricer/pos_pricer|pos_pricer]]
- Scope: Enterprise Addons
- Source file: `views/pricer_store_views.xml`
- Views: 2
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `pricer_pricer_store_form_view`
- Name: pricer_store.form
- Model: `pricer.store`
- Type: inferred from arch
- Root tag: `form`
- Field references: 8
- Sample fields: `dummy_prod_barcode`, `dummy_tag_barcode`, `name`, `pricer_login`, `pricer_password`, `pricer_store_identifier`, `pricer_tag_ids`, `pricer_tenant_name`
- XPath or positional patches: 0

### `pricer_pricer_store_view_list`
- Name: pricer_store.list
- Model: `pricer.store`
- Type: inferred from arch
- Root tag: `list`
- Field references: 8
- Sample fields: `last_update_datetime`, `last_update_status_message`, `name`, `pricer_login`, `pricer_password`, `pricer_store_identifier`, `pricer_tag_ids`, `pricer_tenant_name`
- Buttons: `action_button_update_pricer_tags`
- XPath or positional patches: 0

## Actions

- `action_open_pricer_stores`: `act_window` Pricer Stores

## Navigation

- **Parent:** [[docs/Enterprise Addons/pos_pricer/Views]]

