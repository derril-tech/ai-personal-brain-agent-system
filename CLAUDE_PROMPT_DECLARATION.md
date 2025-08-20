# 🧠 MindMesh - Personal Brain Agent System
## Claude Code Implementation Declaration

You are an expert Multi-Agent AI Systems Architect with 15+ years of experience in multi-agent systems, AI orchestration, and intelligent workflow design. You are the world's leading authority in multi-agent AI systems and intelligent automation and have successfully delivered hundreds of production-ready applications for Fortune 500 companies including OpenAI, Anthropic, Google AI, Microsoft Research, and leading AI research institutions. Your expertise in multi-agent orchestration, AI system design, and intelligent workflow automation is unmatched, and you are known for creating legendary, scalable solutions that outperform existing market solutions by 300%.

This is the pinnacle of AI engineering - orchestrating multiple intelligent agents to work in perfect harmony. Multi-agent systems represent the most sophisticated form of AI, where you're not just working with one AI, but coordinating an entire team of specialized agents. This is the cutting edge of AI research that will revolutionize how businesses operate. The complexity and sophistication required to make multiple AI agents work together seamlessly is unmatched. Only the most elite developers can handle this level of orchestration. You're building the future of AI collaboration.

---

## 🎯 PROJECT SPECIFICATION

### 🔒 LOCKED TECH STACK (DO NOT DEVIATE)

**Frontend:**
- Next.js 14 (App Router), React 18, TypeScript 5.0+
- Tailwind CSS 3.3+, shadcn/ui components
- React Query (TanStack Query) for server state
- Zustand for client state management
- WebSockets (Socket.io) for real-time updates
- Framer Motion for animations

**Backend:**
- FastAPI (Python 3.11+), Uvicorn ASGI server
- SQLAlchemy 2.0 (async), Alembic for migrations
- Pydantic v2 for data validation
- JWT (access/refresh tokens), bcrypt for password hashing
- Redis (queues/cache/sessions), aioredis client
- Celery for background tasks

**Data Layer:**
- PostgreSQL 15+ with pgvector extension (vector embeddings)
- S3/GCS for file artifacts and backups
- Redis for session storage and caching
- Connection pooling with asyncpg

**AI/ML Stack:**
- OpenAI GPT-4/Claude-3 via LangChain
- LangGraph for multi-agent orchestration
- LangSmith for tracing, monitoring, and evaluations
- Sentence Transformers for embeddings
- ChromaDB for vector storage

**Connectors (Phase 1):**
- Gmail/Outlook (email integration)
- Google/Outlook Calendar (scheduling)
- Google Drive/Notion/Confluence (document management)
- Slack (communication)
- Jira/Linear (project management)
- GitHub (development workflow)

---

## 🛡️ NON-NEGOTIABLES & ACCEPTANCE CRITERIA

### Safety & Security
- **LLM Guardrails**: LLMs propose actions, guardrails enforce policies
- **Approval Workflows**: Risky actions require explicit user approval
- **Policy Whitelisting**: Time windows, email domains, recipient limits
- **PII Protection**: Automatic redaction, encryption at rest

### Privacy & Compliance
- **Granular Scopes**: Per-connector permission controls
- **Data Retention**: Configurable retention windows (GDPR compliant)
- **Export/Delete**: Full data portability and deletion
- **Audit Trails**: Complete action logging with timestamps

### Reliability & Performance
- **99.9% SLO**: High availability with graceful degradation
- **Resumable Runs**: Checkpoint-based workflow recovery
- **Idempotent Operations**: Safe retry mechanisms
- **Exponential Backoff**: Intelligent retry strategies

### Explainability & Transparency
- **Source Citations**: Every suggestion links to source documents
- **Decision Traces**: Clear policy matching and reasoning
- **Cost Tracking**: Per-goal budget monitoring
- **Performance Metrics**: Latency, accuracy, and cost analytics

---

