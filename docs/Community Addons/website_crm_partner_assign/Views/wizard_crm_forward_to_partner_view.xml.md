<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# wizard/crm_forward_to_partner_view.xml

- Module: [[docs/Community Addons/website_crm_partner_assign/website_crm_partner_assign|website_crm_partner_assign]]
- Scope: Community Addons
- Source file: `wizard/crm_forward_to_partner_view.xml`
- Views: 1
- Actions: 2
- Menus: 0
- Rules: 0

## View records

### `crm_lead_forward_to_partner_form`
- Name: crm_lead_forward_to_partner
- Model: `crm.lead.forward.to.partner`
- Type: inferred from arch
- Root tag: `form`
- Field references: 9
- Sample fields: `assignation_lines`, `body`, `forward_type`, `lead_id`, `lead_link`, `lead_location`, `partner_assigned_id`, `partner_id`, `partner_location`
- Buttons: `action_forward`
- XPath or positional patches: 0

## Actions

- `action_crm_send_mass_forward`: `act_window` Forward to partner
- `crm_lead_forward_to_partner_act`: `act_window` Forward to Partner

## Navigation

- **Parent:** [[docs/Community Addons/website_crm_partner_assign/Views]]

<!-- GENERATED:VIEWFILE -->
