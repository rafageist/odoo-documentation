---
tags: [v18, community, inventory, procurement, jit, analysis]
status: draft
---

# Procurement JIT Module (Odoo 18)

> **Summary:** `procurement_jit` forces procurements to run immediately when demand is created, bypassing the scheduled run. It shortens lead time responsiveness but increases processing load. Suitable for real-time environments where demand should trigger replenishment instantly.

## 1. Behaviour
- Installs overrides to call `_run_move_prepare` and `_run_procurement` immediately after sales/production triggers rather than waiting for the scheduler (`stock.scheduler.compute`).
- Affects creation of purchase orders, manufacturing orders, and internal transfers driven by procurement rules.
- Does not change rule configuration itself; it alters timing only.

## 2. Key code hooks
- Inherits from `stock.move` (`addons/procurement_jit/models/stock_move.py`).
- Overrides `action_confirm` and `_action_confirm` to call `_action_assign()` and `_procure_orderpoint_confirm` without delay.
- For purchase flows, triggers `_run_buy` instantly, leading to `purchase.order` creation upon confirming sale/delivery order.

## 3. Pros & cons
- **Pros:**
  - Eliminate delay between demand creation and procurement; helpful for make-to-order setups or drop-shipping where timing is critical.
  - Reduces need to schedule cron jobs for timely replenishment.
- **Cons:**
  - Increased processing at confirmation time; may slow down large batch operations.
  - Removes ability to review draft procurements before creation.
  - Unsuitable for companies relying on nightly batch planning or approval workflows.

## 4. Integration
- Works alongside `stock`, `purchase`, `mrp` modules; however, double validation or approval modules should be evaluated to avoid immediate PO creation without review.
- For drop-shipping, ensures supplier POs are created at order confirmation.
- Watch interaction with procurement lead times (`orderpoint` configuration still respected).

## 5. Configuration
- No UI settings. Installing module is enough.
- Cron `stock.scheduler.compute` remains available but is redundant for demand processes covered by JIT.

## 6. To-do (Issue #20)
- [ ] Document concrete examples showing order confirmation -> immediate PO creation.
- [ ] Measure performance impact for large order batches.
- [ ] Highlight scenarios where standard scheduler is preferred.

## Navigation
- **Parent:** `[[Odoo 18/Community Addons/Inventory]]`
- **Related:** `[[Odoo 18/Core/Processes/Inventory]]`, `[[Odoo 18/Core/Processes/Purchasing]]`, `[[Odoo 18/Core/Processes/Manufacturing]]`
- **Issue:** #20 `Docs: Odoo 18 - Community Operations suite`
