# 🧠 MindMesh - Personal Brain Agent System

Your always-on team of specialists for life & work.

## Overview

MindMesh connects your scattered knowledge (email, files, notes, calendar, links) to a coordinated crew of AI agents that plan, research, write, schedule, decide, and follow up—with clear approvals and privacy controls.

## Architecture

### Tech Stack
- **Frontend**: Next.js 14, React 18, TypeScript, Tailwind CSS, shadcn/ui, React Query, WebSockets
- **Backend**: FastAPI (Python 3.11+), SQLAlchemy 2.0 (async), Pydantic v2, JWT, Redis
- **Data**: PostgreSQL + pgvector, S3/GCS, Redis
- **AI**: OpenAI + Anthropic via LangChain, LangGraph orchestration, LangSmith tracing
- **Connectors**: Gmail/Outlook, Google/Outlook Calendar, Google Drive/Notion/Confluence, Slack, Jira/Linear, GitHub

### Core Features
- **Unified Memory Hub**: Ingests & dedupes data, builds personal knowledge graph
- **Orchestrated Agent Team**: Planner, Researcher, Writer, Organizer, Project Manager, Analyst
- **Inbox & Command Console**: Natural language commands with live agent timeline
- **Workflow Templates**: Research, meeting prep, project kickoff workflows
- **Privacy & Governance**: Per-connector scopes, PII redaction, audit trails

## Quick Start

### Prerequisites
- Python 3.11+
- Node.js 18+
- PostgreSQL 14+ with pgvector extension
- Redis 6+
- Docker & Docker Compose

### Development Setup

1. **Clone and setup environment**
```bash
git clone <repository>
cd ai-personal-brain-agent-system
cp .env.example .env
# Edit .env with your configuration
```

2. **Start infrastructure**
```bash
docker-compose up -d postgres redis
```

3. **Backend setup**
```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
alembic upgrade head
uvicorn app.main:app --reload
```

4. **Frontend setup**
```bash
cd frontend
npm install
npm run dev
```

5. **AI/ML setup**
```bash
cd ai_engine
pip install -r requirements.txt
python -m langchain.scripts.setup_langsmith
```

## Project Structure

```
ai-personal-brain-agent-system/
├── backend/                 # FastAPI backend
├── frontend/               # Next.js frontend
├── ai_engine/              # LangGraph orchestration
├── infrastructure/         # Docker, deployment configs
├── docs/                   # Documentation
└── tests/                  # E2E and integration tests
```

## API Documentation

Once running, visit:
- Backend API: http://localhost:8000/docs
- Frontend: http://localhost:3000

## Implementation Priorities for Claude Code

### High Priority (Complete First)
1. **Backend API Endpoints** - Complete remaining CRUD operations
2. **Database Migrations** - Set up Alembic migrations
3. **Authentication Flow** - Complete login/register pages
4. **Core Dashboard** - Implement main dashboard functionality
5. **LangGraph Nodes** - Implement individual AI engine nodes

### Medium Priority
1. **Memory Management** - Document indexing and search
2. **Connector Integrations** - Gmail, Slack, Notion APIs
3. **Real-time Updates** - WebSocket connections
4. **Workflow Templates** - Pre-built automation templates

### Low Priority
1. **Advanced Analytics** - Charts and metrics
2. **Mobile Optimization** - Responsive design improvements
3. **Performance Optimization** - Caching and optimization
4. **Advanced Features** - Advanced automation rules

## File Structure Deep Dive

