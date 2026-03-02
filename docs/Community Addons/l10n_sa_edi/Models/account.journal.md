<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# account.journal

- Module: [[docs/Community Addons/l10n_sa_edi/l10n_sa_edi|l10n_sa_edi]]
- Scope: Community Addons
- Defined in module: extension only
- Source files: `models/account_journal.py`
- Python classes: `AccountJournal`

## Field footprint

- Detected fields: 10
- Field types: `Binary` x 1, `Boolean` x 1, `Char` x 3, `Datetime` x 1, `Html` x 1, `Many2one` x 3
- Relation fields: 3

## Sample fields

- `l10n_sa_chain_sequence_id`: `Many2one` (comodel `ir.sequence`)
- `l10n_sa_compliance_checks_passed`: `Boolean` (comodel `Compliance Checks Done`)
- `l10n_sa_compliance_csid_certificate_id`: `Many2one` (comodel `certificate.certificate`)
- `l10n_sa_compliance_csid_json`: `Char` (comodel `CCSID JSON`)
- `l10n_sa_csr`: `Binary`
- `l10n_sa_csr_errors`: `Html` (comodel `Onboarding Errors`)
- `l10n_sa_latest_submission_hash`: `Char` (comodel `Latest Submission Hash`)
- `l10n_sa_production_csid_certificate_id`: `Many2one` (comodel `certificate.certificate`)
- `l10n_sa_production_csid_json`: `Char` (comodel `PCSID JSON`)
- `l10n_sa_production_csid_validity`: `Datetime` (related `l10n_sa_production_csid_certificate_id.date_end`)

## Method hints

- Detected methods: 29
- Action methods: none
- Compute methods: none
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
title account.journal - Direct Relations
class "account.journal" as account_journal
class "certificate.certificate" as certificate_certificate
class "ir.sequence" as ir_sequence
account_journal --> certificate_certificate : l10n_sa_production_csid_certificate_id
account_journal --> certificate_certificate : l10n_sa_compliance_csid_certificate_id
account_journal --> ir_sequence : l10n_sa_chain_sequence_id
@enduml
```

## Navigation

- **Parent:** [[docs/Community Addons/l10n_sa_edi/Models]]

<!-- GENERATED:MODEL -->
