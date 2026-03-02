<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/product_product_views.xml

- Module: [[docs/Community Addons/hr_expense/hr_expense|hr_expense]]
- Scope: Community Addons
- Source file: `views/product_product_views.xml`
- Views: 6
- Actions: 4
- Menus: 0
- Rules: 0

## View records

### `product_product_expense_categories_tree_view`
- Name: product.product.expense.categories.list.view
- Model: `product.product`
- Type: inferred from arch
- Root tag: `list`
- Field references: 7
- Sample fields: `currency_id`, `default_code`, `description`, `lst_price`, `name`, `standard_price`, `supplier_taxes_id`
- XPath or positional patches: 0

### `product_product_expense_tree_view`
- Name: product.product.expense.list
- Model: `product.product`
- Type: inferred from arch
- Root tag: `list`
- Field references: 6
- Sample fields: `barcode`, `default_code`, `name`, `product_template_attribute_value_ids`, `standard_price`, `uom_id`
- XPath or positional patches: 0

### `product_product_expense_kanban_view`
- Name: product.product.kanban.expense
- Model: `product.product`
- Type: inferred from arch
- Inherits: `product.product_kanban_view`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `standard_price`
- XPath or positional patches: 1

### `product_product_expense_form_view`
- Name: product.product.expense.form
- Model: `product.product`
- Type: inferred from arch
- Root tag: `form`
- Field references: 16
- Sample fields: `active`, `categ_id`, `company_id`, `currency_id`, `default_code`, `description`, `id`, `image_1920`, `name`, `product_variant_count`, and 6 more
- XPath or positional patches: 0

### `product_template_search_view_inherit_hr_expense`
- Name: product.template.search.view.inherit.hr_expense
- Model: `product.template`
- Type: inferred from arch
- Inherits: `product.product_template_search_view`
- Root tag: `filter`
- Field references: 0
- XPath or positional patches: 1

### `view_product_hr_expense_form`
- Name: product.template.expense.form
- Model: `product.template`
- Type: inferred from arch
- Inherits: `product.product_template_form_view`
- Root tag: `span`
- Field references: 1
- Sample fields: `can_be_expensed`
- XPath or positional patches: 1

## Actions

- `hr_expense_product_form`: `view`
- `hr_expense_product_kanban`: `view`
- `hr_expense_product_tree`: `view`
- `hr_expense_product`: `act_window` Expense Categories

## Navigation

- **Parent:** [[docs/Community Addons/hr_expense/Views]]

<!-- GENERATED:VIEWFILE -->