### Backend (`backend/`)
```
backend/
├── app/
│   ├── main.py                 # ✅ FastAPI app setup
│   ├── core/                   # ✅ Core configurations
│   │   ├── config.py           # ✅ Settings management
│   │   ├── database.py         # ✅ Database setup
│   │   ├── auth.py             # ✅ Authentication logic
│   │   ├── logging.py          # ✅ Structured logging
│   │   └── middleware.py       # ✅ Custom middleware
│   ├── models/                 # ✅ SQLAlchemy models
│   │   ├── __init__.py         # ✅ Model imports
│   │   ├── tenant.py           # ✅ Tenant model
│   │   ├── user.py             # ✅ User model
│   │   ├── connector.py        # ✅ Connector model
│   │   ├── document.py         # ✅ Document model
│   │   ├── episode.py          # ✅ Episode model
│   │   ├── entity.py           # ✅ Entity model
│   │   ├── goal.py             # ✅ Goal model
│   │   ├── task.py             # ✅ Task model
│   │   ├── run.py              # ✅ Run model
│   │   ├── approval.py         # ✅ Approval model
│   │   └── audit_log.py        # ✅ Audit log model
│   ├── api/v1/                 # ✅ API routes
│   │   ├── api.py              # ✅ Main router
│   │   └── endpoints/          # ✅ Endpoint handlers
│   │       ├── auth.py         # ✅ Auth endpoints
│   │       └── goals.py        # ✅ Goals endpoints
│   ├── schemas/                # ❌ Pydantic schemas (NEEDS IMPLEMENTATION)
│   ├── crud/                   # ❌ Database operations (NEEDS IMPLEMENTATION)
│   └── services/               # ❌ Business logic (NEEDS IMPLEMENTATION)
├── requirements.txt            # ✅ Python dependencies
└── alembic.ini                 # ❌ Migration config (NEEDS IMPLEMENTATION)
```

### Frontend (`frontend/`)
```
frontend/
├── app/                        # ✅ Next.js 14 App Router
│   ├── layout.tsx              # ✅ Root layout with providers
│   ├── globals.css             # ✅ Global styles and Tailwind
│   ├── page.tsx                # ✅ Home page
│   └── dashboard/              # ✅ Dashboard pages
│       └── page.tsx            # ✅ Main dashboard
├── components/                 # ✅ Reusable UI components
│   ├── ui/                     # ✅ shadcn/ui components
│   │   ├── button.tsx          # ✅ Button component with variants
│   │   ├── input.tsx           # ✅ Input component
│   │   ├── card.tsx            # ✅ Card components
│   │   └── badge.tsx           # ✅ Badge component
│   ├── providers.tsx           # ✅ App providers (React Query, Theme)
│   └── dashboard/              # ✅ Dashboard-specific components
│       ├── command-console.tsx # ✅ Main command interface
│       └── goals-overview.tsx  # ✅ Goals display component
├── lib/                        # ✅ Utility functions and configurations
│   ├── utils.ts                # ✅ Utility functions (cn, formatDate, etc.)
│   ├── api.ts                  # ✅ API client with interceptors
│   └── store.ts                # ✅ Zustand stores (auth, UI, app)
├── hooks/                      # ✅ Custom React hooks
│   ├── useAuth.ts              # ✅ Authentication hook
│   └── useGoals.ts             # ✅ Goals management hook
├── types/                      # ✅ TypeScript type definitions
│   └── index.ts                # ✅ Complete type definitions
├── package.json                # ✅ Dependencies and scripts
├── next.config.js              # ✅ Next.js configuration
└── tailwind.config.js          # ✅ Tailwind CSS configuration
```

### AI Engine (`ai_engine/`)
```
ai_engine/
├── mindmesh/
│   ├── graphs/
│   │   └── main_graph.py       # ✅ Main LangGraph orchestration
│   ├── state.py                # ✅ Workflow state management
│   ├── nodes/                  # ❌ Individual nodes (NEEDS IMPLEMENTATION)
│   │   ├── intent_router.py    # ❌ Intent classification
│   │   ├── planner.py          # ❌ Goal decomposition
│   │   ├── memory_reader.py    # ❌ RAG retrieval
│   │   ├── tool_router.py      # ❌ Tool selection
│   │   ├── executor.py         # ❌ Action execution
│   │   ├── guardrails.py       # ❌ Safety checks
│   │   ├── reflector.py        # ❌ Outcome analysis
│   │   ├── scheduler.py        # ❌ Task scheduling
│   │   └── audit_logger.py     # ❌ Audit logging
│   ├── tools/                  # ❌ Tool integrations (NEEDS IMPLEMENTATION)
│   │   ├── gmail.py            # ❌ Gmail integration
│   │   ├── calendar.py         # ❌ Calendar integration
│   │   ├── slack.py            # ❌ Slack integration
│   │   └── notion.py           # ❌ Notion integration
│   └── memory/                 # ❌ Memory management (NEEDS IMPLEMENTATION)
│       ├── vector_store.py     # ❌ Vector database operations
│       ├── embeddings.py       # ❌ Embedding generation
│       └── retrieval.py        # ❌ Semantic search
├── requirements.txt            # ✅ AI/ML dependencies
└── config/                     # ❌ AI configuration (NEEDS IMPLEMENTATION)
```

