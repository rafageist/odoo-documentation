<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# WhatsApp Tests

- Scope: Enterprise Addons
- Source: enterprise/test_whatsapp
- Dependencies: [[docs/Community Addons/contacts/contacts|contacts]], [[docs/Community Addons/mail/mail|mail]], [[docs/Community Addons/portal/portal|portal]], [[docs/Enterprise Addons/whatsapp/whatsapp|whatsapp]]

## Summary

WhatsApp Tests

## XML Artifacts (detected)

- Views: 0
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 11

## Detected Models

- `whatsapp.test.base`
- `whatsapp.test.nothread`
- `whatsapp.test.nothread.noname`
- `whatsapp.test.responsible`
- `whatsapp.test.selection`
- `whatsapp.test.timezone`

```plantuml
@startuml
!include ../../../templates/DiagramStyles.puml
title WhatsApp Tests - Models and Relations
class "whatsapp.test.base" as whatsapp_test_base
class "whatsapp.test.nothread" as whatsapp_test_nothread
class "whatsapp.test.nothread.noname" as whatsapp_test_nothread_noname
class "whatsapp.test.responsible" as whatsapp_test_responsible
class "whatsapp.test.selection" as whatsapp_test_selection
class "whatsapp.test.timezone" as whatsapp_test_timezone
class "res.country" as res_country
whatsapp_test_base --> res_country : many2one
class "res.partner" as res_partner
whatsapp_test_base --> res_partner : many2one
whatsapp_test_base .. res_partner : many2many
class "res.users" as res_users
whatsapp_test_base --> res_users : many2one
whatsapp_test_base --> whatsapp_test_selection : many2one
whatsapp_test_nothread --> res_country : many2one
whatsapp_test_nothread --> res_partner : many2one
whatsapp_test_nothread --> res_users : many2one
whatsapp_test_nothread_noname --> res_country : many2one
whatsapp_test_nothread_noname --> res_partner : many2one
whatsapp_test_nothread_noname --> res_users : many2one
whatsapp_test_responsible .. res_users : many2many
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->



