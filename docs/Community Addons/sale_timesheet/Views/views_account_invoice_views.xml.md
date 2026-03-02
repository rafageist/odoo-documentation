<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/account_invoice_views.xml

- Module: [[docs/Community Addons/sale_timesheet/sale_timesheet|sale_timesheet]]
- Scope: Community Addons
- Source file: `views/account_invoice_views.xml`
- Views: 1
- Actions: 6
- Menus: 0
- Rules: 0

## View records

### `account_invoice_view_form_inherit_sale_timesheet`
- Name: account.invoice.form.inherit.timesheet
- Model: `account.move`
- Type: inferred from arch
- Inherits: `account.view_move_form`
- Root tag: `xpath`
- Field references: 3
- Sample fields: `timesheet_count`, `timesheet_encode_uom_id`, `timesheet_total_duration`
- Buttons: `%(sale_timesheet.action_timesheet_from_invoice)d`
- XPath or positional patches: 1

## Actions

- `action_timesheet_from_invoice_view_graph`: `view`
- `action_timesheet_from_invoice_view_pivot`: `view`
- `action_timesheet_from_invoice_view_kanban`: `view`
- `action_timesheet_from_invoice_view_form`: `view`
- `action_timesheet_from_invoice_view_tree`: `view`
- `action_timesheet_from_invoice`: `act_window` Timesheets

## Navigation

- **Parent:** [[docs/Community Addons/sale_timesheet/Views]]

<!-- GENERATED:VIEWFILE -->
