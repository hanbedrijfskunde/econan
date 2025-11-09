---
name: tech-lead
description: Creates comprehensive Technical Design Documents (TDD) that translate product requirements into detailed technical implementation plans. Guides you through architectural decisions, technology choices, data modeling, and component design. Triggers include requests for "TDD", "technical design", "architecture", "system design", "tech spec", or technical planning.
version: 1.0.0
---

## What This Skill Does

This skill helps you create a Technical Design Document (TDD) that bridges the gap between a Product Requirements Document (PRD) and actual implementation. The TDD answers "how" to build what the PRD defines as "what" and "why".

**Target Audience**: The TDD should be detailed enough for a junior developer to implement with minimal ambiguity.

## Process

### 1. Analyze the PRD

Start by deeply understanding the product requirements:
- Which PRD should I read? (provide the file path)
- Let me read and analyze the functional requirements, user stories, and goals
- I'll identify the key technical challenges and integration points

**Note**: If no PRD exists yet, I'll guide you to create one first using the product-manager skill.

### 2. Propose System Architecture

Before diving into details, I'll help you choose the right architectural approach:
- Would you prefer:
  - (A) Serverless architecture for automatic scalability
  - (B) Traditional monolithic architecture for simplicity
  - (C) Microservices architecture for modularity
  - (D) Something else?
- What are your scalability expectations? (users, traffic patterns, data volume)
- Any existing architectural patterns or constraints I should follow?
- Are there performance requirements or SLAs to consider?

### 3. Define Technology Stack

Let's establish the technologies we'll use:
- **Backend**: What's your preference?
  - (A) Node.js + Express
  - (B) Python + Django/FastAPI
  - (C) Java + Spring Boot
  - (D) Other?
- **Frontend**: What should we use?
  - (A) React
  - (B) Vue.js
  - (C) Angular
  - (D) Other?
- **Database**: What fits your data model best?
  - (A) PostgreSQL (relational)
  - (B) MongoDB (document)
  - (C) Redis (cache/key-value)
  - (D) Combination or other?
- **Infrastructure**: Deployment preferences?
  - (A) Cloud (AWS/GCP/Azure)
  - (B) Containers (Docker/Kubernetes)
  - (C) Serverless (Lambda/Cloud Functions)
  - (D) Other?

### 4. Design Data Model

Let's define how data will be structured:
- What are the primary data entities? (e.g., User, Project, Task)
- How do these entities relate to each other?
  - Example: "A User has many Projects, a Project has many Tasks"
- What fields does each entity need?
- Any specific indexing or performance considerations?
- Should I create a visual diagram of the data model?

### 5. Define API Architecture

How will components communicate:
- **API Style**: What should we use?
  - (A) REST (standard HTTP endpoints)
  - (B) GraphQL (flexible queries)
  - (C) gRPC (high-performance)
  - (D) Combination?
- What are the main API endpoints needed?
- Any existing API conventions to follow?
- How will we handle versioning?
- What's the request/response format? (JSON, Protocol Buffers, etc.)

### 6. Plan Authentication & Security

How will we secure the system:
- **Authentication Method**:
  - (A) JWT tokens
  - (B) OAuth 2.0
  - (C) Session-based
  - (D) Other?
- **Authorization**: How granular should permissions be?
  - Role-based (RBAC)?
  - Permission-based?
  - Resource-based?
- What are the main security threats we need to address?
- Any compliance requirements? (GDPR, HIPAA, etc.)
- Rate limiting and abuse prevention strategies?

### 7. Break Down Components

What are the main building blocks:
- What are the primary software components/modules?
  - Example: ConversationManager, ToolExecutor, StateGraph
- What's each component's responsibility?
- How do components interact with each other?
- Any third-party services or libraries needed?
- Should I create a component interaction diagram?

### 8. Define Error Handling Strategy

How will we handle things going wrong:
- What are the critical error scenarios?
- How should errors be logged and monitored?
- What's the retry/fallback strategy?
- How do we communicate errors to users?
- What edge cases need special handling?

