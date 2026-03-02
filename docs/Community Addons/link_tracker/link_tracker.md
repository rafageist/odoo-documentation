<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Link Tracker

- Scope: Community Addons
- Source: odoo/addons/link_tracker
- Dependencies: [[docs/Community Addons/utm/utm|utm]], [[docs/Community Addons/mail/mail|mail]]

## XML Artifacts (detected)

- Views: 10
- Actions: 3
- Menus: 1
- Rules (ir.rule): 0
- Access CSV entries: 9

## Detected Models

- `link.tracker`
- `link.tracker.code`
- `link.tracker.click`
- `UtmCampaign`

```plantuml
@startuml
!include ../../../templates/DiagramStyles.puml
title Link Tracker - Models and Relations
class "link.tracker" as link_tracker
class "link.tracker.code" as link_tracker_code
class "link.tracker.click" as link_tracker_click
class UtmCampaign
link_tracker --|> link_tracker_code : one2many
link_tracker --|> link_tracker_click : one2many
link_tracker_code --> link_tracker : many2one
class "utm.campaign" as utm_campaign
link_tracker_click --> utm_campaign : many2one
link_tracker_click --> link_tracker : many2one
class "res.country" as res_country
link_tracker_click --> res_country : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->





