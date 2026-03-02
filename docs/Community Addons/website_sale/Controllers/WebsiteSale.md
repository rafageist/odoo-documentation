<!-- GENERATED:CONTROLLER -->
---
tags: [odoo, community, generated, controller]
---

# WebsiteSale

- Module: [[docs/Community Addons/website_sale/website_sale|website_sale]]
- Scope: Community Addons
- Source file: `controllers/main.py`
- Base classes: `payment_portal.PaymentPortal`
- Routes: 28

## Routes

### `shop`
- Paths: `<dynamic>`
- Type: `http`
- Auth: `public`
- Website route: `True`

### `product`
- Paths: `<dynamic>`
- Type: `http`
- Auth: `public`
- Website route: `True`

### `product_document`
- Paths: `/shop/<model("product.template"):product_template>/document/<int:document_id>`
- Type: `http`
- Auth: `public`
- Website route: `True`
- Readonly: `True`

### `old_product`
- Paths: `<dynamic>`
- Type: `http`
- Auth: `public`
- Website route: `True`

### `add_product_media`
- Paths: `/shop/product/extra-media`
- Type: `jsonrpc`
- Auth: `user`
- Website route: `True`

### `clear_product_images`
- Paths: `/shop/product/clear-images`
- Type: `jsonrpc`
- Auth: `user`
- Website route: `True`

### `resequence_product_image`
- Paths: `/shop/product/resequence-image`
- Type: `jsonrpc`
- Auth: `user`
- Website route: `True`

### `is_add_to_cart_allowed`
- Paths: `/shop/product/is_add_to_cart_allowed`
- Type: `jsonrpc`
- Auth: `public`
- Website route: `True`
- Readonly: `True`

### `pricelist_change`
- Paths: `/shop/change_pricelist/<model("product.pricelist"):pricelist>`
- Type: `http`
- Auth: `public`
- Website route: `True`

### `pricelist`
- Paths: `/shop/pricelist`
- Type: `http`
- Auth: `public`
- Website route: `True`

### `save_shop_layout_mode`
- Paths: `/shop/save_shop_layout_mode`
- Type: `jsonrpc`
- Auth: `public`
- Website route: `True`

### `shop_checkout`
- Paths: `/shop/checkout`
- Type: `http`
- Auth: `public`
- Website route: `True`

### `shop_address`
- Paths: `/shop/address`
- Type: `http`
- Auth: `public`
- Website route: `True`

### `shop_address_submit`
- Paths: `/shop/address/submit`
- Type: `http`
- Auth: `public`
- Website route: `True`

### `process_express_checkout`
- Paths: `<dynamic>`
- Type: `jsonrpc`
- Auth: `public`
- Website route: `True`

### `shop_update_address`
- Paths: `/shop/update_address`
- Type: `jsonrpc`
- Auth: `public`
- Website route: `True`

### `extra_info`
- Paths: `/shop/extra_info`
- Type: `http`
- Auth: `public`
- Website route: `True`

### `shop_payment`
- Paths: `/shop/payment`
- Type: `http`
- Auth: `public`
- Website route: `True`

### `shop_payment_validate`
- Paths: `/shop/payment/validate`
- Type: `http`
- Auth: `public`
- Website route: `True`

### `shop_payment_confirmation`
- Paths: `/shop/confirmation`
- Type: `http`
- Auth: `public`
- Website route: `True`

### `print_saleorder`
- Paths: `/shop/print`
- Type: `http`
- Auth: `public`
- Website route: `True`

### `change_product_config`
- Paths: `/shop/config/product`
- Type: `jsonrpc`
- Auth: `user`

### `change_attribute_config`
- Paths: `/shop/config/attribute`
- Type: `jsonrpc`
- Auth: `user`

### `_change_website_config`
- Paths: `/shop/config/website`
- Type: `jsonrpc`
- Auth: `user`

### `_change_category_config`
- Paths: `/shop/config/category`
- Type: `jsonrpc`
- Auth: `user`

### `products_recently_viewed_update`
- Paths: `/shop/products/recently_viewed_update`
- Type: `jsonrpc`
- Auth: `public`
- Website route: `True`

### `products_recently_viewed_delete`
- Paths: `/shop/products/recently_viewed_delete`
- Type: `jsonrpc`
- Auth: `public`
- Website route: `True`

### `set_category_image`
- Paths: `/snippets/category/set_image`
- Type: `jsonrpc`
- Auth: `user`

## Navigation

- **Parent:** [[docs/Community Addons/website_sale/Controllers]]

<!-- GENERATED:CONTROLLER -->
