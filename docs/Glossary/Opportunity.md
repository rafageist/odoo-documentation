---
tags: [odoo, glossary, business]
status: active
---

# Opportunity

## Definition
- An opportunity is a qualified sales case with enough confidence, data, and intent to be worked through a pipeline.
- In Odoo CRM, leads and opportunities share the same main model, but they represent different business maturity.

## Why developers should care
- Pipeline stage logic, quotations, expected revenue, win/loss analysis, and sales-team automation usually target opportunities rather than raw leads.
- A customization that ignores the lead-to-opportunity transition often produces broken reporting or noisy automations.

## Technical anchors
- Main model: `crm.lead`
- Functional module: `[[docs/Community Addons/crm/crm|crm]]`
- Sales bridge: `[[docs/Community Addons/sale_management/sale_management|sale_management]]`

## Related terms
- `[[docs/Glossary/Lead]]`
- `[[docs/Glossary/Partner]]`
- `[[docs/Glossary/Activity]]`

## Navigation
- **Parent:** [[docs/Glossary/Glossary]]
