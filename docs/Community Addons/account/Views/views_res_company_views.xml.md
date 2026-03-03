<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/res_company_views.xml

- Module: [[docs/Community Addons/account/account|account]]
- Scope: Community Addons
- Source file: `views/res_company_views.xml`
- Views: 4
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `res_company_form_view_onboarding_sale_tax`
- Name: res.company.form.view.onboarding.sale.tax
- Model: `res.company`
- Type: inferred from arch
- Root tag: `form`
- Field references: 1
- Sample fields: `account_sale_tax_id`
- Buttons: `action_save_onboarding_sale_tax`
- XPath or positional patches: 0

### `res_company_form_view_onboarding`
- Name: res.company.form.view.onboarding
- Model: `res.company`
- Type: inferred from arch
- Root tag: `form`
- Field references: 14
- Sample fields: `city`, `company_registry`, `country_id`, `currency_id`, `email`, `logo`, `name`, `phone`, `state_id`, `street`, and 4 more
- Buttons: `action_save_onboarding_company_data`
- XPath or positional patches: 0

### `res_company_view_form_terms`
- Name: res.company.view.form.terms
- Model: `res.company`
- Type: inferred from arch
- Root tag: `form`
- Field references: 1
- Sample fields: `invoice_terms_html`
- XPath or positional patches: 0

### `view_company_form`
- Name: res.company.form.inherit.account
- Model: `res.company`
- Type: inferred from arch
- Inherits: `base.view_company_form`
- Root tag: `xpath`
- Field references: 5
- Sample fields: `account_enabled_tax_country_ids`, `company_registry`, `company_registry_placeholder`, `company_vat_placeholder`, `vat`
- XPath or positional patches: 2

## Navigation

- **Parent:** [[docs/Community Addons/account/Views]]

<!-- GENERATED:VIEWFILE -->
