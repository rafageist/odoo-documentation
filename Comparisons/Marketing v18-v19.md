---
tags: [comparison, marketing]
status: draft
---
# Marketing v18 vs v19

> **Summary:** Tracks the email/marketing stack changes between v18 and v19. Baseline references: `[[Odoo 18/Community Addons/Marketing/Marketing]]`.

## Key observations so far
- Email marketing merges into the core `mailing` module; mass mailing models live under `addons/mailing` and `message_type`/queue APIs align with the generic mail stack.
- Mailing batches adopt the new Domain helpers and leverage mail server ownership checks (`_check_mail_server_id`), improving multi-user safety.
- Queue processing signatures change (`process_email_queue(email_ids=...)`) and progress commits run via cron-aware `_commit_progress`.
- Notification post-processing distinguishes partner successes from raw email successes, reducing false failures.
- Spam detection adds `mail_spam` states; unrestricted attachments now reuse `_filtered_access('read')` instead of legacy access filters.

## Migration hints
- Update custom overrides of `process_email_queue`/`send` to accept keyword-only `email_ids` and use `modules.module.current_test` instead of `threading.testing`.
- Replace direct tuple domains with `Domain` when filtering mailings or notifications.
- Ensure custom forms or controllers respect the mail server ownership constraint when assigning `mail_server_id`.
- Switch UI integrations to the renamed module and adjust import paths (`from odoo.addons.mailing...`).

## Next steps
- Diff marketing automation flows (`marketing_automation`) once the v19 modules are imported.
- Document website/CRM opt-in changes as we analyse frontend modules.
- Capture enterprise-specific additions (SMS, surveys) after community stack is settled.

## Navigation
- **Parent:** [[Comparisons/Comparisons]]
