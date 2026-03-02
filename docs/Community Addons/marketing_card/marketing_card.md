<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Marketing Card

- Scope: Community Addons
- Source: odoo/addons/marketing_card
- Dependencies: [[docs/Community Addons/link_tracker/link_tracker|link_tracker]], [[docs/Community Addons/mass_mailing/mass_mailing|mass_mailing]], [[docs/Community Addons/website/website|website]]

## Summary

Generate dynamic shareable cards

## XML Artifacts (detected)

- Views: 8
- Actions: 3
- Menus: 4
- Rules (ir.rule): 2
- Access CSV entries: 9

## Detected Models

- `card.campaign`
- `card.campaign.tag`
- `card.card`
- `card.template`
- `IrModel`
- `MailingMailing`
- `UtmSource`

```plantuml
@startuml
!include ../../../templates/DiagramStyles.puml
title Marketing Card - Models and Relations
class "card.campaign" as card_campaign
class "card.campaign.tag" as card_campaign_tag
class "card.card" as card_card
class "card.template" as card_template
class IrModel
class MailingMailing
class UtmSource
class "mailing.mailing" as mailing_mailing
card_campaign --|> mailing_mailing : one2many
card_campaign --|> card_card : one2many
card_campaign --> card_template : many2one
class "link.tracker" as link_tracker
card_campaign --> link_tracker : many2one
card_campaign .. card_campaign_tag : many2many
class "res.users" as res_users
card_campaign --> res_users : many2one
card_card --> card_campaign : many2one
MailingMailing --> card_campaign : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->





