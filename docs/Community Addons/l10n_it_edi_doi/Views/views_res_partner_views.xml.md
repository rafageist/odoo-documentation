<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/res_partner_views.xml

- Module: [[docs/Community Addons/l10n_it_edi_doi/l10n_it_edi_doi|l10n_it_edi_doi]]
- Scope: Community Addons
- Source file: `views/res_partner_views.xml`
- Views: 2
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `view_partner_l10n_form`
- Name: view_partner_l10n_form
- Model: `res.partner`
- Type: inferred from arch
- Inherits: `base_vat.view_partner_base_vat_form`
- Root tag: `div`
- Field references: 0
- Buttons: `l10n_it_edi_doi_action_open_declarations`
- XPath or positional patches: 1

### `res_partner_view_search`
- Name: res.partner.search.inherit
- Model: `res.partner`
- Type: inferred from arch
- Inherits: `account.res_partner_view_search`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

## Navigation

- **Parent:** [[docs/Community Addons/l10n_it_edi_doi/Views]]

<!-- GENERATED:VIEWFILE -->
