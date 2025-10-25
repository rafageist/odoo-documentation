---
tags: [v18, community, sales, sale_management, analysis]
status: draft
---

# Sales Management Module (Odoo 18)

> **Summary:** `sale_management` delivers the core sales order features beyond CRM: quotations, pricing, invoicing triggers, and delivery coordination. It extends the core sales process described in `[[Odoo 18/Core/Processes/Sales]]` with UI, wizards, and reporting.

## 1. Principal models & components

| Component | File | Responsibilities |
|-----------|------|------------------|
| `sale.order`, `sale.order.line` | `addons/sale/models/sale_order.py` | Main logic for quotations/orders; handles state transitions, pricing, taxes, delivered/invoiced quantities. |
| `sale.order.option`, `sale.order.line.option` | `addons/sale/models/sale_order.py` | Optional products on quotation (up-selling). |
| `sale.advance.payment.inv` (wizard) | `addons/sale/wizard/sale_make_invoice_advance.py` | Down payments and invoicing options. |
| `sale.order.cancel`, `sale.mass.reschedule`, `sale.order.close` (wizards) | Various | Manage cancellation, rescheduling, closing orders. |
| Reports (`sale.report`, `sale.order.template`) | Provide dashboards and quotation templates. |

## 2. Pricing, discounts, and taxes
- Pricelists: `product.pricelist` rules choose base price, discount, margin. Seasonality and currency managed per pricelist.
- Discounts: line-level discount field; can auto-apply via pricelist rules or promotions (`sale_coupon`).
- Taxes auto-set from product/company/partner; fiscal positions (`account.fiscal.position`) remap accounts/taxes.
- Coupons/Promotions: optional modules extend `sale.order` with reward lines, conditions; to be documented separately.

## 3. Workflow & wizards
- Quotation creation -> `action_confirm` -> delivers/invoices as per configuration (see Sales core note for sequence diagram).
- `sale.order.line._action_launch_procurement_rule()` ties to inventory for stockable products.
- Down payments wizard adds service lines or percentage deposits.
- Cancel wizard enforces state checks and optionally restocks products.
- Reschedule wizard adjusts commitment dates; interacts with `stock.move` (`delivery_status`).

## 4. Reports & dashboards
- `sale.report`: aggregated SQL view used for graph/pivot reports (orders, revenue, margins).
- Quotation templates: `sale.order.template` pre-fill order lines/options; ability to set validity days, default email template.
- KPI dashboards: per salesperson/team, pipeline values via CRM integration.

## 5. Integration highlights
- **Inventory:** delivered qty computed via stock moves; returns handled via `stock.return.picking`. Documented in `[[Odoo 18/Core/Processes/Inventory]]`.
- **Accounting:** invoice policies and down payments link to `account.move`. See `[[Odoo 18/Core/Processes/Accounting]]`.
- **Projects/Subscriptions:** `sale_project`, `sale_subscription` rely on fields like `service_tracking` and `recurrence_id` to extend order lines.
- **Portal:** `sale_portal` exposes quotations/orders on website, allowing acceptance/refusal, signature.

## 6. Configuration
- Settings toggle discounts, pro-forma invoices, online signature, multi-step invoices.
- Default journals/products set via `res.config.settings` (down payment product, deposit account).
- Security: groups `sales_team.group_sale_user`, `group_sale_manager` control UI/features. See `[[Odoo 18/Core/Master Data/res_users.md]]` for access analysis.

## 7. To-do (Issue #18)
- [ ] Provide examples of quotation template usage.
- [ ] Document integration with coupon/promotion modules.
- [ ] Add sample RPC payload for confirmation and invoicing.

## Navigation
- **Parent:** [[Odoo 18/Community Addons/Sales/Sales]]