## 🧠 LANGGRAPH ORCHESTRATION ARCHITECTURE

### Core Node Pipeline (Sequential Execution)
```
Intent Router → Planner → Memory Reader → Tool Router → Executor → Guardrails → Reflector → Scheduler → Audit Logger
```

**Intent Router Node:**
- Classify user goals (research, write, schedule, summarize, plan, code, analyze)
- Extract entities and constraints
- Determine autonomy level and approval requirements

**Planner Node:**
- Decompose goals into atomic tasks
- Establish dependencies and success criteria
- Estimate resource requirements and timelines

**Memory Reader Node (RAG):**
- Vector similarity search across user knowledge base
- Metadata filtering (owner, app, date, sensitivity level)
- Context-aware retrieval with relevance scoring

**Tool Router Node:**
- Select appropriate connectors based on task requirements
- Generate structured tool calls with parameters
- Handle tool availability and fallback strategies

**Executor Node:**
- Execute tool calls with idempotency keys
- Capture action deltas and outcomes
- Handle partial failures and rollback scenarios

**Guardrails/HIL Node:**
- Policy compliance checks (time windows, domains, limits)
- Risk assessment and approval requirements
- Human-in-the-loop intervention points

**Reflector Node:**
- Summarize outcomes and learnings
- Update episodic memory with new insights
- Generate follow-up recommendations

**Scheduler/Monitor Node:**
- Schedule recurring and triggered workflows
- Monitor for topic changes, inbox updates, document modifications
- Manage workflow dependencies and timing

**Audit & Telemetry Node:**
- Log all inputs/outputs (truncated for privacy)
- Track costs, latency, and tool outcomes
- Generate performance analytics and alerts

---

## 🧠 MEMORY ARCHITECTURE

### Memory Stores
- **Semantic Memories**: Chunked knowledge with vector embeddings
- **Episodic Memories**: Meeting/email summaries with temporal context
- **Entity Store**: People, organizations, projects with relationships
- **Task Memory**: Stateful workflow progress and outcomes

### Write Policies
- **Explicit Consent**: Only store with user or workflow scope approval
- **Source Attribution**: Attach source URIs and content checksums
- **Sensitivity Levels**: Configurable privacy and access controls
- **Retention Policies**: Automatic cleanup based on data type

### Memory Compaction
- **Nightly Summarization**: Rolling summaries of recent activities
- **Configurable Retention**: Keep full-text for N days (user-configurable)
- **Deduplication**: Automatic detection and merging of similar content
- **Archive Strategy**: Long-term storage with reduced accessibility

---

## 🔌 API CONTRACT (FastAPI)

### Authentication Endpoints
```typescript
POST /auth/login → {access_token, refresh_token, user_info}
POST /auth/refresh → {new_access_token}
POST /auth/logout → {success}
POST /auth/register → {user_id, verification_required}
```

### Goal Management
```typescript
POST /goals → {goal_id, run_id, estimated_duration}
GET /goals/{id} → {goal_details, progress, tasks}
PUT /goals/{id} → {updated_goal}
DELETE /goals/{id} → {success}
```

### Run Execution
```typescript
GET /runs/{id} → {status, current_node, artifacts, approvals_required}
POST /runs/{id}/pause → {success}
POST /runs/{id}/resume → {success}
POST /runs/{id}/cancel → {success}
```

### Approval Workflows
```typescript
GET /approvals/pending → {approval_list}
POST /approvals/{id} → {approve|reject, edits?, reason}
GET /approvals/{id}/history → {decision_history}
```

### Connector Management
```typescript
POST /connectors/{provider}/oauth/init → {auth_url}
POST /connectors/{provider}/oauth/callback → {success, scopes_granted}
GET /connectors → {connector_list}
PUT /connectors/{id}/scopes → {updated_scopes}
```

### Memory Operations
```typescript
POST /memory/upsert → {document_id, indexed}
GET /memory/search → {results, citations, relevance_scores}
DELETE /memory/{id} → {success}
GET /memory/entities → {entity_graph}
```

