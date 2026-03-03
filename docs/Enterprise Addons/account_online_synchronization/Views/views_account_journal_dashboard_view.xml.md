---
tags: [odoo, enterprise, generated, views]
---

# views/account_journal_dashboard_view.xml

- Module: [[docs/Enterprise Addons/account_online_synchronization/account_online_synchronization|account_online_synchronization]]
- Scope: Enterprise Addons
- Source file: `views/account_journal_dashboard_view.xml`
- Views: 1
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `account_journal_dashboard_inherit_online_sync`
- Name: account.journal.dashboard.inherit.online.sync
- Model: `account.journal`
- Type: inferred from arch
- Inherits: `account.account_journal_dashboard_kanban_view`
- Root tag: `field`
- Field references: 7
- Sample fields: `account_online_account_id`, `account_online_link_state`, `expiring_synchronization_date`, `expiring_synchronization_due_day`, `kanban_dashboard`, `next_link_synchronization`, `online_sync_fetching_status`
- Buttons: `action_reconnect_online_account`, `manual_sync`
- XPath or positional patches: 9

## Navigation

- **Parent:** [[docs/Enterprise Addons/account_online_synchronization/Views]]

