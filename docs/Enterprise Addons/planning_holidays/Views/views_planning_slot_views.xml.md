<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/planning_slot_views.xml

- Module: [[docs/Enterprise Addons/planning_holidays/planning_holidays|planning_holidays]]
- Scope: Enterprise Addons
- Source file: `views/planning_slot_views.xml`
- Views: 4
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `planning_slot_view_search_inherit_planning_holidays`
- Name: planning.slot.search.inherit.planning_holidays
- Model: `planning.slot`
- Type: inferred from arch
- Inherits: `planning.planning_view_search_base`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

### `planning_slot_view_gantt`
- Name: planning.slot.view.gantt
- Model: `planning.slot`
- Type: inferred from arch
- Inherits: `planning.planning_view_gantt`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

### `planning_view_kanban_inherit_planning_holidays`
- Name: planning.slot.kanban
- Model: `planning.slot`
- Type: inferred from arch
- Inherits: `planning.planning_view_kanban_inherit`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `leave_warning`
- XPath or positional patches: 1

### `planning_slot_view_form`
- Name: planning.slot.view.form
- Model: `planning.slot`
- Type: inferred from arch
- Inherits: `planning.planning_view_form`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `leave_warning`
- XPath or positional patches: 3

## Navigation

- **Parent:** [[docs/Enterprise Addons/planning_holidays/Views]]

<!-- GENERATED:VIEWFILE -->
