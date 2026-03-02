<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# wizard/account_move_reversal_views.xml

- Module: [[docs/Enterprise Addons/helpdesk_account/helpdesk_account|helpdesk_account]]
- Scope: Enterprise Addons
- Source file: `wizard/account_move_reversal_views.xml`
- Views: 1
- Actions: 2
- Menus: 0
- Rules: 0

## View records

### `view_account_move_reversal_inherit_helpdesk_account`
- Name: account.move.reversal.inherit.helpdesk.account
- Model: `account.move.reversal`
- Type: inferred from arch
- Inherits: `account.view_account_move_reversal`
- Root tag: `xpath`
- Field references: 5
- Sample fields: `helpdesk_sale_order_id`, `helpdesk_ticket_id`, `move_ids`, `suitable_move_ids`, `suitable_sale_order_ids`
- XPath or positional patches: 1

## Actions

- `helpdesk_ticket_action_refund_form`: `view`
- `helpdesk_ticket_action_refund`: `act_window` Refund

## Navigation

- **Parent:** [[docs/Enterprise Addons/helpdesk_account/Views]]

<!-- GENERATED:VIEWFILE -->
