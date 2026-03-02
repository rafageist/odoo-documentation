<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# l10n_be_reports.isoc.prepayment.pay.wizard

- Module: [[docs/Enterprise Addons/l10n_be_reports/l10n_be_reports|l10n_be_reports]]
- Scope: Enterprise Addons
- Defined in module: yes
- Source files: `wizard/isoc_prepayment_pay_wizard.py`
- Python classes: `L10n_Be_ReportsISOCPrepaymentPayWizard`
- Description: Payment instructions for ISOC prepayment
- Inherits: `qr.code.payment.wizard`

## Field footprint

- Detected fields: 2
- Field types: `Monetary` x 1, `Selection` x 1
- Relation fields: 0

## Sample fields

- `corporate_tax_rate`: `Selection` (related `company_id.l10n_be_isoc_corporate_tax_rate`)
- `profit_estimate`: `Monetary`

## Method hints

- Detected methods: 6
- Action methods: `action_mark_as_paid`, `action_pay_later`, `action_send_email_instructions`
- Compute methods: `_compute_amount_to_pay`
- Onchange methods: none

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_be_reports/Models]]

<!-- GENERATED:MODEL -->
