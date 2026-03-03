---
tags: [odoo, enterprise, generated, views]
---

# views/res_company_views.xml

- Module: [[docs/Enterprise Addons/l10n_de_pos_cert/l10n_de_pos_cert|l10n_de_pos_cert]]
- Scope: Enterprise Addons
- Source file: `views/res_company_views.xml`
- Views: 1
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `view_company_form`
- Name: res.company.form.inherit.account
- Model: `res.company`
- Type: inferred from arch
- Inherits: `base.view_company_form`
- Root tag: `page`
- Field references: 4
- Sample fields: `is_country_germany`, `l10n_de_fiskaly_api_key`, `l10n_de_fiskaly_api_secret`, `l10n_de_fiskaly_organization_id`
- Buttons: `l10n_de_action_fiskaly_create_new_keys`, `l10n_de_action_fiskaly_register`
- XPath or positional patches: 1

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_de_pos_cert/Views]]

