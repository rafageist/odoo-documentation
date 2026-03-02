<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Mail Tests

- Scope: Community Addons
- Source: odoo/addons/test_mail
- Dependencies: [[docs/Community Addons/mail/mail|mail]], test_orm (not documented)

## Summary

Mail Tests: performances and tests specific to mail

## XML Artifacts (detected)

- Views: 0
- Actions: 0
- Menus: 0
- Rules (ir.rule): 19
- Access CSV entries: 77

## Detected Models

- `mail.test.access`
- `mail.test.access.custo`
- `mail.test.access.public`
- `mail.test.lead`
- `mail.test.ticket`
- `mail.test.ticket.el`
- `mail.test.ticket.mc`
- `mail.test.ticket.partner`
- `mail.test.container`
- `mail.test.container.mc`
- `mail.performance.thread`
- `mail.performance.thread.recipients`
- `mail.performance.tracking`
- `mail.test.field.type`
- `mail.test.lang`
- `mail.test.track.all.m2m`
- `mail.test.track.all.o2m`
- `mail.test.track.all.properties.parent`
- `mail.test.track.all`
- `mail.test.track.compute`
- `mail.test.track.duration.mixin`
- `mail.test.track.groups`
- `mail.test.track.monetary`
- `mail.test.track.selection`
- `mail.test.multi.company`
- `mail.test.multi.company.read`
- `mail.test.multi.company.with.activity`
- `mail.test.nothread`
- `mail.test.recipients`
- `mail.test.thread.customer`
- `mail.test.properties`
- `mail.test.rotting.stage`
- `mail.test.rotting.resource`
- `mail.test.simple`
- `mail.test.simple.unnamed`
- `mail.test.simple.main.attachment`
- `mail.test.simple.unfollow`
- `mail.test.alias.optional`
- `mail.test.gateway`
- `mail.test.gateway.company`
- `mail.test.gateway.main.attachment`
- `mail.test.gateway.groups`
- `mail.test.track`
- `mail.test.activity`
- `mail.test.composer.mixin`
- `mail.test.composer.source`
- `mail.test.cc`

```plantuml
@startuml
!include ../../../templates/DiagramStyles.puml
title Mail Tests - Models and Relations
class "mail.test.access" as mail_test_access
class "mail.test.access.custo" as mail_test_access_custo
class "mail.test.access.public" as mail_test_access_public
class "mail.test.lead" as mail_test_lead
class "mail.test.ticket" as mail_test_ticket
class "mail.test.ticket.el" as mail_test_ticket_el
class "mail.test.ticket.mc" as mail_test_ticket_mc
class "mail.test.ticket.partner" as mail_test_ticket_partner
class "mail.test.container" as mail_test_container
class "mail.test.container.mc" as mail_test_container_mc
class "mail.performance.thread" as mail_performance_thread
class "mail.performance.thread.recipients" as mail_performance_thread_recipients
class "mail.performance.tracking" as mail_performance_tracking
class "mail.test.field.type" as mail_test_field_type
class "mail.test.lang" as mail_test_lang
class "mail.test.track.all.m2m" as mail_test_track_all_m2m
class "mail.test.track.all.o2m" as mail_test_track_all_o2m
class "mail.test.track.all.properties.parent" as mail_test_track_all_properties_parent
class "mail.test.track.all" as mail_test_track_all
class "mail.test.track.compute" as mail_test_track_compute
class "mail.test.track.duration.mixin" as mail_test_track_duration_mixin
class "mail.test.track.groups" as mail_test_track_groups
class "mail.test.track.monetary" as mail_test_track_monetary
class "mail.test.track.selection" as mail_test_track_selection
class "mail.test.multi.company" as mail_test_multi_company
class "mail.test.multi.company.read" as mail_test_multi_company_read
class "mail.test.multi.company.with.activity" as mail_test_multi_company_with_activity
class "mail.test.nothread" as mail_test_nothread
class "mail.test.recipients" as mail_test_recipients
class "mail.test.thread.customer" as mail_test_thread_customer
class "mail.test.properties" as mail_test_properties
class "mail.test.rotting.stage" as mail_test_rotting_stage
class "mail.test.rotting.resource" as mail_test_rotting_resource
class "mail.test.simple" as mail_test_simple
class "mail.test.simple.unnamed" as mail_test_simple_unnamed
class "mail.test.simple.main.attachment" as mail_test_simple_main_attachment
class "mail.test.simple.unfollow" as mail_test_simple_unfollow
class "mail.test.alias.optional" as mail_test_alias_optional
class "mail.test.gateway" as mail_test_gateway
class "mail.test.gateway.company" as mail_test_gateway_company
class "mail.test.gateway.main.attachment" as mail_test_gateway_main_attachment
class "mail.test.gateway.groups" as mail_test_gateway_groups
class "mail.test.track" as mail_test_track
class "mail.test.activity" as mail_test_activity
class "mail.test.composer.mixin" as mail_test_composer_mixin
class "mail.test.composer.source" as mail_test_composer_source
class "mail.test.cc" as mail_test_cc
class "res.partner" as res_partner
mail_test_access --> res_partner : many2one
mail_test_access_custo --> res_partner : many2one
mail_test_access_public --> res_partner : many2one
class "res.company" as res_company
mail_test_lead --> res_company : many2one
class "res.users" as res_users
mail_test_lead --> res_users : many2one
mail_test_lead --> res_partner : many2one
class "mail.template" as mail_template
mail_test_ticket --> mail_template : many2one
mail_test_ticket --> res_partner : many2one
mail_test_ticket --> res_users : many2one
mail_test_ticket --> mail_test_container : many2one
mail_test_ticket_mc --> res_company : many2one
mail_test_ticket_mc --> mail_test_container_mc : many2one
mail_test_ticket_partner --> mail_template : many2one
mail_test_container --> res_partner : many2one
mail_test_container_mc --> res_company : many2one
mail_performance_thread --> res_partner : many2one
mail_performance_thread_recipients --> res_partner : many2one
mail_performance_thread_recipients --> res_users : many2one
mail_test_field_type --> res_partner : many2one
mail_test_field_type --> res_users : many2one
mail_test_lang --> res_partner : many2one
mail_test_track_all_o2m --> mail_test_track_all : many2one
mail_test_track_all --> res_company : many2one
class "res.currency" as res_currency
mail_test_track_all --> res_currency : many2one
mail_test_track_all .. mail_test_track_all_m2m : many2many
mail_test_track_all --> res_partner : many2one
mail_test_track_all --|> mail_test_track_all_o2m : one2many
mail_test_track_all --> mail_test_track_all_properties_parent : many2one
mail_test_track_compute --> res_partner : many2one
mail_test_track_duration_mixin --> res_partner : many2one
mail_test_track_groups --> res_partner : many2one
mail_test_track_monetary --> res_company : many2one
mail_test_track_monetary --> res_currency : many2one
mail_test_multi_company --> res_company : many2one
mail_test_multi_company_with_activity --> res_company : many2one
mail_test_nothread --> res_company : many2one
mail_test_nothread --> res_partner : many2one
mail_test_recipients --> res_company : many2one
mail_test_recipients .. res_partner : many2many
mail_test_recipients --> res_partner : many2one
mail_test_properties --> mail_test_properties : many2one
mail_test_rotting_resource --> mail_test_rotting_stage : many2one
mail_test_simple_unfollow --> res_company : many2one
mail_test_alias_optional --> res_company : many2one
mail_test_gateway --> res_users : many2one
mail_test_gateway_company --> res_company : many2one
mail_test_gateway_main_attachment --> res_company : many2one
mail_test_gateway_groups --> res_partner : many2one
mail_test_track --> res_users : many2one
mail_test_track --> mail_test_container : many2one
mail_test_track --> res_company : many2one
mail_test_track --> mail_test_track : many2one
mail_test_activity --> res_company : many2one
mail_test_composer_mixin --> res_partner : many2one
mail_test_composer_mixin .. mail_test_composer_source : many2many
mail_test_composer_source --> res_partner : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->




