<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, enterprise, module]
---

# Indian - GSTR Document Summary

- Version: v18
- Category: enterprise
- Source: enterprise18/l10n_in_reports_gstr_document_summary
- Dependencies: [[Odoo 18/Enterprise Addons/l10n_in_reports_gstr_spreadsheet/l10n_in_reports_gstr_spreadsheet|l10n_in_reports_gstr_spreadsheet]]

## Summary

GSTR Document Summary Management

## XML Artifacts (detected)

- Views: 3
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 1

## Detected Models

- `l10n_in.gstr.document.summary.line`
- `L10nInGstReturnPeriod`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Indian - GSTR Document Summary - Models and Relations
class "l10n_in.gstr.document.summary.line" as l10n_in_gstr_document_summary_line
class L10nInGstReturnPeriod
class "l10n_in.gst.return.period" as l10n_in_gst_return_period
l10n_in_gstr_document_summary_line --> l10n_in_gst_return_period : many2one
L10nInGstReturnPeriod --|> l10n_in_gstr_document_summary_line : one2many
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
