<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, community, module]
---

# eLearning

- Version: v18
- Category: community
- Source: odoo/addons/website_slides
- Dependencies: [[Odoo 18/Community Addons/portal_rating/portal_rating|portal_rating]], [[Odoo 18/Community Addons/website/website|website]], [[Odoo 18/Community Addons/website_mail/website_mail|website_mail]], [[Odoo 18/Community Addons/website_profile/website_profile|website_profile]]

## Summary

Manage and publish an eLearning platform

## XML Artifacts (detected)

- Views: 49
- Actions: 29
- Menus: 15
- Rules (ir.rule): 21
- Access CSV entries: 41

## Detected Models

- `Challenge`
- `KarmaTracking`
- `UserGroup`
- `ResPartner`
- `Users`
- `slide.channel.partner`
- `slide.channel`
- `slide.channel.tag.group`
- `slide.channel.tag`
- `slide.embed`
- `slide.question`
- `slide.answer`
- `slide.slide.partner`
- `slide.tag`
- `slide.slide`
- `slide.slide.resource`
- `Website`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title eLearning - Models and Relations
class Challenge
class KarmaTracking
class UserGroup
class ResPartner
class Users
class "slide.channel.partner" as slide_channel_partner
class "slide.channel" as slide_channel
class "slide.channel.tag.group" as slide_channel_tag_group
class "slide.channel.tag" as slide_channel_tag
class "slide.embed" as slide_embed
class "slide.question" as slide_question
class "slide.answer" as slide_answer
class "slide.slide.partner" as slide_slide_partner
class "slide.tag" as slide_tag
class "slide.slide" as slide_slide
class "slide.slide.resource" as slide_slide_resource
class Website
ResPartner .. slide_channel : many2many
ResPartner --|> slide_channel : one2many
slide_channel_partner --> slide_channel : many2one
class "res.partner" as res_partner
slide_channel_partner --> res_partner : many2one
class "res.users" as res_users
slide_channel_partner --> res_users : many2one
class website
slide_channel_partner --> website : many2one
slide_channel_partner --> slide_slide : many2one
slide_channel --> res_users : many2one
slide_channel .. slide_channel_tag : many2many
slide_channel --|> slide_slide : one2many
slide_channel --|> slide_slide : one2many
slide_channel --|> slide_slide : one2many
slide_channel --|> slide_slide_partner : one2many
slide_channel --> slide_slide : many2one
class "mail.template" as mail_template
slide_channel --> mail_template : many2one
slide_channel --> mail_template : many2one
slide_channel --> mail_template : many2one
slide_channel --> mail_template : many2one
class "res.groups" as res_groups
slide_channel .. res_groups : many2many
slide_channel .. res_groups : many2many
slide_channel --|> slide_channel_partner : one2many
slide_channel --|> slide_channel_partner : one2many
slide_channel .. res_partner : many2many
slide_channel .. slide_channel : many2many
slide_channel .. slide_channel : many2many
slide_channel_tag_group --|> slide_channel_tag : one2many
slide_channel_tag --> slide_channel_tag_group : many2one
slide_channel_tag .. slide_channel : many2many
slide_embed --> slide_slide : many2one
slide_question --> slide_slide : many2one
slide_question --|> slide_answer : one2many
slide_answer --> slide_question : many2one
slide_slide_partner --> slide_slide : many2one
slide_slide_partner --> slide_channel : many2one
slide_slide_partner --> res_partner : many2one
slide_slide --> res_users : many2one
slide_slide --> slide_channel : many2one
slide_slide .. slide_tag : many2many
slide_slide --> slide_slide : many2one
slide_slide --|> slide_slide : one2many
slide_slide .. res_partner : many2many
slide_slide --|> slide_slide_partner : one2many
slide_slide --> slide_slide_partner : many2one
slide_slide --|> slide_question : one2many
slide_slide --|> slide_slide_resource : one2many
slide_slide --|> slide_embed : one2many
slide_slide_resource --> slide_slide : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
