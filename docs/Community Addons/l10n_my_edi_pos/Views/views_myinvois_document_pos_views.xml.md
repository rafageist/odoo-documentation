<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/myinvois_document_pos_views.xml

- Module: [[docs/Community Addons/l10n_my_edi_pos/l10n_my_edi_pos|l10n_my_edi_pos]]
- Scope: Community Addons
- Source file: `views/myinvois_document_pos_views.xml`
- Views: 2
- Actions: 1
- Menus: 1
- Rules: 0

## View records

### `myinvois_document_pos_list_view`
- Name: myinvois.document.list.view
- Model: `myinvois.document`
- Type: inferred from arch
- Inherits: `l10n_my_edi.myinvois_document_list_view`
- Root tag: `header`
- Field references: 3
- Sample fields: `myinvois_state`, `pos_config_id`, `pos_order_date_range`
- Buttons: `action_open_consolidate_invoice_wizard`
- XPath or positional patches: 1

### `myinvois_document_pos_form_view`
- Name: myinvois.document.pos.form.view
- Model: `myinvois.document`
- Type: inferred from arch
- Inherits: `l10n_my_edi.myinvois_document_form_view`
- Root tag: `div`
- Field references: 4
- Sample fields: `linked_order_count`, `myinvois_issuance_date`, `pos_config_id`, `pos_order_date_range`
- Buttons: `action_view_linked_orders`
- XPath or positional patches: 1

## Actions

- `action_consolidated_invoices`: `act_window` Consolidated Invoices

## Menus

- `l10n_my_edi_pos.menu_consolidated_invoices`: Consolidated Invoice

## Navigation

- **Parent:** [[docs/Community Addons/l10n_my_edi_pos/Views]]

<!-- GENERATED:VIEWFILE -->
