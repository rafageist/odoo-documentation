<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, community, module]
---

# SMS Tests

- Version: v19
- Scope: Community Addons
- Source: odoo19/addons/test_mail_sms
- Dependencies: [[Odoo 19/Community Addons/mail/mail|mail]], [[Odoo 19/Community Addons/sms/sms|sms]], [[Odoo 19/Community Addons/sms_twilio/sms_twilio|sms_twilio]], test_orm (not documented)

## Summary

SMS Tests: performances and tests specific to SMS

## XML Artifacts (detected)

- Views: 0
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 13

## Detected Models

- `mail.test.sms`
- `mail.test.sms.bl`
- `mail.test.sms.bl.activity`
- `mail.test.sms.bl.optout`
- `mail.test.sms.partner`
- `mail.test.sms.partner.2many`
- `sms.test.nothread`

```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title SMS Tests - Models and Relations
class "mail.test.sms" as mail_test_sms
class "mail.test.sms.bl" as mail_test_sms_bl
class "mail.test.sms.bl.activity" as mail_test_sms_bl_activity
class "mail.test.sms.bl.optout" as mail_test_sms_bl_optout
class "mail.test.sms.partner" as mail_test_sms_partner
class "mail.test.sms.partner.2many" as mail_test_sms_partner_2many
class "sms.test.nothread" as sms_test_nothread
class "res.partner" as res_partner
mail_test_sms .. res_partner : many2many
mail_test_sms --> res_partner : many2one
class "res.country" as res_country
mail_test_sms --> res_country : many2one
mail_test_sms_bl --> res_partner : many2one
mail_test_sms_bl_optout --> res_partner : many2one
mail_test_sms_partner --> res_partner : many2one
mail_test_sms_partner_2many .. res_partner : many2many
class "res.company" as res_company
sms_test_nothread --> res_company : many2one
sms_test_nothread --> res_partner : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->


