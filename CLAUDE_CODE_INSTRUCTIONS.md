# 🧠 MindMesh - Claude Code Implementation Guide

## Project Overview

MindMesh is a Personal Brain Agent System that orchestrates AI agents to help users achieve goals through natural language commands. The system uses LangGraph for workflow orchestration, RAG for memory retrieval, and provides a modern web interface.

## Architecture Summary

- **Frontend**: Next.js 14 with TypeScript, Tailwind CSS, shadcn/ui components
- **Backend**: FastAPI with async SQLAlchemy, JWT auth, comprehensive API structure
- **AI Engine**: LangGraph orchestration with 9 core nodes (Intent Router → Planner → Memory Reader → Tool Router → Executor → Guardrails → Reflector → Scheduler → Audit Logger)
- **Database**: PostgreSQL + pgvector for vector embeddings, Redis for caching
- **Infrastructure**: Docker Compose for development, comprehensive environment setup

## Implementation Priorities for Claude Code

### 🔥 HIGH PRIORITY (Start Here)

#### 1. Backend Core Implementation
**Location**: `backend/app/`

**Missing Files to Create**:
- `backend/app/core/auth.py` - JWT authentication logic
- `backend/app/core/logging.py` - Structured logging setup
- `backend/app/core/middleware.py` - Custom middleware classes
- `backend/app/schemas/` - Complete Pydantic schemas for all models
- `backend/app/crud/` - Database CRUD operations
- `backend/app/api/v1/endpoints/` - Complete API endpoints (runs, approvals, connectors, memory, automations, audit)
- `backend/alembic/` - Database migrations

**Key Implementation Notes**:
- All endpoints should be tenant-scoped
- Use async/await throughout
- Implement proper error handling and validation
- Add comprehensive logging and audit trails

#### 2. Frontend Core Components
**Location**: `frontend/`

**Missing Files to Create**:
- `frontend/components/ui/` - shadcn/ui components
- `frontend/components/providers.tsx` - React Query, Zustand, theme providers
- `frontend/lib/` - Utility functions, API clients, hooks
- `frontend/app/(dashboard)/` - Main dashboard pages
- `frontend/app/(auth)/` - Authentication pages
- `frontend/types/` - TypeScript type definitions

**Key Implementation Notes**:
- Use shadcn/ui for consistent design
- Implement responsive, mobile-first design
- Add proper loading states and error handling
- Use React Query for data fetching

#### 3. AI Engine Nodes
**Location**: `ai_engine/mindmesh/nodes/`

**Missing Files to Create**:
- `ai_engine/mindmesh/nodes/intent_router.py` - Classify user goals
- `ai_engine/mindmesh/nodes/planner.py` - Decompose goals into tasks
- `ai_engine/mindmesh/nodes/memory_reader.py` - RAG-based memory retrieval
- `ai_engine/mindmesh/nodes/tool_router.py` - Select appropriate tools
- `ai_engine/mindmesh/nodes/executor.py` - Execute tool calls
- `ai_engine/mindmesh/nodes/guardrails.py` - Safety and approval checks
- `ai_engine/mindmesh/nodes/reflector.py` - Learn and update memory
- `ai_engine/mindmesh/nodes/scheduler.py` - Schedule follow-up tasks
- `ai_engine/mindmesh/nodes/audit.py` - Log all activities

**Key Implementation Notes**:
- Each node should be a LangGraph node class
- Implement proper error handling and retries
- Add comprehensive logging and tracing
- Ensure idempotency for all operations

### 🟡 MEDIUM PRIORITY

#### 4. Connector Integrations
**Location**: `backend/app/connectors/`

**Implement**:
- Gmail/Outlook email connectors
- Google/Outlook Calendar connectors
- Google Drive/Notion/Confluence document connectors
- Slack communication connector
- Jira/Linear project management connectors
- GitHub development connector

#### 5. Memory Management
**Location**: `backend/app/services/memory.py`

**Implement**:
- Vector embedding generation
- Semantic search functionality
- Memory deduplication
- Episodic memory storage
- Entity extraction and linking

#### 6. Workflow Templates
**Location**: `backend/app/templates/`

**Implement**:
- Research workflow (brief → outline → draft → review → publish)
- Meeting workflow (prep → agenda → notes → action items → follow-ups)
- Project workflow (kickoff → milestones → owners → reminders → status)

### 🟢 LOW PRIORITY

#### 7. Advanced Features
- Real-time WebSocket connections for live updates
- Advanced analytics and reporting
- Custom workflow builder
- Advanced security features (PII redaction, encryption)
- Performance monitoring and optimization

## File Structure Deep Dive

