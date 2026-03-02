<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/slide_channel_views.xml

- Module: [[docs/Community Addons/mass_mailing_slides/mass_mailing_slides|mass_mailing_slides]]
- Scope: Community Addons
- Source file: `views/slide_channel_views.xml`
- Views: 2
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `slide_channel_view_kanban`
- Name: slide.channel.view.kanban.inherit.mass.mailing
- Model: `slide.channel`
- Type: inferred from arch
- Inherits: `website_slides.slide_channel_view_kanban`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

### `slide_channel_view_form`
- Name: slide.channel.view.form.inherit.mass.mailing
- Model: `slide.channel`
- Type: inferred from arch
- Inherits: `website_slides.view_slide_channel_form`
- Root tag: `button`
- Field references: 1
- Sample fields: `members_count`
- Buttons: `action_channel_enroll`, `action_mass_mailing_attendees`
- XPath or positional patches: 0

## Navigation

- **Parent:** [[docs/Community Addons/mass_mailing_slides/Views]]

<!-- GENERATED:VIEWFILE -->
