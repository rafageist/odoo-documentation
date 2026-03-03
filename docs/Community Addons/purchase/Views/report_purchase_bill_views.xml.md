---
tags: [odoo, community, generated, views]
---

# report/purchase_bill_views.xml

- Module: [[docs/Community Addons/purchase/purchase|purchase]]
- Scope: Community Addons
- Source file: `report/purchase_bill_views.xml`
- Views: 2
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `view_purchase_bill_union_tree`
- Name: purchase.bill.union.list
- Model: `purchase.bill.union`
- Type: inferred from arch
- Root tag: `list`
- Field references: 7
- Sample fields: `amount`, `company_id`, `currency_id`, `date`, `name`, `partner_id`, `reference`
- XPath or positional patches: 0

### `view_purchase_bill_union_filter`
- Name: purchase.bill.union.select
- Model: `purchase.bill.union`
- Type: inferred from arch
- Root tag: `search`
- Field references: 3
- Sample fields: `amount`, `name`, `partner_id`
- XPath or positional patches: 0

## Navigation

- **Parent:** [[docs/Community Addons/purchase/Views]]

