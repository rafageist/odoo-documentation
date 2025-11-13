<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, enterprise, module]
---

# Australia - Payroll with API

- Version: v19
- Category: enterprise
- Source: enterprise19/l10n_au_hr_payroll_api
- Dependencies: [[Odoo 19/Enterprise Addons/l10n_au_hr_payroll_account/l10n_au_hr_payroll_account|l10n_au_hr_payroll_account]], [[Odoo 19/Community Addons/account_edi_proxy_client/account_edi_proxy_client|account_edi_proxy_client]], [[Odoo 19/Community Addons/auth_timeout/auth_timeout|auth_timeout]]
## XML Artifacts (detected)

- Views: 12
- Actions: 1
- Menus: 2
- Rules (ir.rule): 2
- Access CSV entries: 4

## Detected Models

- `AccountEdiProxyClientUser`
- `hr.employee`
- `Payslip`
- `IrAttachment`
- `l10n_au.audit.log`
- `l10n_au.employer.registration`
- `L10n_AuSTP`
- `L10n_auSuperStream`
- `L10n_auSuperStreamLine`
- `L10n_AuSuperFund`
- `res.company`
- `res.groups`
- `res.partner.bank`
- `res.users`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Australia - Payroll with API - Models and Relations
class AccountEdiProxyClientUser
class "hr.employee" as hr_employee
class Payslip
class IrAttachment
class "l10n_au.audit.log" as l10n_au_audit_log
class "l10n_au.employer.registration" as l10n_au_employer_registration
class L10n_AuSTP
class L10n_auSuperStream
class L10n_auSuperStreamLine
class L10n_AuSuperFund
class "res.company" as res_company
class "res.groups" as res_groups
class "res.partner.bank" as res_partner_bank
class "res.users" as res_users
l10n_au_audit_log --> res_company : many2one
l10n_au_employer_registration --> res_company : many2one
class "l10n_au.super.stream.line" as l10n_au_super_stream_line
L10n_auSuperStreamLine --> l10n_au_super_stream_line : many2one
class "account_edi_proxy_client.user" as account_edi_proxy_client_user
res_company --> account_edi_proxy_client_user : many2one
res_company --|> l10n_au_employer_registration : one2many
res_company --> l10n_au_employer_registration : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->
