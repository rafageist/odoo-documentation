<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, enterprise, module]
---

# WhatsApp in Marketing Automation

- Version: v18
- Category: enterprise
- Source: enterprise18/marketing_automation_whatsapp
- Dependencies: [[Odoo 18/Enterprise Addons/marketing_automation/marketing_automation|marketing_automation]], [[Odoo 18/Enterprise Addons/whatsapp/whatsapp|whatsapp]]

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
- `WhatsAppMessage`
- `WhatsAppTemplate`
- `WhatsAppTemplateButton`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title WhatsApp in Marketing Automation - Models and Relations
class DiscussChannel
class LinkTrackerClick
class MarketingActivity
class MarketingCampaign
class MarketingTrace
class WhatsAppMessage
class WhatsAppTemplate
class WhatsAppTemplateButton
class "whatsapp.message" as whatsapp_message
LinkTrackerClick --> whatsapp_message : many2one
class "whatsapp.template" as whatsapp_template
MarketingActivity --> whatsapp_template : many2one
MarketingTrace --> whatsapp_message : many2one
class "marketing.trace" as marketing_trace
WhatsAppMessage --|> marketing_trace : one2many
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
