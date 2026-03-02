<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/pos_order_view.xml

- Module: [[docs/Enterprise Addons/l10n_at_pos/l10n_at_pos|l10n_at_pos]]
- Scope: Enterprise Addons
- Source file: `views/pos_order_view.xml`
- Views: 2
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `view_pos_order_tree_l10n_at_inherit`
- Name: pos.order.list.austria.inherit
- Model: `pos.order`
- Type: inferred from arch
- Inherits: `point_of_sale.view_pos_order_tree`
- Root tag: `xpath`
- Field references: 2
- Sample fields: `is_fiskaly_order_receipt_signed`, `l10n_at_pos_order_receipt_number`
- XPath or positional patches: 1

### `view_pos_pos_form_l10n_at`
- Name: pos.order.form.austria.inherit
- Model: `pos.order`
- Type: inferred from arch
- Inherits: `point_of_sale.view_pos_pos_form`
- Root tag: `xpath`
- Field references: 2
- Sample fields: `is_fiskaly_order_receipt_signed`, `l10n_at_pos_order_receipt_number`
- XPath or positional patches: 1

## Actions

- `pos_order_sign_receipts`: `server` Sign Order

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_at_pos/Views]]

<!-- GENERATED:VIEWFILE -->
