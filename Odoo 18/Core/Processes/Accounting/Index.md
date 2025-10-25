---
tags: [v18, core, processes, accounting]
status: seed
---
# Core Accounting Processes v18

## Key flows
- `[[Odoo 18/Core/Processes/Accounting/account_move.md]]`
- Journal control (placeholder)
- Tax reporting (placeholder)

```plantuml
@startmindmap
* Accounting Processes
** Journal Entries
*** account.move
** Payments
** Tax Reporting
@endmindmap
```

## Next steps
- Detail payment matching (`account.payment`, bank reconciliation).
- Link inventory valuation moves coming from `stock.account` to `account.move`.
- Document closing process (lock dates, electronic invoicing).

## Navigation
- **Parent:** `[[Odoo 18/Core/Processes/Index.md]]`
- **Siblings:** `[[Odoo 18/Core/Processes/Sales/Index.md]]`, `[[Odoo 18/Core/Processes/Purchasing/Index.md]]`, `[[Odoo 18/Core/Processes/Inventory/Index.md]]`


## Children
- [[Odoo 18/Core/Processes/Accounting/account_move]]