---
tags: [odoo, community, generated, views]
---

# views/lunch_product_views.xml

- Module: [[docs/Community Addons/lunch/lunch|lunch]]
- Scope: Community Addons
- Source file: `views/lunch_product_views.xml`
- Views: 10
- Actions: 4
- Menus: 0
- Rules: 0

## View records

### `lunch_product_category_view_search`
- Name: lunch.product.category.search
- Model: `lunch.product.category`
- Type: inferred from arch
- Root tag: `search`
- Field references: 1
- Sample fields: `name`
- XPath or positional patches: 0

### `lunch_product_category_view_kanban`
- Name: Product category Kanban
- Model: `lunch.product.category`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 4
- Sample fields: `company_id`, `image_128`, `name`, `product_count`
- Buttons: `%(lunch.lunch_product_action_statbutton)d`
- XPath or positional patches: 0

### `lunch_product_category_view_form`
- Name: Product category Form
- Model: `lunch.product.category`
- Type: inferred from arch
- Root tag: `form`
- Field references: 4
- Sample fields: `company_id`, `image_1920`, `name`, `product_count`
- Buttons: `%(lunch.lunch_product_action_statbutton)d`
- XPath or positional patches: 0

### `lunch_product_category_view_tree`
- Name: Product category List
- Model: `lunch.product.category`
- Type: inferred from arch
- Root tag: `list`
- Field references: 2
- Sample fields: `company_id`, `name`
- XPath or positional patches: 0

### `view_lunch_product_kanban`
- Name: lunch.product.kanban
- Model: `lunch.product`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 8
- Sample fields: `category_id`, `currency_id`, `description`, `id`, `image_128`, `name`, `price`, `supplier_id`
- XPath or positional patches: 0

### `view_lunch_product_kanban_order`
- Name: lunch.product.kanban
- Model: `lunch.product`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 8
- Sample fields: `currency_id`, `description`, `image_128`, `is_favorite`, `is_new`, `name`, `price`, `supplier_id`
- XPath or positional patches: 0

### `lunch_product_view_form`
- Name: lunch.product.form
- Model: `lunch.product`
- Type: inferred from arch
- Root tag: `form`
- Field references: 10
- Sample fields: `active`, `category_id`, `company_id`, `currency_id`, `description`, `image_1920`, `name`, `new_until`, `price`, `supplier_id`
- XPath or positional patches: 0

### `lunch_product_view_tree_order`
- Name: lunch.product.list.order
- Model: `lunch.product`
- Type: inferred from arch
- Inherits: `lunch_product_view_tree`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

### `lunch_product_view_tree`
- Name: lunch.product.list
- Model: `lunch.product`
- Type: inferred from arch
- Root tag: `list`
- Field references: 7
- Sample fields: `category_id`, `company_id`, `currency_id`, `description`, `name`, `price`, `supplier_id`
- XPath or positional patches: 0

### `lunch_product_view_search`
- Name: lunch.product.search
- Model: `lunch.product`
- Type: inferred from arch
- Root tag: `search`
- Field references: 4
- Sample fields: `category_id`, `description`, `name`, `supplier_id`
- XPath or positional patches: 0

## Actions

- `lunch_product_category_action`: `act_window` Product Categories
- `lunch_product_action_order`: `act_window` Order Your Lunch
- `lunch_product_action`: `act_window` Products
- `lunch_product_action_statbutton`: `act_window` Products

## Navigation

- **Parent:** [[docs/Community Addons/lunch/Views]]

