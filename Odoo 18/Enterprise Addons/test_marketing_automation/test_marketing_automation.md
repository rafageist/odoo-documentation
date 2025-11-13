<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, enterprise, module]
---

# Marketing Automation Tests

- Version: v18
- Category: enterprise
- Source: enterprise18/test_marketing_automation
- Dependencies: [[Odoo 18/Enterprise Addons/marketing_automation/marketing_automation|marketing_automation]], [[Odoo 18/Enterprise Addons/marketing_automation_sms/marketing_automation_sms|marketing_automation_sms]], [[Odoo 18/Enterprise Addons/marketing_automation_whatsapp/marketing_automation_whatsapp|marketing_automation_whatsapp]], [[Odoo 18/Community Addons/test_mail/test_mail|test_mail]], [[Odoo 18/Enterprise Addons/test_mail_enterprise/test_mail_enterprise|test_mail_enterprise]], [[Odoo 18/Community Addons/test_mail_full/test_mail_full|test_mail_full]], [[Odoo 18/Community Addons/test_mail_sms/test_mail_sms|test_mail_sms]], [[Odoo 18/Community Addons/test_mass_mailing/test_mass_mailing|test_mass_mailing]]

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

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
