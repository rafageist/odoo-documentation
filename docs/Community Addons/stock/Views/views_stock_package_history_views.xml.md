---
tags: [odoo, community, generated, views]
---

# views/stock_package_history_views.xml

- Module: [[docs/Community Addons/stock/stock|stock]]
- Scope: Community Addons
- Source file: `views/stock_package_history_views.xml`
- Views: 2
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `view_stock_package_history_list`
- Name: stock.package.history.list
- Model: `stock.package.history`
- Type: inferred from arch
- Root tag: `list`
- Field references: 7
- Sample fields: `company_id`, `location_dest_id`, `location_id`, `package_name`, `package_type_id`, `parent_dest_id`, `parent_orig_id`
- XPath or positional patches: 0

### `package_history_search_view`
- Name: stock.package.history.search
- Model: `stock.package.history`
- Type: inferred from arch
- Root tag: `search`
- Field references: 3
- Sample fields: `location_id`, `package_name`, `package_type_id`
- XPath or positional patches: 0

## Navigation

- **Parent:** [[docs/Community Addons/stock/Views]]

