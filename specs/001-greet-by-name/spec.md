# Feature Specification: Greet by Name

**Feature Branch**: None (local Lab has no Git repository)

**Created**: 2026-11-26

**Status**: Implemented

**Input**: A learner wants a tiny greeting that makes a requirement change easy to see.

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Receive a personal greeting (Priority: P1)

A person gives one name and receives a greeting addressed to that name. This is the entire first feature.

**Why this priority**: One input and one output make the requirement, plan, task, and observed result easy to trace.

**Independent Test**: Supply a name and compare the resulting line with the expected greeting.

**Acceptance Scenarios**:

1. **Given** the greeting is available, **When** a person supplies `Ada`, **Then** the output is exactly `Hello, Ada!` followed by a newline.
2. **Given** the greeting is available, **When** a person supplies `Lin`, **Then** the output is exactly `Hello, Lin!` followed by a newline.
3. **Given** the greeting is available, **When** a person supplies no name, **Then** a short usage message is shown and the request fails.

### Edge Cases

- Surrounding whitespace on a supplied name is ignored.
- A name containing only whitespace is rejected with a short explanation.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: The greeting MUST accept one name supplied by the person running it.
- **FR-002**: For a valid name, the greeting MUST output exactly one line in the form `Hello, <name>!`.
- **FR-003**: The greeting MUST remove leading and trailing whitespace from the name before producing output.
- **FR-004**: The greeting MUST reject a missing or whitespace-only name with a non-success result and a helpful message.

### Key Entities

- **Name**: The person's supplied text after trimming surrounding whitespace. It is used only for the current greeting.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: A person can produce the expected greeting with one command and one name in under one minute.
- **SC-002**: The two valid examples and two invalid examples produce their specified results in four of four checks.
- **SC-003**: A learner can change the salutation in this specification and identify the corresponding changes needed in the plan, tasks, and output without adding a new component.

## Assumptions

- The greeting runs locally for one person at a time.
- No persistence, network service, account, or localization is needed.
- The first implementation uses `Hello`; changing it is the learner exercise.
