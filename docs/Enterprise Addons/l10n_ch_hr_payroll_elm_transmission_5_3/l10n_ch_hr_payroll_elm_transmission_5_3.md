
<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Swissdec Certified Payroll ELM 5.3

- Scope: Enterprise Addons
- Source: enterprise/l10n_ch_hr_payroll_elm_transmission_5_3
- Dependencies: [[docs/Enterprise Addons/l10n_ch_hr_payroll/l10n_ch_hr_payroll|l10n_ch_hr_payroll]]

## XML Artifacts (detected)

- Views: 10
- Actions: 1
- Menus: 1
- Rules (ir.rule): 0
- Access CSV entries: 2

## Detected Models

- `HrContract`
- `HrEmployee`
- `HrPayslip`
- `L10nChCompensationFund`
- `l10n.ch.caf.scale`
- `L10nChHrEmployeeChildren`
- `l10nChSicknessInsuranceLine`
- `l10nChSicknessInsuranceLineRate`
- `l10nChAdditionalAccidentInsuranceLine`
- `l10nChAdditionalAccidentInsuranceLineRate`
- `l10n.lpp.coordination.amount`
- `l10nChLppInsurance`

```plantuml
@startuml
!include ../../../templates/DiagramStyles.puml
title Swissdec Certified Payroll ELM 5.3 - Models and Relations
class HrContract
class HrEmployee
class HrPayslip
class L10nChCompensationFund
class "l10n.ch.caf.scale" as l10n_ch_caf_scale
class L10nChHrEmployeeChildren
class l10nChSicknessInsuranceLine
class l10nChSicknessInsuranceLineRate
class l10nChAdditionalAccidentInsuranceLine
class l10nChAdditionalAccidentInsuranceLineRate
class "l10n.lpp.coordination.amount" as l10n_lpp_coordination_amount
class l10nChLppInsurance
L10nChCompensationFund --|> l10n_ch_caf_scale : one2many
class "l10n.ch.compensation.fund" as l10n_ch_compensation_fund
l10n_ch_caf_scale --> l10n_ch_compensation_fund : many2one
class "l10n.ch.lpp.insurance" as l10n_ch_lpp_insurance
l10n_lpp_coordination_amount --> l10n_ch_lpp_insurance : many2one
l10nChLppInsurance --|> l10n_lpp_coordination_amount : one2many
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->

