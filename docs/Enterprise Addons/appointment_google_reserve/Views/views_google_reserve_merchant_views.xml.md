---
tags: [odoo, enterprise, generated, views]
---

# views/google_reserve_merchant_views.xml

- Module: [[docs/Enterprise Addons/appointment_google_reserve/appointment_google_reserve|appointment_google_reserve]]
- Scope: Enterprise Addons
- Source file: `views/google_reserve_merchant_views.xml`
- Views: 2
- Actions: 1
- Menus: 1
- Rules: 0

## View records

### `google_reserve_merchant_view_form`
- Name: google.reserve.merchant.view.form
- Model: `google.reserve.merchant`
- Type: inferred from arch
- Root tag: `form`
- Field references: 5
- Sample fields: `business_category`, `location_id`, `name`, `phone`, `website_url`
- XPath or positional patches: 0

### `google_reserve_merchant_view_list`
- Name: google.reserve.merchant.view.list
- Model: `google.reserve.merchant`
- Type: inferred from arch
- Root tag: `list`
- Field references: 5
- Sample fields: `business_category`, `location_id`, `name`, `phone`, `website_url`
- XPath or positional patches: 0

## Actions

- `google_reserve_merchant_action`: `act_window` Google Reserve Merchants

## Menus

- `menu_appointment_google_reserve_merchants`: Google Reserve

## Navigation

- **Parent:** [[docs/Enterprise Addons/appointment_google_reserve/Views]]

