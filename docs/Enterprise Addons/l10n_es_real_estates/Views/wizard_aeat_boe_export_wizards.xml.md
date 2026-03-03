---
tags: [odoo, enterprise, generated, views]
---

# wizard/aeat_boe_export_wizards.xml

- Module: [[docs/Enterprise Addons/l10n_es_real_estates/l10n_es_real_estates|l10n_es_real_estates]]
- Scope: Enterprise Addons
- Source file: `wizard/aeat_boe_export_wizards.xml`
- Views: 2
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `mod347_inmuebles_vat_tree`
- Name: l10n_es_reports.aeat.boe.mod347.real.estates.vat.list
- Model: `l10n_es_reports.aeat.mod347.real.estates.vat`
- Type: inferred from arch
- Inherits: `l10n_es_reports.mod347_manual_partner_data_tree`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `trimester`
- XPath or positional patches: 1

### `mod347_boe_wizard`
- Name: l10n_es_real_estates.aeat.boe.mod347.export.wizard.form
- Model: `l10n_es_reports.aeat.boe.mod347.export.wizard`
- Type: inferred from arch
- Inherits: `l10n_es_reports.mod347_boe_wizard`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `real_estates_vat_mod347_data`
- XPath or positional patches: 1

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_es_real_estates/Views]]

