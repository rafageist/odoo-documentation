<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# WhatsApp in Marketing Automation

- Scope: Enterprise Addons
- Source: enterprise/marketing_automation_whatsapp
- Dependencies: [[docs/Enterprise Addons/marketing_automation/marketing_automation|marketing_automation]], [[docs/Enterprise Addons/whatsapp/whatsapp|whatsapp]]

## Summary

Integrate WhatsApp in marketing campaigns

## XML Artifacts (detected)

- Views: 3
- Actions: 1
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `DiscussChannel`
- `LinkTrackerClick`
- `MarketingActivity`
- `MarketingCampaign`
- `MarketingTrace`
- `WhatsappMessage`
- `WhatsappTemplate`
- `WhatsappTemplateButton`

```plantuml
@startuml
!include ../../../templates/DiagramStyles.puml
title WhatsApp in Marketing Automation - Models and Relations
class DiscussChannel
class LinkTrackerClick
class MarketingActivity
class MarketingCampaign
class MarketingTrace
class WhatsappMessage
class WhatsappTemplate
class WhatsappTemplateButton
class "whatsapp.message" as whatsapp_message
LinkTrackerClick --> whatsapp_message : many2one
class "whatsapp.template" as whatsapp_template
MarketingActivity --> whatsapp_template : many2one
MarketingTrace --> whatsapp_message : many2one
class "marketing.trace" as marketing_trace
WhatsappMessage --|> marketing_trace : one2many
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->



