<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# EDI for Mexico

- Scope: Enterprise Addons
- Source: enterprise/l10n_mx_edi
- Dependencies: [[docs/Enterprise Addons/account_accountant/account_accountant|account_accountant]], [[docs/Community Addons/l10n_mx/l10n_mx|l10n_mx]], [[docs/Community Addons/base_vat/base_vat|base_vat]], [[docs/Enterprise Addons/product_unspsc/product_unspsc|product_unspsc]], [[docs/Community Addons/certificate/certificate|certificate]]

## Summary

Mexican Localization for EDI documents

## XML Artifacts (detected)

- Views: 21
- Actions: 4
- Menus: 2
- Rules (ir.rule): 0
- Access CSV entries: 8

## Detected Models

- `AccountJournal`
- `AccountMove`
- `AccountMoveLine`
- `AccountPayment`
- `IrAttachment`
- `l10n_mx_edi.addenda`
- `l10n_mx_edi.document`
- `l10n_mx_edi.payment.method`
- `ProductTemplate`
- `ResBank`
- `ResCompany`
- `ResCountry`
- `ResCurrency`
- `ResPartner`

```plantuml
@startuml
!include ../../../templates/DiagramStyles.puml
title EDI for Mexico - Models and Relations
class AccountJournal
class AccountMove
class AccountMoveLine
class AccountPayment
class IrAttachment
class "l10n_mx_edi.addenda" as l10n_mx_edi_addenda
class "l10n_mx_edi.document" as l10n_mx_edi_document
class "l10n_mx_edi.payment.method" as l10n_mx_edi_payment_method
class ProductTemplate
class ResBank
class ResCompany
class ResCountry
class ResCurrency
class ResPartner
AccountJournal --> l10n_mx_edi_payment_method : many2one
AccountMove .. l10n_mx_edi_document : many2many
AccountMove --|> l10n_mx_edi_document : one2many
AccountMove --|> l10n_mx_edi_document : one2many
class "ir.attachment" as ir_attachment
AccountMove --> ir_attachment : many2one
class "account.move" as account_move
AccountMove --> account_move : many2one
class "certificate.certificate" as certificate_certificate
AccountMove --> certificate_certificate : many2one
AccountMove --> l10n_mx_edi_payment_method : many2one
AccountMove .. l10n_mx_edi_addenda : many2many
l10n_mx_edi_document .. account_move : many2many
l10n_mx_edi_document --> account_move : many2one
l10n_mx_edi_document --> ir_attachment : many2one
ResCompany --|> certificate_certificate : one2many
ResPartner .. l10n_mx_edi_addenda : many2many
ResPartner --> l10n_mx_edi_payment_method : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->



## Curated analysis

### Functional role
- `l10n_mx_edi` adds Mexican CFDI generation, signing, cancellation, download, and payment complement handling on top of accounting.
- It sits on both compliance and operational accounting, because journals, invoices, payments, addendas, and provider credentials all participate in the workflow.

### Operational footprint
- `account_move.py`, `account_journal.py`, and `l10n_mx_edi_document.py` drive most of the compliance logic, while XML data files load CFDI 4.0 and payment complement templates.
- The module also adds cron work, addenda support, certificate handling, and wizard flows for cancellation and global invoice creation.

### Evidence
- Source files: `enterprise/l10n_mx_edi/models/account_move.py`, `enterprise/l10n_mx_edi/models/account_journal.py`, `enterprise/l10n_mx_edi/models/l10n_mx_edi_document.py`
- Compliance data and views: `enterprise/l10n_mx_edi/data/4.0/cfdi.xml`, `enterprise/l10n_mx_edi/data/ir_cron.xml`, `enterprise/l10n_mx_edi/views/account_move_view.xml`
- Tests: `enterprise/l10n_mx_edi/tests/test_account_move.py`, `enterprise/l10n_mx_edi/tests/test_cfdi_download.py`, `enterprise/l10n_mx_edi/tests/test_cfdi_invoice_documents.py`

### Related notes
- `[[docs/Community Addons/account_edi/account_edi|account_edi]]`
- `[[docs/Community Addons/l10n_mx/l10n_mx|l10n_mx]]`

### Rollout and migration concerns
- PAC credentials, certificates, SAT cancellation rules, and XML templates must be validated before production issuance because failures block legal invoicing, not just an optional integration.
- Cutover plans should include payment complements, public invoices, rounding scenarios, and locked-period cancellation tests, since those are explicitly covered by the module test suite.
- Legacy comparison backlog was retired on 2026-03-02; keep this note focused on the current codebase.

