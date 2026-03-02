<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/pos_printer_views.xml

- Module: [[docs/Enterprise Addons/pos_iot/pos_iot|pos_iot]]
- Scope: Enterprise Addons
- Source file: `views/pos_printer_views.xml`
- Views: 2
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `view_pos_printer_iot_tree`
- Name: pos.iot.config.list.view
- Model: `pos.printer`
- Type: inferred from arch
- Inherits: `point_of_sale.view_pos_printer`
- Root tag: `field`
- Field references: 2
- Sample fields: `device_id`, `proxy_ip`
- XPath or positional patches: 0

### `view_pos_printer_iot_form`
- Name: pos.iot.config.form.view
- Model: `pos.printer`
- Type: inferred from arch
- Inherits: `point_of_sale.view_pos_printer_form`
- Root tag: `field`
- Field references: 2
- Sample fields: `device_id`, `proxy_ip`
- XPath or positional patches: 0

## Navigation

- **Parent:** [[docs/Enterprise Addons/pos_iot/Views]]

<!-- GENERATED:VIEWFILE -->
