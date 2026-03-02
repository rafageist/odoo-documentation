<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, enterprise, module]
---

# Belgian Intervat & Myminfin Edi

- Version: v19
- Scope: Enterprise Addons
- Source: enterprise19/l10n_be_intervat
- Dependencies: [[Odoo 19/Community Addons/l10n_be/l10n_be|l10n_be]], [[Odoo 19/Enterprise Addons/l10n_be_reports/l10n_be_reports|l10n_be_reports]], [[Odoo 19/Community Addons/certificate/certificate|certificate]]

## XML Artifacts (detected)

- Views: 3
- Actions: 0
- Menus: 0
- Rules (ir.rule): 1
- Access CSV entries: 2

## Detected Models

- `AccountReturn`
- `Certificate`
- `l10n_be.vat.declaration`
- `ResCompany`

```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Belgian Intervat & Myminfin Edi - Models and Relations
class AccountReturn
class Certificate
class "l10n_be.vat.declaration" as l10n_be_vat_declaration
class ResCompany
l10n_be_vat_declaration --> l10n_be_vat_declaration : many2one
class "account.return" as account_return
l10n_be_vat_declaration --> account_return : many2one
class "certificate.key" as certificate_key
ResCompany --> certificate_key : many2one
class "certificate.certificate" as certificate_certificate
ResCompany --> certificate_certificate : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->
