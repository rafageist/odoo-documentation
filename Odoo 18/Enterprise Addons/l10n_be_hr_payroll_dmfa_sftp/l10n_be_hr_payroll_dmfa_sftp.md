<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, enterprise, module]
---

# Belgium - Payroll - DmfA SFTP

- Version: v18
- Category: enterprise
- Source: enterprise18/l10n_be_hr_payroll_dmfa_sftp
- Dependencies: [[Odoo 18/Enterprise Addons/l10n_be_hr_payroll/l10n_be_hr_payroll|l10n_be_hr_payroll]], [[Odoo 18/Community Addons/certificate/certificate|certificate]]
## XML Artifacts (detected)

- Views: 7
- Actions: 3
- Menus: 2
- Rules (ir.rule): 2
- Access CSV entries: 2

## Detected Models

- `l10n_be.dmfa`
- `l10n.be.onss.declaration`
- `l10n.be.onss.file`
- `ResCompany`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Belgium - Payroll - DmfA SFTP - Models and Relations
class "l10n_be.dmfa" as l10n_be_dmfa
class "l10n.be.onss.declaration" as l10n_be_onss_declaration
class "l10n.be.onss.file" as l10n_be_onss_file
class ResCompany
l10n_be_dmfa --|> l10n_be_onss_declaration : one2many
l10n_be_onss_declaration --> l10n_be_dmfa : many2one
class "res.company" as res_company
l10n_be_onss_declaration --> res_company : many2one
l10n_be_onss_declaration --|> l10n_be_onss_file : one2many
l10n_be_onss_file --> l10n_be_onss_declaration : many2one
class "hr.employee" as hr_employee
l10n_be_onss_file --> hr_employee : many2one
l10n_be_onss_file --> res_company : many2one
class "certificate.key" as certificate_key
ResCompany --> certificate_key : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
