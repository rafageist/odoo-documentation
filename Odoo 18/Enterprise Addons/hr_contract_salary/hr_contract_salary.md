<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, enterprise, module]
---

# Salary Configurator

- Version: v18
- Category: enterprise
- Source: enterprise18/hr_contract_salary
- Dependencies: [[Odoo 18/Enterprise Addons/hr_contract_sign/hr_contract_sign|hr_contract_sign]], [[Odoo 18/Enterprise Addons/hr_contract_reports/hr_contract_reports|hr_contract_reports]], [[Odoo 18/Community Addons/http_routing/http_routing|http_routing]], [[Odoo 18/Community Addons/hr_recruitment/hr_recruitment|hr_recruitment]], [[Odoo 18/Enterprise Addons/sign/sign|sign]]

## Summary

Sign Employment Contracts

## XML Artifacts (detected)

- Views: 26
- Actions: 9
- Menus: 10
- Rules (ir.rule): 4
- Access CSV entries: 42

## Detected Models

- `HrApplicant`
- `HrCandidate`
- `HrContract`
- `hr.contract.salary.benefit`
- `hr.contract.salary.benefit.type`
- `hr.contract.salary.benefit.value`
- `hr.contract.salary.offer`
- `hr.contract.salary.offer.refusal.reason`
- `hr.contract.salary.personal.info`
- `hr.contract.salary.personal.info.type`
- `hr.contract.salary.personal.info.value`
- `hr.contract.salary.resume.category`
- `hr.contract.salary.resume`
- `hr.contract.signatory`
- `HrJob`
- `HrPayrollStructureType`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Salary Configurator - Models and Relations
class HrApplicant
class HrCandidate
class HrContract
class "hr.contract.salary.benefit" as hr_contract_salary_benefit
class "hr.contract.salary.benefit.type" as hr_contract_salary_benefit_type
class "hr.contract.salary.benefit.value" as hr_contract_salary_benefit_value
class "hr.contract.salary.offer" as hr_contract_salary_offer
class "hr.contract.salary.offer.refusal.reason" as hr_contract_salary_offer_refusal_reason
class "hr.contract.salary.personal.info" as hr_contract_salary_personal_info
class "hr.contract.salary.personal.info.type" as hr_contract_salary_personal_info_type
class "hr.contract.salary.personal.info.value" as hr_contract_salary_personal_info_value
class "hr.contract.salary.resume.category" as hr_contract_salary_resume_category
class "hr.contract.salary.resume" as hr_contract_salary_resume
class "hr.contract.signatory" as hr_contract_signatory
class HrJob
class HrPayrollStructureType
HrApplicant --|> hr_contract_salary_offer : one2many
class "hr.contract" as hr_contract
HrApplicant .. hr_contract : many2many
HrContract --> hr_contract : many2one
class "hr.applicant" as hr_applicant
HrContract --> hr_applicant : many2one
HrContract --> hr_contract : many2one
class "sign.template" as sign_template
HrContract --> sign_template : many2one
HrContract --|> hr_contract_signatory : one2many
HrContract --> sign_template : many2one
HrContract --|> hr_contract_signatory : one2many
HrContract --|> hr_contract_salary_offer : one2many
HrContract --> hr_contract_salary_offer : many2one
class "ir.model.fields" as ir_model_fields
hr_contract_salary_benefit --> ir_model_fields : many2one
hr_contract_salary_benefit --> ir_model_fields : many2one
hr_contract_salary_benefit --> hr_contract_salary_benefit_type : many2one
hr_contract_salary_benefit .. hr_contract_salary_benefit : many2many
hr_contract_salary_benefit --> ir_model_fields : many2one
hr_contract_salary_benefit --> ir_model_fields : many2one
class "res.country" as res_country
hr_contract_salary_benefit --> res_country : many2one
class "hr.payroll.structure.type" as hr_payroll_structure_type
hr_contract_salary_benefit --> hr_payroll_structure_type : many2one
hr_contract_salary_benefit --|> hr_contract_salary_benefit_value : one2many
hr_contract_salary_benefit .. ir_model_fields : many2many
class "mail.activity.type" as mail_activity_type
hr_contract_salary_benefit --> mail_activity_type : many2one
class "res.users" as res_users
hr_contract_salary_benefit --> res_users : many2one
hr_contract_salary_benefit --> sign_template : many2one
class "res.partner" as res_partner
hr_contract_salary_benefit --> res_partner : many2one
hr_contract_salary_benefit_value --> hr_contract_salary_benefit : many2one
class "res.company" as res_company
hr_contract_salary_offer --> res_company : many2one
hr_contract_salary_offer --> hr_contract : many2one
hr_contract_salary_offer --> hr_contract_salary_offer_refusal_reason : many2one
class "sign.request" as sign_request
hr_contract_salary_offer .. sign_request : many2many
hr_contract_salary_offer --> hr_contract : many2one
hr_contract_salary_offer --> hr_applicant : many2one
class "hr.job" as hr_job
hr_contract_salary_offer --> hr_job : many2one
class "hr.department" as hr_department
hr_contract_salary_offer --> hr_department : many2one
hr_contract_salary_personal_info --> ir_model_fields : many2one
hr_contract_salary_personal_info --> hr_payroll_structure_type : many2one
hr_contract_salary_personal_info --> hr_contract_salary_personal_info_type : many2one
hr_contract_salary_personal_info --|> hr_contract_salary_personal_info_value : one2many
hr_contract_salary_personal_info --> hr_contract_salary_personal_info : many2one
hr_contract_salary_personal_info --|> hr_contract_salary_personal_info : one2many
hr_contract_salary_personal_info_value --> hr_contract_salary_personal_info : many2one
hr_contract_salary_resume .. hr_contract_salary_benefit : many2many
hr_contract_salary_resume --> hr_contract_salary_resume_category : many2one
hr_contract_salary_resume --> hr_payroll_structure_type : many2one
class "sign.item.role" as sign_item_role
hr_contract_signatory --> sign_item_role : many2one
hr_contract_signatory --> res_partner : many2one
hr_contract_signatory --> hr_contract : many2one
hr_contract_signatory --> hr_contract : many2one
HrJob --> hr_contract : many2one
HrPayrollStructureType --|> hr_contract_salary_benefit : one2many
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
