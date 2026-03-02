<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Mass Mail Tests

- Scope: Community Addons
- Source: odoo/addons/test_mass_mailing
- Dependencies: [[docs/Community Addons/mass_mailing/mass_mailing|mass_mailing]], [[docs/Community Addons/mass_mailing_sms/mass_mailing_sms|mass_mailing_sms]], [[docs/Community Addons/sms_twilio/sms_twilio|sms_twilio]], [[docs/Community Addons/test_mail/test_mail|test_mail]], [[docs/Community Addons/test_mail_sms/test_mail_sms|test_mail_sms]]

## Summary

Mass Mail Tests: feature and performance tests for mass mailing

## XML Artifacts (detected)

- Views: 0
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 20

## Detected Models

- `mailing.test.customer`
- `mailing.test.simple`
- `mailing.test.utm`
- `mailing.test.blacklist`
- `mailing.test.optout`
- `mailing.test.partner`
- `mailing.performance`
- `mailing.performance.blacklist`
- `mailing.test.partner.unstored`
- `utm.test.source.mixin`
- `utm.test.source.mixin.other`

```plantuml
@startuml
!include ../../../templates/DiagramStyles.puml
title Mass Mail Tests - Models and Relations
class "mailing.test.customer" as mailing_test_customer
class "mailing.test.simple" as mailing_test_simple
class "mailing.test.utm" as mailing_test_utm
class "mailing.test.blacklist" as mailing_test_blacklist
class "mailing.test.optout" as mailing_test_optout
class "mailing.test.partner" as mailing_test_partner
class "mailing.performance" as mailing_performance
class "mailing.performance.blacklist" as mailing_performance_blacklist
class "mailing.test.partner.unstored" as mailing_test_partner_unstored
class "utm.test.source.mixin" as utm_test_source_mixin
class "utm.test.source.mixin.other" as utm_test_source_mixin_other
class "res.partner" as res_partner
mailing_test_customer --> res_partner : many2one
mailing_test_blacklist --> res_partner : many2one
class "res.users" as res_users
mailing_test_blacklist --> res_users : many2one
mailing_test_optout --> res_partner : many2one
mailing_test_optout --> res_users : many2one
mailing_test_partner --> res_partner : many2one
mailing_performance_blacklist --> res_users : many2one
class "mail.test.container" as mail_test_container
mailing_performance_blacklist --> mail_test_container : many2one
mailing_test_partner_unstored --> res_partner : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->



