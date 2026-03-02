<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Mail Tests (Full)

- Scope: Community Addons
- Source: odoo/addons/test_mail_full
- Dependencies: [[docs/Community Addons/mail/mail|mail]], [[docs/Community Addons/mail_bot/mail_bot|mail_bot]], [[docs/Community Addons/portal/portal|portal]], [[docs/Community Addons/rating/rating|rating]], [[docs/Community Addons/mass_mailing/mass_mailing|mass_mailing]], [[docs/Community Addons/mass_mailing_sms/mass_mailing_sms|mass_mailing_sms]], [[docs/Community Addons/phone_validation/phone_validation|phone_validation]], [[docs/Community Addons/sms/sms|sms]], [[docs/Community Addons/test_mail/test_mail|test_mail]], [[docs/Community Addons/test_mail_sms/test_mail_sms|test_mail_sms]], [[docs/Community Addons/test_mass_mailing/test_mass_mailing|test_mass_mailing]]

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
!include ../../../templates/DiagramStyles.puml
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

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->




