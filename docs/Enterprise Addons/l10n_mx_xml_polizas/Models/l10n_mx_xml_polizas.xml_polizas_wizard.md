<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# l10n_mx_xml_polizas.xml_polizas_wizard

- Module: [[docs/Enterprise Addons/l10n_mx_xml_polizas/l10n_mx_xml_polizas|l10n_mx_xml_polizas]]
- Scope: Enterprise Addons
- Defined in module: yes
- Source files: `wizard/xml_polizas_wizard.py`
- Python classes: `L10n_Mx_Xml_PolizasXml_Polizas_Wizard`
- Description: Wizard for the XML Polizas export of Journal Entries

## Field footprint

- Detected fields: 9
- Field types: `Binary` x 1, `Boolean` x 3, `Char` x 4, `Selection` x 1
- Relation fields: 0

## Sample fields

- `export_type`: `Selection`
- `filter_all_entries`: `Boolean` (compute `_compute_filter_all_entries`)
- `filter_partial_journals`: `Boolean` (compute `_compute_filter_partial_journals`)
- `filter_partial_month`: `Boolean` (compute `_compute_filter_partial_month`)
- `mimetype`: `Char`
- `order_number`: `Char`
- `process_number`: `Char`
- `report_data`: `Binary` (comodel `Report file`)
- `report_filename`: `Char`

## Method hints

- Detected methods: 12
- Action methods: none
- Compute methods: `_compute_filter_all_entries`, `_compute_filter_partial_journals`, `_compute_filter_partial_month`
- Onchange methods: `_onchange_export_type`

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_mx_xml_polizas/Models]]

<!-- GENERATED:MODEL -->
