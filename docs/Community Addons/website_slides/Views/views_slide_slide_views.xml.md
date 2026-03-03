---
tags: [odoo, community, generated, views]
---

# views/slide_slide_views.xml

- Module: [[docs/Community Addons/website_slides/website_slides|website_slides]]
- Scope: Community Addons
- Source file: `views/slide_slide_views.xml`
- Views: 10
- Actions: 7
- Menus: 0
- Rules: 0

## View records

### `slide_slide_view_pivot`
- Name: slide.slide.view.pivot
- Model: `slide.slide`
- Type: inferred from arch
- Root tag: `pivot`
- Field references: 2
- Sample fields: `channel_id`, `total_views`
- XPath or positional patches: 0

### `slide_slide_view_graph`
- Name: slide.slide.view.graph
- Model: `slide.slide`
- Type: inferred from arch
- Root tag: `graph`
- Field references: 8
- Sample fields: `channel_id`, `quiz_first_attempt_reward`, `quiz_fourth_attempt_reward`, `quiz_second_attempt_reward`, `quiz_third_attempt_reward`, `sequence`, `slide_category`, `total_views`
- XPath or positional patches: 0

### `view_slide_slide_search`
- Name: slide.slide.filter
- Model: `slide.slide`
- Type: inferred from arch
- Root tag: `search`
- Field references: 4
- Sample fields: `channel_id`, `name`, `tag_ids`, `user_id`
- XPath or positional patches: 0

### `slide_slide_view_tree_report`
- Name: slide.slide.view.list.report
- Model: `slide.slide`
- Type: inferred from arch
- Root tag: `list`
- Field references: 8
- Sample fields: `category_id`, `channel_id`, `completion_time`, `date_published`, `name`, `questions_count`, `total_views`, `user_id`
- XPath or positional patches: 0

### `view_slide_slide_tree`
- Name: slide.slide.list
- Model: `slide.slide`
- Type: inferred from arch
- Root tag: `list`
- Field references: 7
- Sample fields: `category_id`, `channel_id`, `completion_time`, `date_published`, `is_published`, `name`, `user_id`
- XPath or positional patches: 0

### `slide_slide_view_kanban`
- Name: slide.slide.view.kanban
- Model: `slide.slide`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 9
- Sample fields: `channel_id`, `completion_time`, `image_128`, `name`, `questions_count`, `slide_category`, `tag_ids`, `total_views`, `user_id`
- XPath or positional patches: 0

### `view_slide_slide_form_wo_channel_id`
- Name: slide.slide.form.wo.channel_id
- Model: `slide.slide`
- Type: inferred from arch
- Inherits: `view_slide_slide_form`
- Root tag: `field`
- Field references: 1
- Sample fields: `channel_id`
- XPath or positional patches: 0

### `view_slide_slide_form`
- Name: slide.slide.form
- Model: `slide.slide`
- Type: inferred from arch
- Root tag: `form`
- Field references: 43
- Sample fields: `active`, `answer_ids`, `channel_allow_comment`, `channel_id`, `channel_type`, `comments_count`, `completion_time`, `data`, `date_published`, `description`, and 33 more
- Buttons: `%(slide_slide_partner_action_from_slide)d`, `action_view_embeds`
- XPath or positional patches: 0

### `view_slide_tag_tree`
- Name: slide.tag.list
- Model: `slide.tag`
- Type: inferred from arch
- Root tag: `list`
- Field references: 1
- Sample fields: `name`
- XPath or positional patches: 0

### `view_slide_tag_form`
- Name: slide.tag.form
- Model: `slide.tag`
- Type: inferred from arch
- Root tag: `form`
- Field references: 1
- Sample fields: `name`
- XPath or positional patches: 0

## Actions

- `slide_slide_action_report_view_pivot`: `view`
- `slide_slide_action_report_view_form`: `view`
- `slide_slide_action_report_view_tree`: `view`
- `slide_slide_action_report_view_graph`: `view`
- `slide_slide_action_report`: `act_window` Contents
- `slide_slide_action`: `act_window` Contents
- `action_slide_tag`: `act_window` Content Tags

## Navigation

- **Parent:** [[docs/Community Addons/website_slides/Views]]