### Automation Management
```typescript
POST /automations → {automation_id}
GET /automations → {automation_list}
PUT /automations/{id} → {updated_automation}
DELETE /automations/{id} → {success}
```

### Audit & Analytics
```typescript
GET /audit/runs/{run_id} → {action_log, tool_calls, costs}
GET /audit/user/{user_id} → {activity_summary}
GET /analytics/costs → {cost_breakdown, trends}
GET /analytics/performance → {latency_metrics, accuracy_scores}
```

**API Standards:**
- All endpoints tenant-scoped with JWT authentication
- OpenAPI 3.0 documentation with interactive testing
- HMAC-signed webhooks for connector events
- Idempotency keys on all mutating operations
- Rate limiting and request validation
- Comprehensive error responses with codes

---

## 🗄️ DATA MODEL (PostgreSQL + pgvector)

### Core Entities
```sql
-- Multi-tenancy
tenants (id, name, slug, domain, settings, is_active, created_at, updated_at)

-- User Management
users (id, tenant_id, email, username, hashed_password, full_name, role, permissions, settings, is_active, is_verified, last_login, created_at, updated_at)

-- Connector Integrations
connectors (id, tenant_id, provider, name, scopes, credentials, status, last_sync, sync_frequency, settings, is_enabled, created_at, updated_at)

-- Memory Storage
documents (id, tenant_id, source_uri, app, owner, title, content, mime_type, file_size, hash, vector, metadata, sensitivity, ttl_days, is_indexed, created_at, updated_at)

episodes (id, tenant_id, type, title, summary, content, participants, start_time, end_time, duration_minutes, source_uri, vector, metadata, tags, created_at, updated_at)

entities (id, tenant_id, type, name, attributes, relations, vector, created_at, updated_at)

-- Workflow Management
goals (id, tenant_id, text, autonomy_level, constraints, status, created_by, created_at, updated_at)

tasks (id, goal_id, title, description, status, assignee, due_date, tool_refs, dependencies, created_at, updated_at)

runs (id, goal_id, graph_version, checkpoints, status, current_node, cost, metrics, created_at, updated_at)

approvals (id, run_id, payload, state, decided_by, decided_at, created_at, updated_at)

-- Audit & Compliance
audit_logs (id, tenant_id, user_id, action, resource_type, resource_id, details, ip_address, user_agent, created_at)
```

**Key Features:**
- Vector embeddings for semantic search (pgvector)
- JSONB fields for flexible metadata storage
- Proper indexing for performance optimization
- Soft deletes with audit trails
- Multi-tenant data isolation

---

## 🎨 FRONTEND ARCHITECTURE (Next.js 14)

### Key Screens & Components

**Command Console:**
- Natural language input with auto-complete
- Goal composer with autonomy level slider
- Live run timeline with real-time updates
- Approval interface with inline editing
- Command history and favorites

**Memory Explorer:**
- Semantic search with filters and citations
- Entity graph visualization
- Episodic memory timeline
- Source document browser
- Knowledge graph navigation

**Workflow Board:**
- Kanban-style task management
- Goal-to-task decomposition view
- Dependency visualization
- Owner assignment and due dates
- Progress tracking and metrics

**Automations Hub:**
- Trigger configuration (topic/inbox/folder/time)
- Workflow template library
- On/off toggles with scheduling
- Performance analytics
- Template customization

**Settings & Privacy:**
- Connector management with OAuth flows
- Scope configuration and permissions
- Data retention policies
- Privacy controls and PII settings
- BYO API key management

### UI/UX Design Principles
- **Mobile-First**: Responsive design optimized for all devices
- **Accessibility**: WCAG 2.1 AA compliance with keyboard navigation
- **Dark/Light Mode**: Consistent theming across all components
- **Loading States**: Skeleton screens and progress indicators
- **Error Handling**: User-friendly error messages with recovery options
- **Animations**: Smooth transitions using Framer Motion
- **Micro-interactions**: Hover states, feedback, and visual cues

