<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Salary Configurator

- Scope: Enterprise Addons
- Source: enterprise/hr_contract_salary
- Dependencies: [[docs/Enterprise Addons/hr_sign/hr_sign|hr_sign]], [[docs/Community Addons/http_routing/http_routing|http_routing]], [[docs/Community Addons/hr_recruitment/hr_recruitment|hr_recruitment]], [[docs/Enterprise Addons/sign/sign|sign]]

## Summary

Sign Employment Contracts

## XML Artifacts (detected)

- Views: 27
- Actions: 12
- Menus: 10
- Rules (ir.rule): 4
- Access CSV entries: 43

## Detected Models

- `HrApplicant`
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
- `HrEmployee`
- `HrEmployeePublic`
- `HrJob`
- `HrPayrollStructureType`
- `HrVersion`
- `SignItem`
- `SignRequest`

```plantuml
@startuml
!include ../../../templates/DiagramStyles.puml
title Salary Configurator - Models and Relations
class HrApplicant
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
class HrEmployee
class HrEmployeePublic
class HrJob
class HrPayrollStructureType
class HrVersion
class SignItem
class SignRequest
HrApplicant --|> hr_contract_salary_offer : one2many
class "hr.version" as hr_version
HrApplicant .. hr_version : many2many
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
class "sign.template" as sign_template
hr_contract_salary_benefit --> sign_template : many2one
class "res.partner" as res_partner
hr_contract_salary_benefit --> res_partner : many2one
hr_contract_salary_benefit_value --> hr_contract_salary_benefit : many2one
class "res.company" as res_company
hr_contract_salary_offer --> res_company : many2one
hr_contract_salary_offer --> hr_version : many2one
hr_contract_salary_offer --> sign_template : many2one
hr_contract_salary_offer --|> hr_contract_signatory : one2many
hr_contract_salary_offer --> hr_contract_salary_offer_refusal_reason : many2one
class "sign.request" as sign_request
hr_contract_salary_offer .. sign_request : many2many
hr_contract_salary_offer --> hr_version : many2one
class "hr.employee" as hr_employee
hr_contract_salary_offer --> hr_employee : many2one
class "hr.applicant" as hr_applicant
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
hr_contract_signatory --> hr_version : many2one
hr_contract_signatory --> hr_version : many2one
hr_contract_signatory --> hr_contract_salary_offer : many2one
HrJob --> hr_version : many2one
HrPayrollStructureType --|> hr_contract_salary_benefit : one2many
HrVersion --> hr_version : many2one
HrVersion --> hr_applicant : many2one
HrVersion --> sign_template : many2one
HrVersion --|> hr_contract_signatory : one2many
HrVersion --> sign_template : many2one
HrVersion --|> hr_contract_signatory : one2many
HrVersion --|> hr_contract_salary_offer : one2many
HrVersion --> hr_contract_salary_offer : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->



