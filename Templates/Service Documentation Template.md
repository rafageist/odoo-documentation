---
tags: [template, service, documentation, v19]
status: draft
---

# Service `{{service_name}}`

## Template usage
- Use this for controllers, cron services, import/export pipelines, or reusable service objects.
- Prefer sequence diagrams when ordering matters and a short Mermaid flowchart when branching matters.

- Module: `{{module_name}}`
- Entry point: `{{source_path}}`

## Purpose
- Trigger:
- Consumers:
- Expected outcome:

## Flow
1. Input arrives
2. Validation happens
3. Core logic executes
4. Side effects are emitted

```plantuml
@startuml
actor Caller
participant Service
participant Model
database External
Caller -> Service: request
Service -> Model: business logic
Model -> External: optional sync
External --> Model: response
Model --> Service: result
Service --> Caller: output
@enduml
```

## Dependencies
- Internal modules:
- External services:

## Observability
- Logs or chatter traces:
- Recovery path:
- Test coverage:

## Risks
- Failure modes:
- Retries / idempotency:
- Security considerations:
