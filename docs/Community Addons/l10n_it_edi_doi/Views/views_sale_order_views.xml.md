<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/sale_order_views.xml

- Module: [[docs/Community Addons/l10n_it_edi_doi/l10n_it_edi_doi|l10n_it_edi_doi]]
- Scope: Community Addons
- Source file: `views/sale_order_views.xml`
- Views: 3
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `view_order_form`
- Name: sale.order.form
- Model: `sale.order`
- Type: inferred from arch
- Inherits: `sale.view_order_form`
- Root tag: `div`
- Field references: 3
- Sample fields: `l10n_it_edi_doi_id`, `l10n_it_edi_doi_use`, `l10n_it_edi_doi_warning`
- Buttons: `action_open_declaration_of_intent`
- XPath or positional patches: 3

### `view_quotation_tree`
- Name: sale.order.list
- Model: `sale.order`
- Type: inferred from arch
- Root tag: `list`
- Field references: 6
- Sample fields: `currency_id`, `date_order`, `l10n_it_edi_doi_not_yet_invoiced`, `name`, `partner_id`, `state`
- XPath or positional patches: 0

### `view_sales_order_filter`
- Name: sale.order.list.select
- Model: `sale.order`
- Type: inferred from arch
- Inherits: `sale.view_sales_order_filter`
- Root tag: `filter`
- Field references: 0
- XPath or positional patches: 2

## Navigation

- **Parent:** [[docs/Community Addons/l10n_it_edi_doi/Views]]

<!-- GENERATED:VIEWFILE -->
