---
tags: [template, process, business, v19]
area:
version: v19
status: draft
---

# Process {{name}}

## Template usage
- Use this note for cross-module flows such as invoice validation, replenishment, or lead-to-order.
- Keep the diagram small and move implementation details to linked module or model notes.
- Optional sections can be removed when the process is simple.

## Overview
- Objective:
- Actors:
- Triggers:
- Output:

```plantuml
@startuml
title Process flow {{name}}
start
:Trigger;
:Main business step;
if (Decision?) then (Yes)
  :Branch A;
else (No)
  :Branch B;
endif
:Outcome;
stop
@enduml
```

## Modules involved
- `[[Related Module 1]]`
- `[[Related Module 2]]`

## System touchpoints
- Entry views or actions:
- Automated jobs:
- External services or file exchanges:

## Evidence
- Models:
- Views:
- Security:
- Reports:
- Automations:
- Tests:

## Operational risks
- Failure points:
- Manual workarounds:
- Audit or compliance concerns:

## Cross-links
- Parent index:
- Related process:
- Related service or model note:

## Follow-up
- Gaps in current documentation:
- Next notes to create:
