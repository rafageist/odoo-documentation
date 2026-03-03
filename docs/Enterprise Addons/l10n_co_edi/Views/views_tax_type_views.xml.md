---
tags: [odoo, enterprise, generated, views]
---

# views/tax_type_views.xml

- Module: [[docs/Enterprise Addons/l10n_co_edi/l10n_co_edi|l10n_co_edi]]
- Scope: Enterprise Addons
- Source file: `views/tax_type_views.xml`
- Views: 2
- Actions: 1
- Menus: 1
- Rules: 0

## View records

### `tax_type_view_form`
- Name: account.type.form
- Model: `l10n_co_edi.tax.type`
- Type: inferred from arch
- Root tag: `form`
- Field references: 3
- Sample fields: `code`, `name`, `retention`
- XPath or positional patches: 0

### `tax_type_view_tree`
- Name: account.type.list
- Model: `l10n_co_edi.tax.type`
- Type: inferred from arch
- Root tag: `list`
- Field references: 3
- Sample fields: `code`, `name`, `retention`
- XPath or positional patches: 0

## Actions

- `action_tax_type`: `act_window` Tipo de Valor en Factura

## Menus

- `tax_type_menu`: Tipo de Valor en Factura

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_co_edi/Views]]