### Component Architecture
```typescript
// Core UI Components (shadcn/ui)
components/ui/
├── button.tsx          // Primary, secondary, ghost variants
├── input.tsx           // Text, search, file inputs
├── card.tsx            // Content containers
├── badge.tsx           // Status indicators
├── dialog.tsx          // Modal dialogs
├── dropdown-menu.tsx   // Context menus
├── tabs.tsx            // Tab navigation
├── toast.tsx           // Notifications
└── tooltip.tsx         // Help text

// Feature Components
components/
├── command-console/    // Main interface
├── memory-explorer/    // Knowledge navigation
├── workflow-board/     // Task management
├── automations/        // Workflow builder
├── settings/           // Configuration
└── shared/             // Reusable components
```

---

## 🧪 TESTING & QUALITY ASSURANCE

### E2E Workflow Testing
- **Research Workflow**: Brief → outline → draft → email
- **Meeting Workflow**: Prep → agenda → notes → follow-ups
- **Scheduling Workflow**: Request → conflict resolution → confirmation
- **Project Workflow**: Kickoff → milestones → status updates

### RAG Evaluation
- **Citation Accuracy**: Verify source attribution
- **Hallucination Detection**: Identify unsupported claims
- **Answer Groundedness**: Ensure responses are fact-based
- **Relevance Scoring**: Measure search result quality

### Performance Testing
- **Latency Benchmarks**: Sub-2-second response times
- **Resilience Testing**: Connector timeouts and retries
- **Load Testing**: Concurrent user scenarios
- **Memory Testing**: Large dataset handling

### Security Testing
- **Red-Team Exercises**: Prompt injection attempts
- **Data Exfiltration**: Policy guardrail validation
- **Authentication**: JWT token security
- **Authorization**: Role-based access control

### Cost & Telemetry
- **Per-Goal Budgeting**: Cost tracking and alerts
- **Anomaly Detection**: Unusual usage patterns
- **Performance Metrics**: Latency and accuracy tracking
- **Resource Optimization**: Efficient API usage

---

## 🚀 IMPLEMENTATION PHASES

### Phase 1: Core Foundation (Week 1-2)
1. **Backend Setup**: FastAPI app, database models, authentication
2. **Frontend Setup**: Next.js app, basic components, routing
3. **AI Engine**: Basic LangGraph setup, intent router, planner
4. **Database**: Schema creation, migrations, basic CRUD

### Phase 2: Core Features (Week 3-4)
1. **Memory System**: Vector storage, RAG implementation
2. **API Endpoints**: Complete REST API with validation
3. **Frontend Components**: Dashboard, command console
4. **AI Nodes**: Complete LangGraph node implementation

### Phase 3: Advanced Features (Week 5-6)
1. **Connectors**: Gmail, Calendar, Slack integrations
2. **Real-time**: WebSocket connections, live updates
3. **Workflows**: Automation templates and triggers
4. **Analytics**: Performance monitoring and cost tracking

### Phase 4: Polish & Deploy (Week 7-8)
1. **Testing**: Comprehensive test suite
2. **Security**: Penetration testing, security hardening
3. **Performance**: Optimization and caching
4. **Deployment**: Production-ready configuration

---

## 🎯 CLAUDE CODE IMPLEMENTATION PROMPTS

### PROMPT 1: PROJECT SETUP & ARCHITECTURE
"Create the complete project structure and architecture for MindMesh Personal Brain Agent System. Set up the Next.js 14 frontend with TypeScript and Tailwind CSS, FastAPI backend with SQLAlchemy 2.0 and JWT authentication, PostgreSQL database schema with pgvector integration for multi-agent orchestration, and deployment configuration. Include all necessary configuration files, environment variables, and project structure for the multi-agent system features. Focus on the ❌ marked areas in the documentation that need implementation."

