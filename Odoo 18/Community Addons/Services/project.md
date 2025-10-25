---
tags: [v18, community, services, project, analysis]
status: draft
---

# Project Module (Community)

> **Summary:** Community `project` app delivers collaborative project/task management. It complements the core process note (`[[Odoo 18/Core/Processes/Projects]]`) with module-specific features, views, and settings.

## 1. Models and structure

| Model | File | Responsibilities |
|-------|------|------------------|
| `project.project` | `addons/project/models/project.py` | Project container, manages stages, privacy, default settings, analytic account linkage.
| `project.task` | `addons/project/models/project.py` | Tasks with kanban stages, assigned users, timesheets, sub-tasks.
| `project.task.type` | `addons/project/models/project.py` | Stage definitions per project.
| `project.task.tag` | `addons/project/models/project.py` | Labels for tasks.
| Wizards (`project.task.create.timesheet`) | Create timesheets or convert issues.

## 2. Views & UI highlights
- Kanban board with drag-and-drop stage changes (`kanban_state`).
- Gantt, calendar, list and pivot views built from `project.task`.
- Activity view integrates mail activities for deadlines.
- Portal visibility: tasks shown to portal users if project privacy settings allow.

## 3. Settings & configuration
- Project settings toggles: sub-tasks, recurring tasks, timesheets, milestones.
- Default stage templates definable per project template (if template module installed).
- Security groups: `project.group_project_manager`, `project.group_project_user`.
- `privacy_visibility` controls employee/portal restrictions (`employees`, `portal`, `followers`).

## 4. Integrations
- **Sales (`sale_project`):** see `[[Odoo 18/Community Addons/Sales/sale_project.md]]` for automatic project/task creation.
- **Timesheets (`project_timesheet`):** tasks log `account.analytic.line`; needed for billing/time tracking.
- **Helpdesk:** optional modules transform tickets into tasks.
- **Documents/Sign (Enterprise)** extend projects with file management and signatures.

## 5. Automation & activities
- Activities (`mail.activity`) triggered on deadlines (config via settings).
- Recurring tasks if module enabled; generate clones on completion.
- Email gateway: project alias create tasks via incoming emails (`project.project.alias_id`).

## 6. Reporting & KPIs
- `project.task` pivot/graph: track time spent, stage counts, assignee workload.
- Burndown charts available when timesheets enabled.
- SLA-like metrics possible with stage lead times (`project.task` fields `date_assign`, `date_close`).

## 7. To-do (Issue #21)
- [ ] Describe project mail alias configuration with examples.
- [ ] Add sample analytic report for project profitability.
- [ ] Document recurring tasks once feature note exists.

## Navigation
- **Parent:** `[[Odoo 18/Community Addons/Services]]`
- **Related:** `[[Odoo 18/Core/Processes/Projects]]`, `[[Odoo 18/Community Addons/Sales/sale_project.md]]`, `[[Odoo 18/Core/Master Data/res_users.md]]`
- **Issue:** #21 `Docs: Odoo 18 - Community Services suite`
