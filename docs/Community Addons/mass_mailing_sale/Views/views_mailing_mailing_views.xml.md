---
tags: [odoo, community, generated, views]
---

# views/mailing_mailing_views.xml

- Module: [[docs/Community Addons/mass_mailing_sale/mass_mailing_sale|mass_mailing_sale]]
- Scope: Community Addons
- Source file: `views/mailing_mailing_views.xml`
- Views: 1
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `mailing_mailing_view_form`
- Name: mailing.mailing.view.form.inherit.sale
- Model: `mailing.mailing`
- Type: inferred from arch
- Inherits: `mass_mailing.view_mail_mass_mailing_form`
- Root tag: `xpath`
- Field references: 2
- Sample fields: `sale_invoiced_amount`, `sale_quotation_count`
- Buttons: `action_redirect_to_invoiced`, `action_redirect_to_quotations`
- XPath or positional patches: 1

## Navigation

- **Parent:** [[docs/Community Addons/mass_mailing_sale/Views]]

