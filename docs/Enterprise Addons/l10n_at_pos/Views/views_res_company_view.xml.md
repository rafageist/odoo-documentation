<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/res_company_view.xml

- Module: [[docs/Enterprise Addons/l10n_at_pos/l10n_at_pos|l10n_at_pos]]
- Scope: Enterprise Addons
- Source file: `views/res_company_view.xml`
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
- Field references: 9
- Sample fields: `currency_id`, `l10n_at_fiskaly_api_key`, `l10n_at_fiskaly_api_secret`, `l10n_at_fon_participant_id`, `l10n_at_fon_user_id`, `l10n_at_fon_user_pin`, `l10n_at_is_odoo_managed_org`, `l10n_at_pos_is_tax_exempted`, `l10n_at_pos_test_mode`
- Buttons: `action_auth_fiskaly_credentials`, `action_generate_fiskaly_credentials`, `action_l10n_at_authenticate_fon_credentials`
- XPath or positional patches: 2

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_at_pos/Views]]

<!-- GENERATED:VIEWFILE -->
