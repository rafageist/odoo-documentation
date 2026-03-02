<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/certificate_views.xml

- Module: [[docs/Community Addons/certificate/certificate|certificate]]
- Scope: Community Addons
- Source file: `views/certificate_views.xml`
- Views: 3
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `certificate_certificate_view_search`
- Name: certificate.certificate.search
- Model: `certificate.certificate`
- Type: inferred from arch
- Root tag: `search`
- Field references: 2
- Sample fields: `name`, `scope`
- XPath or positional patches: 0

### `certificate_certificate_view_list`
- Name: certificate.certificate.list
- Model: `certificate.certificate`
- Type: inferred from arch
- Root tag: `list`
- Field references: 4
- Sample fields: `company_id`, `is_valid`, `name`, `subject_common_name`
- XPath or positional patches: 0

### `certificate_certificate_view_form`
- Name: certificate.certificate.form
- Model: `certificate.certificate`
- Type: inferred from arch
- Root tag: `form`
- Field references: 12
- Sample fields: `company_id`, `content`, `date_end`, `date_start`, `loading_error`, `name`, `pkcs12_password`, `private_key_id`, `public_key_id`, `scope`, and 2 more
- XPath or positional patches: 0

## Navigation

- **Parent:** [[docs/Community Addons/certificate/Views]]

<!-- GENERATED:VIEWFILE -->
