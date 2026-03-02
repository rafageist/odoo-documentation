<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# audit.report

- Module: [[docs/Enterprise Addons/accountant_knowledge/accountant_knowledge|accountant_knowledge]]
- Scope: Enterprise Addons
- Defined in module: yes
- Source files: `models/audit_report.py`
- Python classes: `AuditReport`
- Description: Audit Report

## Field footprint

- Detected fields: 9
- Field types: `Char` x 1, `Date` x 2, `Integer` x 1, `Many2many` x 1, `Many2one` x 3, `Selection` x 1
- Relation fields: 4

## Sample fields

- `color`: `Integer`
- `company_id`: `Many2one` (comodel `res.company`)
- `end_date`: `Date`
- `knowledge_article_id`: `Many2one` (comodel `knowledge.article`)
- `knowledge_template_article_id`: `Many2one` (comodel `knowledge.article`)
- `responsible_user_ids`: `Many2many` (comodel `res.users`)
- `start_date`: `Date`
- `status`: `Selection`
- `title`: `Char`

## Method hints

- Detected methods: 6
- Action methods: `action_audit_report_pdf`, `action_edit_audit_report`, `action_set_to_done`, `action_set_to_draft`
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
title audit.report - Direct Relations
class "audit.report" as audit_report
class "knowledge.article" as knowledge_article
class "res.company" as res_company
class "res.users" as res_users
audit_report --> knowledge_article : knowledge_article_id
audit_report --> res_company : company_id
audit_report .. res_users : responsible_user_ids
audit_report --> knowledge_article : knowledge_template_article_id
@enduml
```

## Navigation

- **Parent:** [[docs/Enterprise Addons/accountant_knowledge/Models]]

<!-- GENERATED:MODEL -->
