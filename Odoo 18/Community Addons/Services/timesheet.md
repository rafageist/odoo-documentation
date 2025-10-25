---
tags: [v18, community, services, timesheet, analysis]
status: draft
---

# Timesheet Module (Odoo 18)

> **Summary:** Adds time tracking on tasks/projects and feeds billing/analytics. Core components rely on `account.analytic.line` for storage, integrating with Projects, Sales, and HR.

## 1. Principal models

| Model | File | Responsibilities |
|-------|------|------------------|
| `account.analytic.line` | `addons/hr_timesheet/models/account_analytic_line.py` | Stores timesheet entries (employee, task, date, hours). |
| `hr.timesheet.sheet` | (Enterprise)  not in CE. | Keep aware for references. |
| In CE: `project.task` linking timesheets. |

## 2. Timesheet recording
- Users log time via task kanban/list views, or dedicated timesheet view (`my_timesheet`).
- Fields: `employee_id`, `unit_amount`, `product_id` (service), `account_id` (analytic), `so_line`, `amount` (cost), `name` (description).
- Access restricted to employees; managers can see subordinates.

## 3. Billing integration
- When tied to a sale order line (`so_line`), delivered quantity updates automatically.
- Invoicing billed services uses `sale_timesheet` bridging module (documented in Sales notes).
- Cost tracking via analytic accounts for profitability reports (`account.analytic.account`).

## 4. Reporting
- Timesheet grid (weekly) summarises per employee/project.
- Pivot/graph views show billable vs non-billable hours, planned vs actual.
- KPIs: timesheet delay, employee utilization.

## 5. Configuration
- Enable module; set `timesheet_cost` on employee (`hr.employee`).
- Default unit (hours) adjustable; company-level rounding defined in settings.
- Security groups: `project.group_project_user`, `hr_timesheet.group_hr_timesheet_user` (CE includes basic rights).

## 6. To-do (Issue #21)
- [ ] Provide example timesheet entry with JSON for API usage.
- [ ] Document timesheet approvals once dedicated module covered.
- [ ] Link to payroll integration (Enterprise) if relevant.

## Navigation
- **Parent:** `[[Odoo 18/Community Addons/Services]]`
- **Related:** `[[Odoo 18/Core/Processes/Projects]]`, `[[Odoo 18/Community Addons/Sales/sale_project.md]]`, `[[Odoo 18/Core/Master Data/res_users.md]]`
- **Issue:** #21 `Docs: Odoo 18 - Community Services suite`