## Key Implementation Guidelines

### Backend Implementation
1. **Follow FastAPI best practices** - Use dependency injection, proper error handling
2. **Implement proper validation** - Use Pydantic schemas for all inputs/outputs
3. **Add comprehensive logging** - Use structured logging for debugging
4. **Implement proper authentication** - JWT with refresh tokens
5. **Add rate limiting** - Protect against abuse
6. **Use async/await** - Leverage SQLAlchemy 2.0 async features

### Frontend Implementation
1. **Mobile-first design** - Ensure responsive design
2. **Accessibility** - Follow WCAG guidelines
3. **Performance** - Use React Query for caching, optimize bundles
4. **Type safety** - Use TypeScript strictly
5. **Component composition** - Build reusable components
6. **State management** - Use Zustand for global state

### AI Engine Implementation
1. **Modular design** - Each node should be independent
2. **Error handling** - Graceful failure and recovery
3. **Monitoring** - Use LangSmith for tracing
4. **Security** - Validate all inputs, sanitize outputs
5. **Performance** - Optimize for latency and cost

## Environment Setup

### Required Environment Variables
```bash
# Application
APP_NAME=MindMesh
DEBUG=true
SECRET_KEY=your-secret-key

# Database
DATABASE_URL=postgresql+asyncpg://user:pass@localhost/mindmesh
REDIS_URL=redis://localhost:6379

# AI/ML
OPENAI_API_KEY=your-openai-key
ANTHROPIC_API_KEY=your-anthropic-key
LANGSMITH_API_KEY=your-langsmith-key

# Storage
S3_ENDPOINT_URL=http://localhost:9000
S3_ACCESS_KEY=your-access-key
S3_SECRET_KEY=your-secret-key

# Connectors
GMAIL_CLIENT_ID=your-gmail-client-id
GMAIL_CLIENT_SECRET=your-gmail-client-secret
SLACK_CLIENT_ID=your-slack-client-id
SLACK_CLIENT_SECRET=your-slack-client-secret
```

## Testing Strategy

### Backend Testing
- **Unit tests** - Test individual functions and classes
- **Integration tests** - Test API endpoints with database
- **E2E tests** - Test complete workflows
- **Performance tests** - Test under load

### Frontend Testing
- **Component tests** - Test individual components
- **Integration tests** - Test component interactions
- **E2E tests** - Test user workflows
- **Accessibility tests** - Ensure WCAG compliance

### AI Engine Testing
- **Node tests** - Test individual LangGraph nodes
- **Graph tests** - Test complete workflows
- **Performance tests** - Test latency and cost
- **Safety tests** - Test guardrails and safety measures

## Deployment Considerations

### Production Checklist
- [ ] Environment variables configured
- [ ] Database migrations applied
- [ ] SSL certificates installed
- [ ] Monitoring and logging configured
- [ ] Backup strategy implemented
- [ ] Security headers configured
- [ ] Rate limiting enabled
- [ ] Error tracking configured

### Scaling Considerations
- **Horizontal scaling** - Use load balancers
- **Database scaling** - Read replicas, connection pooling
- **Caching** - Redis for session and query caching
- **CDN** - Static asset delivery
- **Queue processing** - Background job processing

## Next Steps for Claude Code

1. **Start with backend schemas** - Create Pydantic schemas for all models
2. **Implement CRUD operations** - Create database operations in `backend/app/crud/`
3. **Complete API endpoints** - Finish remaining endpoint implementations
4. **Add authentication pages** - Create login/register forms
5. **Implement LangGraph nodes** - Start with intent_router and planner
6. **Add connector integrations** - Begin with Gmail integration
7. **Create memory management** - Implement vector storage and retrieval
8. **Add real-time features** - WebSocket connections for live updates

## Questions for Claude Code

1. **Architecture decisions** - How should we structure the connector integrations?
2. **Performance optimization** - What's the best approach for vector similarity search?
3. **Security considerations** - How should we handle sensitive data in memory?
4. **Scalability planning** - What's the best way to scale the LangGraph workflows?
5. **Testing strategy** - How should we test the AI workflows effectively?

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for development guidelines.

## License

[License details]
