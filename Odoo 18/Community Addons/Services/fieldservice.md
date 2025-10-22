---
tags: [v18, community, services, fieldservice, analysis]
status: draft
---
# Field Service Module (Community)

> **Summary:** Adds planning & scheduling of onsite interventions. Community features cover basic task assignment and time tracking; Enterprise brings mobile app, route optimization, and advanced logistics.

## 1. Principal models

| Model | Responsibilities |
|-------|------------------|
| `field.service.order` (module-specific) | Handles service orders with schedule, technician, status, materials. |
| `project.task` integration | Orders may create tasks for detailed tracking. |

## 2. Workflow
| Step | Description |
|------|-------------|
| Request capture | Ticket/quote triggers field service order. |
| Planning | Assign technician, set schedule, allocate resources. |
| Execution | Technician logs time/materials (portal or mobile in enterprise). |
| Closure | Mark done, generate report, invoice if needed. |

## 3. Integrations
- Helpdesk: escalate tickets to onsite service.
- Inventory: use stock moves for part consumption.
- Accounting: invoiceable services link to sale orders/invoices.
- Timesheets: track time for payroll/billing.

## 4. Configuration
- Define service teams, default technicians.
- Customize service reports/checklists.
- Route planning, geolocation (Enterprise features).

## 5. To-do (Issue #21)
- [ ] Confirm module availability/renaming across versions.
- [ ] Document mobile workflows when enterprise note ready.
- [ ] Provide example of inventory consumption from service order.

## Navigation
- **Parent:** `[[Odoo 18/Community Addons/Services/Index]]`
- **Related:** `[[Odoo 18/Core/Processes/Projects/Index]]`, `[[Odoo 18/Community Addons/Services/helpdesk.md]]`
- **Issue:** #21 `Docs: Odoo 18 - Community Services suite`