### Backend Structure
```
backend/
├── app/
│   ├── core/           # Core functionality (auth, config, database, logging, middleware)
│   ├── models/         # SQLAlchemy models (✅ COMPLETE)
│   ├── schemas/        # Pydantic schemas (❌ NEEDS IMPLEMENTATION)
│   ├── crud/           # Database operations (❌ NEEDS IMPLEMENTATION)
│   ├── api/v1/         # API endpoints (❌ PARTIAL - needs completion)
│   ├── services/       # Business logic services (❌ NEEDS IMPLEMENTATION)
│   ├── connectors/     # External service integrations (❌ NEEDS IMPLEMENTATION)
│   └── templates/      # Workflow templates (❌ NEEDS IMPLEMENTATION)
├── alembic/            # Database migrations (❌ NEEDS IMPLEMENTATION)
└── tests/              # Test suite (❌ NEEDS IMPLEMENTATION)
```

### Frontend Structure
```
frontend/
├── app/
│   ├── (auth)/         # Authentication pages (❌ NEEDS IMPLEMENTATION)
│   ├── (dashboard)/    # Main dashboard (❌ NEEDS IMPLEMENTATION)
│   ├── api/            # API route handlers (❌ NEEDS IMPLEMENTATION)
│   ├── globals.css     # Global styles (✅ COMPLETE)
│   └── layout.tsx      # Root layout (✅ COMPLETE)
├── components/
│   ├── ui/             # shadcn/ui components (❌ NEEDS IMPLEMENTATION)
│   ├── forms/          # Form components (❌ NEEDS IMPLEMENTATION)
│   ├── dashboard/      # Dashboard-specific components (❌ NEEDS IMPLEMENTATION)
│   └── providers.tsx   # App providers (❌ NEEDS IMPLEMENTATION)
├── lib/                # Utilities and helpers (❌ NEEDS IMPLEMENTATION)
├── types/              # TypeScript definitions (❌ NEEDS IMPLEMENTATION)
└── hooks/              # Custom React hooks (❌ NEEDS IMPLEMENTATION)
```

### AI Engine Structure
```
ai_engine/
├── mindmesh/
│   ├── nodes/          # LangGraph nodes (❌ NEEDS IMPLEMENTATION)
│   ├── graphs/         # Graph definitions (✅ COMPLETE)
│   ├── state.py        # State management (✅ COMPLETE)
│   ├── tools/          # Tool implementations (❌ NEEDS IMPLEMENTATION)
│   └── memory/         # Memory management (❌ NEEDS IMPLEMENTATION)
└── tests/              # Test suite (❌ NEEDS IMPLEMENTATION)
```

## Key Implementation Guidelines

### 1. Database & Models
- All models are already defined with proper relationships
- Use async SQLAlchemy 2.0 patterns
- Implement proper indexing for performance
- Add database migrations using Alembic

### 2. API Design
- Follow RESTful conventions
- Use proper HTTP status codes
- Implement comprehensive error handling
- Add request/response validation with Pydantic
- Include proper documentation with OpenAPI

### 3. Authentication & Security
- Implement JWT-based authentication
- Add role-based access control
- Implement proper password hashing
- Add rate limiting and security headers
- Implement audit logging for all actions

### 4. Frontend Development
- Use TypeScript for type safety
- Implement responsive design with Tailwind CSS
- Use shadcn/ui for consistent UI components
- Implement proper state management with Zustand
- Add comprehensive error boundaries and loading states

### 5. AI/ML Implementation
- Use LangGraph for workflow orchestration
- Implement proper error handling and retries
- Add comprehensive logging and tracing
- Ensure idempotency for all operations
- Implement proper memory management with RAG

## Environment Setup

1. Copy `env.example` to `.env` and configure
2. Run `docker-compose up -d postgres redis`
3. Install backend dependencies: `cd backend && pip install -r requirements.txt`
4. Install frontend dependencies: `cd frontend && npm install`
5. Run database migrations: `cd backend && alembic upgrade head`
6. Start backend: `cd backend && uvicorn app.main:app --reload`
7. Start frontend: `cd frontend && npm run dev`

## Testing Strategy

- Unit tests for all business logic
- Integration tests for API endpoints
- E2E tests for critical user flows
- Performance tests for AI workflows
- Security tests for authentication and authorization

## Deployment Considerations

- Use Docker for containerization
- Implement proper health checks
- Add monitoring and alerting
- Configure proper logging and tracing
- Implement backup and recovery procedures

## Next Steps for Claude Code

1. **Start with Backend Core**: Implement authentication, schemas, and basic CRUD operations
2. **Add API Endpoints**: Complete all missing API endpoints with proper validation
3. **Implement AI Nodes**: Create all LangGraph nodes with proper error handling
4. **Build Frontend**: Create dashboard components and authentication flows
5. **Add Connectors**: Implement external service integrations
6. **Test & Polish**: Add comprehensive testing and performance optimization

## Questions for Claude Code

If you need clarification on any aspect:
1. Check the existing code structure for patterns
2. Refer to the database models for data relationships
3. Look at the environment configuration for available services
4. Review the LangGraph documentation for node implementation patterns

Good luck building MindMesh! 🚀
