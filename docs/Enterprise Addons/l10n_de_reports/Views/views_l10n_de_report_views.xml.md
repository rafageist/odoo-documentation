---
tags: [odoo, enterprise, generated, views]
---

# views/l10n_de_report_views.xml

- Module: [[docs/Enterprise Addons/l10n_de_reports/l10n_de_reports|l10n_de_reports]]
- Scope: Enterprise Addons
- Source file: `views/l10n_de_report_views.xml`
- Views: 2
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `view_partner_form_inherit`
- Name: res.partner.form.inherit.l10n_de_reports
- Model: `res.partner`
- Type: inferred from arch
- Inherits: `account.view_partner_property_form`
- Root tag: `xpath`
- Field references: 2
- Sample fields: `l10n_de_datev_identifier`, `l10n_de_datev_identifier_customer`
- XPath or positional patches: 1

### `res_company_form_l10n_de`
- Name: res.company.form.l10n.de
- Model: `res.company`
- Type: inferred from arch
- Inherits: `account.view_company_form`
- Root tag: `data`
- Field references: 2
- Sample fields: `l10n_de_datev_client_number`, `l10n_de_datev_consultant_number`
- XPath or positional patches: 1

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_de_reports/Views]]