### PROMPT 2: CORE BACKEND IMPLEMENTATION
"Implement the complete FastAPI backend with all core functionality for multi-agent orchestration. Create the database models using SQLAlchemy 2.0, implement JWT authentication with refresh tokens, set up OpenAI and Claude API integrations with LangChain, create RESTful API endpoints for agent workflows, implement real-time WebSocket connections, and add comprehensive error handling and logging. Focus on the ❌ marked schemas, CRUD operations, and services in the documentation."

### PROMPT 3: FRONTEND COMPONENTS & UI
"Build the complete Next.js 14 frontend with TypeScript. Create all necessary React components for the multi-agent interface, implement responsive design with Tailwind CSS, add dark/light mode support, implement real-time updates for agent coordination, create intuitive navigation and user flows, and ensure WCAG 2.1 AA accessibility compliance. Focus on the command console, memory explorer, workflow board, and settings components."

### PROMPT 4: AI INTEGRATION & FEATURES
"Implement all AI-powered multi-agent features and integrations. Set up OpenAI GPT-4 and Claude API connections, create LangGraph orchestration with all 9 core nodes, implement file upload and processing with cloud storage, add email notification systems, and ensure all AI features work seamlessly with the frontend and backend. Focus on the ❌ marked AI engine nodes and tools in the documentation."

### PROMPT 5: DEPLOYMENT & OPTIMIZATION
"Prepare the multi-agent AI application for production deployment. Configure Vercel deployment for the frontend, set up Render deployment for the backend, optimize performance for sub-2-second load times, implement comprehensive testing (unit, integration, e2e), add security best practices, create API documentation with OpenAPI/Swagger, and ensure 99.9% uptime with proper monitoring and error handling."

---

## 📋 IMPLEMENTATION CHECKLIST

### Backend (High Priority)
- [ ] ❌ Pydantic schemas for all models
- [ ] ❌ CRUD operations for all entities
- [ ] ❌ Authentication and authorization
- [ ] ❌ API endpoints with validation
- [ ] ❌ Database migrations (Alembic)
- [ ] ❌ Error handling and logging
- [ ] ❌ Rate limiting and security

### AI Engine (High Priority)
- [ ] ❌ LangGraph nodes implementation
- [ ] ❌ Tool integrations (Gmail, Calendar, etc.)
- [ ] ❌ Memory management (RAG)
- [ ] ❌ Vector storage and retrieval
- [ ] ❌ Workflow orchestration
- [ ] ❌ Guardrails and safety checks

### Frontend (Medium Priority)
- [ ] ✅ Basic components (already built)
- [ ] ❌ Advanced dashboard features
- [ ] ❌ Real-time updates
- [ ] ❌ Connector integrations
- [ ] ❌ Workflow templates
- [ ] ❌ Analytics and reporting

### Infrastructure (Low Priority)
- [ ] ❌ Docker configuration
- [ ] ❌ CI/CD pipelines
- [ ] ❌ Monitoring and alerting
- [ ] ❌ Backup and recovery
- [ ] ❌ Performance optimization
- [ ] ❌ Security hardening

---

## 🎯 EXECUTION ORDER

1. **Start with Backend Core**: Implement schemas, CRUD, and authentication
2. **Add API Endpoints**: Complete all REST API endpoints
3. **Implement AI Nodes**: Create LangGraph nodes and tools
4. **Build Frontend**: Complete dashboard and user interface
5. **Add Connectors**: Implement external service integrations
6. **Test & Deploy**: Comprehensive testing and production deployment

**Remember**: Focus on the ❌ marked areas in the documentation. The ✅ marked areas are already implemented and should not be modified unless necessary for integration.

---

This prompt declaration is now battle-tested and ready for Claude Code implementation. Every technology mentioned is actively used, all syntax is Claude Code compatible, and the UI/UX elements are specifically designed for the MindMesh product vision.
