---
tags: [odoo, community, generated, views]
---

# views/res_partner_views.xml

- Module: [[docs/Community Addons/survey/survey|survey]]
- Scope: Community Addons
- Source file: `views/res_partner_views.xml`
- Views: 1
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `res_partner_view_form`
- Name: res.partner.view.form.inherit.survey
- Model: `res.partner`
- Type: inferred from arch
- Inherits: `base.view_partner_form`
- Root tag: `xpath`
- Field references: 2
- Sample fields: `certifications_company_count`, `certifications_count`
- Buttons: `action_view_certifications`
- XPath or positional patches: 1

## Actions

- `res_partner_action_certifications`: `act_window` Certifications Succeeded

## Navigation

- **Parent:** [[docs/Community Addons/survey/Views]]

