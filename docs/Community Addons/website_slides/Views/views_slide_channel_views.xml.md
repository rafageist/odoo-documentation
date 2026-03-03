---
tags: [odoo, community, generated, views]
---

# views/slide_channel_views.xml

- Module: [[docs/Community Addons/website_slides/website_slides|website_slides]]
- Scope: Community Addons
- Source file: `views/slide_channel_views.xml`
- Views: 7
- Actions: 6
- Menus: 0
- Rules: 0

## View records

### `slide_channel_view_kanban`
- Name: slide.channel.view.kanban
- Model: `slide.channel`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 13
- Sample fields: `color`, `members_all_count`, `members_completed_count`, `members_engaged_count`, `members_invited_count`, `name`, `rating_avg_stars`, `rating_count`, `tag_ids`, `total_slides`, and 3 more
- Buttons: `open_website_url`
- XPath or positional patches: 0

### `slide_channel_view_pivot`
- Name: slide.channel.view.pivot
- Model: `slide.channel`
- Type: inferred from arch
- Root tag: `pivot`
- Field references: 8
- Sample fields: `color`, `karma_gen_channel_finish`, `karma_gen_channel_rank`, `karma_review`, `karma_slide_comment`, `name`, `sequence`, `total_views`
- XPath or positional patches: 0

### `slide_channel_view_graph`
- Name: slide.channel.view.graph
- Model: `slide.channel`
- Type: inferred from arch
- Root tag: `graph`
- Field references: 8
- Sample fields: `color`, `karma_gen_channel_finish`, `karma_gen_channel_rank`, `karma_review`, `karma_slide_comment`, `name`, `sequence`, `total_views`
- XPath or positional patches: 0

### `slide_channel_view_search`
- Name: slide.channel.view.search
- Model: `slide.channel`
- Type: inferred from arch
- Root tag: `search`
- Field references: 4
- Sample fields: `name`, `slide_ids`, `tag_ids`, `user_id`
- XPath or positional patches: 0

### `slide_channel_view_tree_report`
- Name: slide.channel.view.list.report
- Model: `slide.channel`
- Type: inferred from arch
- Root tag: `list`
- Field references: 7
- Sample fields: `members_completed_count`, `members_count`, `name`, `rating_avg_stars`, `total_time`, `total_views`, `user_id`
- XPath or positional patches: 0

### `slide_channel_view_tree`
- Name: slide.channel.view.list
- Model: `slide.channel`
- Type: inferred from arch
- Root tag: `list`
- Field references: 9
- Sample fields: `active`, `channel_type`, `enroll`, `is_published`, `name`, `sequence`, `user_id`, `visibility`, `website_id`
- XPath or positional patches: 0

### `view_slide_channel_form`
- Name: slide.channel.view.form
- Model: `slide.channel`
- Type: inferred from arch
- Root tag: `form`
- Field references: 42
- Sample fields: `active`, `allow_comment`, `channel_type`, `completed_template_id`, `completion_time`, `description`, `enroll`, `enroll_group_ids`, `enroll_msg`, `image_1920`, and 32 more
- Buttons: `action_channel_enroll`, `action_channel_invite`, `action_redirect_to_completed_members`, `action_redirect_to_members`, `action_view_ratings`, `action_view_slides`
- XPath or positional patches: 0

## Actions

- `slide_channel_action_report_view_form`: `view`
- `slide_channel_action_report_view_pivot`: `view`
- `slide_channel_action_report_view_graph`: `view`
- `slide_channel_action_report_view_tree`: `view`
- `slide_channel_action_report`: `act_window` Courses
- `slide_channel_action_overview`: `act_window` All Courses

## Navigation

- **Parent:** [[docs/Community Addons/website_slides/Views]]

