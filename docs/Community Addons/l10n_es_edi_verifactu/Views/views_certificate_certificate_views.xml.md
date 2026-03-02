<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/certificate_certificate_views.xml

- Module: [[docs/Community Addons/l10n_es_edi_verifactu/l10n_es_edi_verifactu|l10n_es_edi_verifactu]]
- Scope: Community Addons
- Source file: `views/certificate_certificate_views.xml`
- Views: 2
- Actions: 1
- Menus: 2
- Rules: 0

## View records

### `certificate_certificate_view_form`
- Name: certificate_certificate_view_form.inherit.l10n_es_edi_verifactu
- Model: `certificate.certificate`
- Type: inferred from arch
- Inherits: `certificate.certificate_certificate_view_form`
- Root tag: `field`
- Field references: 1
- Sample fields: `scope`
- XPath or positional patches: 0

### `certificate_certificate_view_search`
- Name: certificate_certificate_view_search.inherit.l10n_es_edi_verifactu
- Model: `certificate.certificate`
- Type: inferred from arch
- Inherits: `certificate.certificate_certificate_view_search`
- Root tag: `filter`
- Field references: 0
- XPath or positional patches: 1

## Actions

- `l10n_es_edi_verifactu_certificate_action`: `act_window` Certificates for Veri*Factu

## Menus

- `menu_l10n_es_edi_verifactu_root`: Veri*Factu (Spain)
- `menu_l10n_es_edi_verifactu_certificates`: Certificates

## Navigation

- **Parent:** [[docs/Community Addons/l10n_es_edi_verifactu/Views]]

<!-- GENERATED:VIEWFILE -->
