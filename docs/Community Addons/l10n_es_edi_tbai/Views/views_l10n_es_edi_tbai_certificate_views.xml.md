<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/l10n_es_edi_tbai_certificate_views.xml

- Module: [[docs/Community Addons/l10n_es_edi_tbai/l10n_es_edi_tbai|l10n_es_edi_tbai]]
- Scope: Community Addons
- Source file: `views/l10n_es_edi_tbai_certificate_views.xml`
- Views: 2
- Actions: 1
- Menus: 2
- Rules: 0

## View records

### `certificate_certificate_view_form`
- Name: certificate_certificate_view_form.inherit.l10n_es_edi_tbai
- Model: `certificate.certificate`
- Type: inferred from arch
- Inherits: `certificate.certificate_certificate_view_form`
- Root tag: `field`
- Field references: 1
- Sample fields: `scope`
- XPath or positional patches: 0

### `certificate_certificate_view_search`
- Name: certificate_certificate_view_search.inherit.l10n_es_edi_tbai
- Model: `certificate.certificate`
- Type: inferred from arch
- Inherits: `certificate.certificate_certificate_view_search`
- Root tag: `filter`
- Field references: 0
- XPath or positional patches: 1

## Actions

- `l10n_es_edi_tbai_certificate_action`: `act_window` Certificates for EDI TicketBAI invoices on Spain

## Menus

- `menu_l10n_es_edi_tbai_root`: Spain TicketBAI
- `menu_l10n_es_edi_tbai_certificates`: Certificates

## Navigation

- **Parent:** [[docs/Community Addons/l10n_es_edi_tbai/Views]]

<!-- GENERATED:VIEWFILE -->
