<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# l10n_pl_reports.periodic.vat.xml.export

- Module: [[docs/Enterprise Addons/l10n_pl_reports/l10n_pl_reports|l10n_pl_reports]]
- Scope: Enterprise Addons
- Defined in module: yes
- Source files: `wizard/vat_report_export.py`
- Python classes: `L10n_Pl_ReportsPeriodicVatXmlExport`
- Description: Polish Periodic VAT Report Export Wizard

## Field footprint

- Detected fields: 10
- Field types: `Boolean` x 4, `Char` x 2, `Date` x 1, `Integer` x 2, `Selection` x 1
- Relation fields: 0

## Sample fields

- `l10n_pl_birthdate`: `Date`
- `l10n_pl_is_amendment`: `Boolean` (comodel `Is an amendment`)
- `l10n_pl_paid_before_deadline`: `Boolean` (comodel `Tax liability has been paid in full before deadline`)
- `l10n_pl_reason_amendment`: `Char` (comodel `Reasons for the amendment`)
- `l10n_pl_repayment_amount`: `Integer` (comodel `Amount to be reimbursed by the government`)
- `l10n_pl_repayment_future_tax`: `Boolean` (comodel `Credit the tax repayment amount towards future tax obligations`)
- `l10n_pl_repayment_future_tax_amount`: `Integer` (comodel `Amount to be credited towards future tax obligations`)
- `l10n_pl_repayment_future_tax_type`: `Char` (comodel `Type of future tax obligations to be credited`)
- `l10n_pl_repayment_timeframe`: `Selection`
- `partner_is_company`: `Boolean` (compute `_compute_partner_is_company`)

## Method hints

- Detected methods: 2
- Action methods: none
- Compute methods: `_compute_partner_is_company`
- Onchange methods: none

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_pl_reports/Models]]

<!-- GENERATED:MODEL -->
