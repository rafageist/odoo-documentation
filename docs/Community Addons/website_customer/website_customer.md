<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Customer References

- Scope: Community Addons
- Source: odoo/addons/website_customer
- Dependencies: [[docs/Community Addons/website_crm_partner_assign/website_crm_partner_assign|website_crm_partner_assign]], [[docs/Community Addons/website_partner/website_partner|website_partner]], [[docs/Community Addons/website_google_map/website_google_map|website_google_map]]

## Summary

Publish your customer references

## XML Artifacts (detected)

- Views: 4
- Actions: 1
- Menus: 1
- Rules (ir.rule): 1
- Access CSV entries: 6

## Detected Models

- `ResPartner`
- `res.partner.tag`
- `Website`

```plantuml
@startuml
!include ../../../templates/DiagramStyles.puml
title Customer References - Models and Relations
class ResPartner
class "res.partner.tag" as res_partner_tag
class Website
ResPartner .. res_partner_tag : many2many
class "res.partner" as res_partner
res_partner_tag .. res_partner : many2many
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->