### 9. Consider Non-Functional Requirements

Let's address quality attributes:
- **Performance**: Response time goals? Throughput requirements?
- **Scalability**: How should the system scale? Horizontal? Vertical?
- **Reliability**: Uptime requirements? Disaster recovery?
- **Maintainability**: Code organization? Testing strategy?
- **Observability**: Logging? Monitoring? Alerting?

### 10. Identify Dependencies and Open Questions

What still needs resolution:
- What external services or APIs will we depend on?
- What libraries or frameworks are required?
- Are there any technical unknowns that need research?
- What decisions need input from other teams?
- Any potential technical debt or trade-offs to document?

## TDD Document Structure

After gathering all this information, I'll generate a comprehensive TDD with these sections:

1. **Introduction**
   - Feature summary from technical perspective
   - Link to source PRD
   - Architectural overview

2. **System Architecture**
   - High-level architecture diagram
   - Component relationships
   - Data flow
   - Infrastructure overview

3. **Technology Stack**
   - Framework choices and rationale
   - Key libraries and dependencies
   - Development tools

4. **Data Model**
   - Database schema
   - Entity relationships
   - Indexes and constraints
   - Data migration strategy

5. **Component Breakdown**
   - Detailed component descriptions
   - Responsibilities and interfaces
   - Component interaction patterns
   - Key algorithms or logic

6. **API Specification**
   - Endpoint definitions
   - Request/response formats
   - Authentication/authorization
   - Error responses
   - API documentation approach

7. **Security Architecture**
   - Authentication flow
   - Authorization model
   - Security best practices
   - Threat mitigation strategies

8. **Error Handling & Edge Cases**
   - Error handling strategy
   - Edge case handling
   - Validation rules
   - Fallback mechanisms

9. **Performance & Scalability**
   - Performance targets
   - Caching strategy
   - Scaling approach
   - Optimization opportunities

10. **Testing Strategy**
    - Unit testing approach
    - Integration testing
    - End-to-end testing
    - Performance testing

11. **Deployment & Operations**
    - Deployment process
    - Environment configuration
    - Monitoring and alerting
    - Logging strategy

12. **Dependencies**
    - External services
    - Third-party libraries
    - Cross-team dependencies

13. **Open Questions & Future Considerations**
    - Unresolved technical questions
    - Future enhancements
    - Technical debt considerations
    - Research items

## Output Format

- **Format**: Markdown (`.md`)
- **Location**: `/products/` or `/docs/`
- **Filename**: `tdd-[feature-name].md`

## Best Practices

When creating the TDD, I will:
- ✅ Ask clarifying questions before generating
- ✅ Provide specific, actionable technical guidance
- ✅ Consider scalability and maintainability
- ✅ Include diagrams where helpful (using Mermaid syntax)
- ✅ Explain trade-offs for architectural decisions
- ✅ Write for a junior developer audience
- ✅ Balance technical perfectionism with pragmatic delivery
- ✅ Anticipate potential issues and propose solutions
- ✅ Reference the source PRD throughout

## Example Workflow

**User**: "I have a PRD for user authentication. Can you help me create a technical design?"

**Assistant**: "I'll create a comprehensive TDD for the authentication feature. Let me start by reading the PRD..."

[Reads PRD and asks clarifying questions about architecture, tech stack, data model, etc.]

[After getting answers, generates the TDD with all sections]

**Assistant**: "I've created a detailed Technical Design Document and saved it to `/products/tdd-user-authentication.md`. The document includes the full architecture, data model, API specifications, and security considerations. Would you like me to elaborate on any particular section?"

## When to Use This Skill

Use this skill when you:
- Have a PRD and need to plan the technical implementation
- Need to make architectural decisions for a new feature
- Want to break down a complex feature into implementable components
- Need to align the team on technical approach before coding
- Want to document architectural decisions and rationale

**Remember**: A good TDD saves time during implementation by resolving technical questions upfront and providing a clear roadmap for developers.