<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# l10n_it_reports.monthly.tax.report.xml.export.wizard

- Module: [[docs/Enterprise Addons/l10n_it_reports/l10n_it_reports|l10n_it_reports]]
- Scope: Enterprise Addons
- Defined in module: yes
- Source files: `wizard/monthly_tax_report_xml_export.py`
- Python classes: `L10nItMonthlyTaxReportXmlExportWizard`
- Description: Italian Monthly Tax Report XML Export Wizard

## Field footprint

- Detected fields: 12
- Field types: `Boolean` x 1, `Char` x 6, `Date` x 1, `Many2one` x 1, `Selection` x 3
- Relation fields: 1

## Sample fields

- `commitment_date`: `Date`
- `company_code`: `Char`
- `declarant_fiscal_code`: `Char`
- `declarant_role_code`: `Selection`
- `id_sistema`: `Char`
- `intermediary_code`: `Char`
- `method`: `Selection`
- `parent_company_id`: `Many2one` (comodel `res.company`)
- `parent_company_vat_number`: `Char`
- `show_method`: `Boolean` (compute `_compute_show_method`)
- `submission_commitment`: `Selection`
- `taxpayer_code`: `Char`

## Method hints

- Detected methods: 4
- Action methods: `action_generate_export`
- Compute methods: `_compute_show_method`
- Onchange methods: none

## Direct relation diagram

```plantuml
@startuml
!define ODOO_COLOR_PRIMARY #714B67
!define ODOO_COLOR_ACCENT #875A7B
!define ODOO_COLOR_BG #FAF7FA

skinparam backgroundColor ODOO_COLOR_BG
skinparam defaultTextAlignment left
skinparam ArrowColor ODOO_COLOR_ACCENT
skinparam ClassBackgroundColor white
skinparam ClassBorderColor ODOO_COLOR_PRIMARY
skinparam ComponentBackgroundColor white
skinparam ComponentBorderColor ODOO_COLOR_PRIMARY
skinparam NoteBackgroundColor #FFF8FF
skinparam NoteBorderColor ODOO_COLOR_ACCENT
skinparam SequenceLifeLineBorderColor ODOO_COLOR_ACCENT
skinparam SequenceLifeLineBackgroundColor #FFFFFF
skinparam SequenceParticipantBorderColor ODOO_COLOR_PRIMARY
skinparam SequenceParticipantBackgroundColor #FFFFFF
skinparam sequence {
  ArrowColor ODOO_COLOR_ACCENT
  ActorBorderColor ODOO_COLOR_PRIMARY
}
title l10n_it_reports.monthly.tax.report.xml.export.wizard - Direct Relations
class "l10n_it_reports.monthly.tax.report.xml.export.wizard" as l10n_it_reports_monthly_tax_report_xml_export_wizard
class "res.company" as res_company
l10n_it_reports_monthly_tax_report_xml_export_wizard --> res_company : parent_company_id
@enduml
```

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_it_reports/Models]]

<!-- GENERATED:MODEL -->
