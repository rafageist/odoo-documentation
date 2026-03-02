---
tags: [odoo, glossary, business]
status: active
---

# Activity

## Definition
- An activity is a scheduled follow-up action assigned to a user, usually with a deadline, a type, and a target record.
- In business language, it is how Odoo tracks "next actions" such as calls, meetings, reminders, or review tasks.

## Why developers should care
- Activities are often the operational glue between modules: CRM, Sales, Helpdesk, Project, Documents, and custom workflows all use them.
- Requirements that mention reminders, follow-ups, or next steps usually map to activity logic rather than to custom status fields.

## Technical anchors
- Main model family: `mail.activity` and `mail.activity.mixin`
- Related note: `[[docs/Community Addons/mail/mail|mail]]`
- Related framework note: `[[docs/Core/Framework/mail]]`

## Related terms
- `[[docs/Glossary/Lead]]`
- `[[docs/Glossary/Opportunity]]`
- `[[docs/Glossary/Picking]]`

## Navigation
- **Parent:** [[docs/Glossary/Glossary]]
