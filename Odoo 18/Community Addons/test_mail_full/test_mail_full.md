<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, community, module]
---

# Mail Tests (Full)

- Version: v18
- Category: community
- Source: odoo/addons/test_mail_full
- Dependencies: [[Odoo 18/Community Addons/mail/mail|mail]], [[Odoo 18/Community Addons/mail_bot/mail_bot|mail_bot]], [[Odoo 18/Community Addons/portal/portal|portal]], [[Odoo 18/Community Addons/rating/rating|rating]], [[Odoo 18/Community Addons/mass_mailing/mass_mailing|mass_mailing]], [[Odoo 18/Community Addons/mass_mailing_sms/mass_mailing_sms|mass_mailing_sms]], [[Odoo 18/Community Addons/phone_validation/phone_validation|phone_validation]], [[Odoo 18/Community Addons/sms/sms|sms]], [[Odoo 18/Community Addons/test_mail/test_mail|test_mail]], [[Odoo 18/Community Addons/test_mail_sms/test_mail_sms|test_mail_sms]], [[Odoo 18/Community Addons/test_mass_mailing/test_mass_mailing|test_mass_mailing]]

## Summary

Mail Tests: performances and tests specific to mail with all sub-modules

## XML Artifacts (detected)

- Views: 0
- Actions: 0
- Menus: 0
- Rules (ir.rule): 2
- Access CSV entries: 12

## Detected Models

- `mail.test.portal`
- `mail.test.portal.no.partner`
- `mail.test.portal.public.access.action`
- `mail.test.rating`
- `mail.test.rating.thread`
- `mail.test.rating.thread.read`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Mail Tests (Full) - Models and Relations
class "mail.test.portal" as mail_test_portal
class "mail.test.portal.no.partner" as mail_test_portal_no_partner
class "mail.test.portal.public.access.action" as mail_test_portal_public_access_action
class "mail.test.rating" as mail_test_rating
class "mail.test.rating.thread" as mail_test_rating_thread
class "mail.test.rating.thread.read" as mail_test_rating_thread_read
class "res.partner" as res_partner
mail_test_portal --> res_partner : many2one
class "res.users" as res_users
mail_test_portal --> res_users : many2one
class "res.company" as res_company
mail_test_rating --> res_company : many2one
mail_test_rating --> res_partner : many2one
mail_test_rating --> res_users : many2one
mail_test_rating_thread --> res_partner : many2one
mail_test_rating_thread --> res_users : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
