<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/slide_channel_views.xml

- Module: [[docs/Community Addons/website_sale_slides/website_sale_slides|website_sale_slides]]
- Scope: Community Addons
- Source file: `views/slide_channel_views.xml`
- Views: 4
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `slide_channel_view_form_add_inherit_sale_slides`
- Name: slide.channel.view.form.add.inherit.sale.slides
- Model: `slide.channel`
- Type: inferred from arch
- Inherits: `website_slides.slide_channel_view_form_add`
- Root tag: `xpath`
- Field references: 2
- Sample fields: `enroll`, `product_id`
- XPath or positional patches: 1

### `slide_channel_view_kanban`
- Name: slide.channel.view.kanban.inherit.sale
- Model: `slide.channel`
- Type: inferred from arch
- Inherits: `website_slides.slide_channel_view_kanban`
- Root tag: `xpath`
- Field references: 2
- Sample fields: `currency_id`, `product_sale_revenues`
- XPath or positional patches: 1

### `slide_channel_view_tree_report`
- Name: slide.channel.view.list.report.inherit.sale_slides
- Model: `slide.channel`
- Type: inferred from arch
- Inherits: `website_slides.slide_channel_view_tree_report`
- Root tag: `field`
- Field references: 3
- Sample fields: `currency_id`, `members_completed_count`, `product_sale_revenues`
- XPath or positional patches: 0

### `slide_channel_view_form`
- Name: slide.channel.view.form.inherit.sale
- Model: `slide.channel`
- Type: inferred from arch
- Inherits: `website_slides.view_slide_channel_form`
- Root tag: `xpath`
- Field references: 2
- Sample fields: `product_id`, `product_sale_revenues`
- Buttons: `action_view_sales`
- XPath or positional patches: 2

## Navigation

- **Parent:** [[docs/Community Addons/website_sale_slides/Views]]

<!-- GENERATED:VIEWFILE -->
