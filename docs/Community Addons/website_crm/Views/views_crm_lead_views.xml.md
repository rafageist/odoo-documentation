---
tags: [odoo, community, generated, views]
---

# views/crm_lead_views.xml

- Module: [[docs/Community Addons/website_crm/website_crm|website_crm]]
- Scope: Community Addons
- Source file: `views/crm_lead_views.xml`
- Views: 1
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `crm_lead_view_form`
- Name: crm.lead.view.form.inherit.website.crm
- Model: `crm.lead`
- Type: inferred from arch
- Inherits: `crm.crm_lead_view_form`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `visitor_page_count`
- Buttons: `action_redirect_to_page_views`
- XPath or positional patches: 1

## Actions

- `crm_lead_action_from_visitor`: `act_window` Leads

## Navigation

- **Parent:** [[docs/Community Addons/website_crm/Views]]

