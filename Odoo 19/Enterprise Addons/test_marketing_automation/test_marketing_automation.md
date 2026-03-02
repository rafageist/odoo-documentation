<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, enterprise, module]
---

# Marketing Automation Tests

- Version: v19
- Scope: Enterprise Addons
- Source: enterprise19/test_marketing_automation
- Dependencies: [[Odoo 19/Enterprise Addons/marketing_automation/marketing_automation|marketing_automation]], [[Odoo 19/Enterprise Addons/marketing_automation_sms/marketing_automation_sms|marketing_automation_sms]], [[Odoo 19/Enterprise Addons/marketing_automation_whatsapp/marketing_automation_whatsapp|marketing_automation_whatsapp]], [[Odoo 19/Community Addons/test_mail/test_mail|test_mail]], [[Odoo 19/Enterprise Addons/test_mail_enterprise/test_mail_enterprise|test_mail_enterprise]], [[Odoo 19/Community Addons/test_mail_full/test_mail_full|test_mail_full]], [[Odoo 19/Community Addons/test_mail_sms/test_mail_sms|test_mail_sms]], [[Odoo 19/Community Addons/test_mass_mailing/test_mass_mailing|test_mass_mailing]]

## Summary

Test Suite for Automated Marketing Campaigns

## XML Artifacts (detected)

- Views: 0
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 4

## Detected Models

- `marketing.test`
- `marketing.test.performance`
- `marketing.test.utm`
- `marketing.test.sms`

```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Marketing Automation Tests - Models and Relations
class "marketing.test" as marketing_test
class "marketing.test.performance" as marketing_test_performance
class "marketing.test.utm" as marketing_test_utm
class "marketing.test.sms" as marketing_test_sms
class "res.partner" as res_partner
marketing_test --> res_partner : many2one
class "res.company" as res_company
marketing_test_performance --> res_company : many2one
marketing_test_performance --> res_partner : many2one
marketing_test_utm --> res_partner : many2one
marketing_test_sms --> res_partner : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->

