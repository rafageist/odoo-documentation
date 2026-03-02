<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# report/mrp_report_views.xml

- Module: [[docs/Enterprise Addons/mrp_subcontracting_account_enterprise/mrp_subcontracting_account_enterprise|mrp_subcontracting_account_enterprise]]
- Scope: Enterprise Addons
- Source file: `report/mrp_report_views.xml`
- Views: 2
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `mrp_report_form_view_inherit_subcontracting`
- Name: mrp.report.view.form.inherit.subcontracting
- Model: `mrp.report`
- Type: inferred from arch
- Inherits: `mrp_account_enterprise.mrp_report_form_view`
- Root tag: `field`
- Field references: 4
- Sample fields: `operation_cost`, `subcontracting_cost`, `unit_operation_cost`, `unit_subcontracting_cost`
- XPath or positional patches: 0

### `mrp_report_pivot_view_inherit_subcontracting`
- Name: mrp.report.view.pivot.inherit.subcontracting
- Model: `mrp.report`
- Type: inferred from arch
- Inherits: `mrp_account_enterprise.mrp_report_pivot_view`
- Root tag: `field`
- Field references: 2
- Sample fields: `unit_operation_cost`, `unit_subcontracting_cost`
- XPath or positional patches: 0

## Navigation

- **Parent:** [[docs/Enterprise Addons/mrp_subcontracting_account_enterprise/Views]]

<!-- GENERATED:VIEWFILE -->
