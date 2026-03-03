---
tags: [odoo, community, generated, views]
---

# views/lunch_supplier_views.xml

- Module: [[docs/Community Addons/lunch/lunch|lunch]]
- Scope: Community Addons
- Source file: `views/lunch_supplier_views.xml`
- Views: 4
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `lunch_supplier_view_search`
- Name: lunch.supplier.view.search
- Model: `lunch.supplier`
- Type: inferred from arch
- Root tag: `search`
- Field references: 1
- Sample fields: `name`
- XPath or positional patches: 0

### `lunch_supplier_view_kanban`
- Name: lunch.supplier.view.kanban
- Model: `lunch.supplier`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 4
- Sample fields: `city`, `country_id`, `display_name`, `email`
- XPath or positional patches: 0

### `lunch_supplier_view_form`
- Name: lunch.supplier.view.form
- Model: `lunch.supplier`
- Type: inferred from arch
- Root tag: `form`
- Field references: 32
- Sample fields: `active`, `automatic_email_time`, `available_location_ids`, `city`, `company_id`, `country_id`, `currency_id`, `delivery`, `email`, `moment`, and 22 more
- XPath or positional patches: 0

### `lunch_supplier_view_tree`
- Name: lunch.supplier.view.list
- Model: `lunch.supplier`
- Type: inferred from arch
- Root tag: `list`
- Field references: 3
- Sample fields: `email`, `name`, `phone`
- XPath or positional patches: 0

## Actions

- `lunch_vendors_action`: `act_window` Vendors

## Navigation

- **Parent:** [[docs/Community Addons/lunch/Views]]

