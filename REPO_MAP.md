# 🗺️ MindMesh Repository Map

## 📁 Project Structure Overview

```
ai-personal-brain-agent-system/
├── 📁 backend/                    # FastAPI Backend Application
├── 📁 frontend/                   # Next.js Frontend Application  
├── 📁 ai_engine/                  # LangGraph AI Orchestration Engine
├── 📁 infrastructure/             # Docker & Deployment Configuration
├── 📁 docs/                       # Documentation & Guides
├── 📁 scripts/                    # Setup & Utility Scripts
├── 📁 tests/                      # E2E & Integration Tests
├── 📄 .env.example               # Environment Variables Template
├── 📄 .gitignore                 # Git Ignore Rules
├── 📄 docker-compose.yml         # Development Infrastructure
├── 📄 README.md                  # Main Project Documentation
├── 📄 REPO_MAP.md               # This File - Repository Navigation
├── 📄 API_SPEC.md               # API Specification & Endpoints
└── 📄 CLAUDE.md                  # Claude Code Instructions
```

---

## 🚀 Backend Structure (`backend/`)

### Core Application (`backend/app/`)

```
backend/app/
├── 📄 main.py                    # 🎯 FastAPI Application Entry Point
│   ├── App initialization with lifespan management
│   ├── Middleware configuration (CORS, security, logging)
│   ├── Exception handlers and error responses
│   ├── Health check endpoint (/health)
│   └── API router inclusion
│
├── 📁 core/                      # 🔧 Core Configuration & Utilities
│   ├── 📄 config.py              # ⚙️ Settings Management (Pydantic Settings)
│   │   ├── Environment variable loading
│   │   ├── Database, Redis, JWT configuration
│   │   ├── AI/ML API keys and settings
│   │   └── Connector configurations
│   │
│   ├── 📄 database.py            # 🗄️ Database Connection & Session Management
│   │   ├── Async SQLAlchemy engine setup
│   │   ├── Session factory and dependency injection
│   │   ├── Database initialization functions
│   │   └── Connection pooling configuration
│   │
│   ├── 📄 auth.py                # 🔐 Authentication & Authorization
│   │   ├── Password hashing (bcrypt)
│   │   ├── JWT token creation and validation
│   │   ├── User authentication functions
│   │   ├── Permission and role decorators
│   │   └── Refresh token handling
│   │
│   ├── 📄 logging.py             # 📝 Structured Logging Configuration
│   │   ├── Structlog setup with JSON formatting
│   │   ├── Request context logging
│   │   ├── User context binding
│   │   └── Custom loggers for different contexts
│   │
│   └── 📄 middleware.py          # 🛡️ Custom FastAPI Middleware
│       ├── Request logging with unique IDs
│       ├── Response time tracking
│       ├── Security headers injection
│       ├── Tenant identification
│       └── Rate limiting protection
│
├── 📁 models/                     # 🗃️ SQLAlchemy Database Models
│   ├── 📄 __init__.py            # 📦 Model imports for Alembic discovery
│   ├── 📄 tenant.py              # 🏢 Multi-tenant organization model
│   │   ├── Tenant isolation and settings
│   │   ├── Domain-based routing
│   │   └── Relationship to all other models
│   │
│   ├── 📄 user.py                # 👤 User authentication and profiles
│   │   ├── JWT-compatible user model
│   │   ├── Role-based permissions
│   │   ├── Settings and preferences
│   │   └── Audit trail relationships
│   │
│   ├── 📄 connector.py           # 🔗 External service integrations
│   │   ├── OAuth2 credential storage
│   │   ├── Sync status and frequency
│   │   ├── Provider-specific settings
│   │   └── Scope management
│   │
│   ├── 📄 document.py            # 📄 Document storage and indexing
│   │   ├── Vector embeddings (pgvector)
│   │   ├── Content deduplication
│   │   ├── Sensitivity classification
│   │   └── TTL and retention policies
│   │
│   ├── 📄 episode.py             # 🎬 Episodic memory (meetings, emails)
│   │   ├── Time-based event tracking
│   │   ├── Participant management
│   │   ├── Vector embeddings for retrieval
│   │   └── Metadata and tagging
│   │
│   ├── 📄 entity.py              # 🏛️ People, organizations, projects
│   │   ├── Entity relationship mapping
│   │   ├── Attribute storage (JSONB)
│   │   ├── Vector embeddings
│   │   └── Active/inactive status
│   │
│   ├── 📄 goal.py                # 🎯 User goals and objectives
│   │   ├── Autonomy level (L0-L3)
│   │   ├── Priority and constraints
│   │   ├── Time tracking (estimated vs actual)
│   │   └── Relationship to tasks and runs
│   │
│   ├── 📄 task.py                # ✅ Individual tasks within goals
│   │   ├── Task dependencies and assignments
│   │   ├── Tool references for execution
│   │   ├── Time tracking and priorities
│   │   └── Status management
│   │
│   ├── 📄 run.py                 # 🏃 LangGraph execution runs
│   │   ├── Graph version tracking
│   │   ├── Checkpoint management
│   │   ├── Cost and metrics tracking
│   │   ├── Error handling and recovery
│   │   └── Artifact storage
│   │
│   ├── 📄 approval.py            # ✅ Human-in-the-loop approvals
│   │   ├── Approval state management
│   │   ├── Decision tracking
│   │   ├── Comment and feedback system
│   │   └── Deadline management
│   │
│   └── 📄 audit_log.py           # 📋 System audit and compliance
│       ├── Action logging with context
│       ├── IP address and user agent tracking
│       ├── Success/failure status
│       └── GDPR compliance support
│
├── 📁 api/v1/                     # 🌐 API Endpoints (Version 1)
│   ├── 📄 api.py                 # 🔗 Main API Router
│   │   ├── Endpoint consolidation
│   │   ├── Tag-based organization
│   │   └── Prefix management
│   │
│   └── 📁 endpoints/              # 📍 Individual Endpoint Handlers
│       ├── 📄 auth.py            # 🔐 Authentication endpoints
│       │   ├── POST /login - User authentication
│       │   ├── POST /register - User registration
│       │   ├── POST /refresh - Token refresh
│       │   └── GET /me - Current user info
│       │
│       ├── 📄 goals.py           # 🎯 Goal management endpoints
│       │   ├── CRUD operations for goals
│       │   ├── Goal execution triggers
│       │   ├── Status updates and filtering
│       │   └── Tenant-scoped operations
│       │
│       ├── 📄 runs.py            # 🏃 Run execution endpoints
│       │   ├── Run status monitoring
│       │   ├── Checkpoint management
│       │   ├── Artifact retrieval
│       │   └── Cost tracking
│       │
│       ├── 📄 approvals.py       # ✅ Approval workflow endpoints
│       │   ├── Approval requests
│       │   ├── Decision submission
│       │   ├── Status updates
│       │   └── Deadline management
│       │
│       ├── 📄 connectors.py      # 🔗 Connector management endpoints
│       │   ├── OAuth2 flow handling
│       │   ├── Connector configuration
│       │   ├── Sync status monitoring
│       │   └── Scope management
│       │
│       ├── 📄 memory.py          # 🧠 Memory management endpoints
│       │   ├── Document indexing
│       │   ├── Semantic search
│       │   ├── Memory updates
│       │   └── Vector operations
│       │
│       ├── 📄 automations.py     # 🤖 Automation workflow endpoints
│       │   ├── Trigger configuration
│       │   ├── Workflow templates
│       │   ├── Execution monitoring
│       │   └── Template management
│       │
│       └── 📄 audit.py           # 📋 Audit and compliance endpoints
│           ├── Audit log retrieval
│           ├── Compliance reporting
│           ├── Data export
│           └── Privacy controls
│
├── 📁 schemas/                    # 📋 Pydantic Schemas (NEEDS IMPLEMENTATION)
│   ├── 📄 __init__.py            # Schema exports
│   ├── 📄 auth.py                # Authentication schemas
│   ├── 📄 goals.py               # Goal-related schemas
│   ├── 📄 runs.py                # Run execution schemas
│   ├── 📄 approvals.py           # Approval workflow schemas
│   ├── 📄 connectors.py          # Connector schemas
│   ├── 📄 memory.py              # Memory management schemas
│   ├── 📄 automations.py         # Automation schemas
│   └── 📄 audit.py               # Audit and compliance schemas
│
├── 📁 crud/                       # 🗄️ Database Operations (NEEDS IMPLEMENTATION)
│   ├── 📄 __init__.py            # CRUD exports
│   ├── 📄 base.py                # Base CRUD operations
│   ├── 📄 auth.py                # User and authentication CRUD
│   ├── 📄 goals.py               # Goal and task CRUD
│   ├── 📄 runs.py                # Run execution CRUD
│   ├── 📄 approvals.py           # Approval workflow CRUD
│   ├── 📄 connectors.py          # Connector management CRUD
│   ├── 📄 memory.py              # Memory operations CRUD
│   ├── 📄 automations.py         # Automation CRUD
│   └── 📄 audit.py               # Audit logging CRUD
│
└── 📁 services/                   # 🏭 Business Logic (NEEDS IMPLEMENTATION)
    ├── 📄 __init__.py            # Service exports
    ├── 📄 auth_service.py        # Authentication business logic
    ├── 📄 goal_service.py        # Goal management logic
    ├── 📄 run_service.py         # Run execution logic
    ├── 📄 approval_service.py    # Approval workflow logic
    ├── 📄 connector_service.py   # Connector integration logic
    ├── 📄 memory_service.py      # Memory management logic
    ├── 📄 automation_service.py  # Automation workflow logic
    └── 📄 audit_service.py       # Audit and compliance logic
```

### Configuration Files

```
backend/
├── 📄 requirements.txt           # 🐍 Python Dependencies
│   ├── FastAPI and web framework
│   ├── Database drivers (asyncpg, psycopg2)
│   ├── AI/ML libraries (langchain, openai)
│   ├── Authentication (python-jose, passlib)
│   ├── Storage (boto3, minio)
│   └── Development tools
│
├── 📄 alembic.ini               # 🗄️ Database Migration Config (NEEDS IMPLEMENTATION)
├── 📄 pyproject.toml            # 📦 Project Configuration (NEEDS IMPLEMENTATION)
└── 📄 .env.example              # 🌍 Environment Variables Template
```

---

## 🎨 Frontend Structure (`frontend/`)

### Next.js Application (`frontend/app/`)

```
frontend/app/
├── 📄 layout.tsx                 # 🎨 Root Layout Component
│   ├── Global providers setup
│   ├── Metadata configuration
│   ├── Font loading (Inter)
│   ├── Global styles inclusion
│   └── Toast notification system
│
├── 📄 globals.css                # 🎨 Global Styles
│   ├── Tailwind CSS directives
│   ├── CSS variables for theming
│   ├── Custom utility classes
│   ├── Neural network animations
│   └── Responsive design utilities
│
├── 📄 page.tsx                   # 🏠 Home Page
│   ├── Landing page content
│   ├── Feature showcase
│   └── Call-to-action elements
│
└── 📁 dashboard/                 # 📊 Dashboard Pages
    ├── 📄 page.tsx              # 🎯 Main Dashboard
    │   ├── Command console integration
    │   ├── Goals overview display
    │   ├── Statistics cards
    │   └── Responsive grid layout
    │
    ├── 📁 goals/                # 🎯 Goal Management Pages
    │   ├── 📄 page.tsx          # Goals list view
    │   ├── 📄 [id]/page.tsx     # Individual goal view
    │   └── 📄 new/page.tsx      # Goal creation form
    │
    ├── 📁 runs/                 # 🏃 Run Execution Pages
    │   ├── 📄 page.tsx          # Runs list view
    │   └── 📄 [id]/page.tsx     # Run details and timeline
    │
    ├── 📁 memory/               # 🧠 Memory Explorer Pages
    │   ├── 📄 page.tsx          # Memory search interface
    │   ├── 📄 documents/page.tsx # Document management
    │   └── 📄 entities/page.tsx  # Entity relationship view
    │
    ├── 📁 automations/          # 🤖 Automation Pages
    │   ├── 📄 page.tsx          # Automation triggers
    │   └── 📄 templates/page.tsx # Workflow templates
    │
    └── 📁 settings/             # ⚙️ Settings Pages
        ├── 📄 page.tsx          # General settings
        ├── 📄 connectors/page.tsx # Connector management
        └── 📄 privacy/page.tsx   # Privacy and security
```

### Components (`frontend/components/`)

```
frontend/components/
├── 📁 ui/                        # 🧩 shadcn/ui Components
│   ├── 📄 button.tsx            # 🔘 Button Component
│   │   ├── Multiple variants (default, destructive, outline, etc.)
│   │   ├── Size options (sm, default, lg, icon)
│   │   ├── Custom neural and gradient variants
│   │   └── Accessibility features
│   │
│   ├── 📄 input.tsx             # 📝 Input Component
│   │   ├── Form input with validation
│   │   ├── Focus states and accessibility
│   │   └── Error handling
│   │
│   ├── 📄 card.tsx              # 🃏 Card Components
│   │   ├── Card, CardHeader, CardTitle
│   │   ├── CardDescription, CardContent
│   │   └── CardFooter components
│   │
│   ├── 📄 badge.tsx             # 🏷️ Badge Component
│   │   ├── Status indicators
│   │   ├── Priority badges
│   │   ├── Custom neural variant
│   │   └── Color-coded variants
│   │
│   ├── 📄 dialog.tsx            # 💬 Dialog Component (NEEDS IMPLEMENTATION)
│   ├── 📄 dropdown-menu.tsx     # 📋 Dropdown Menu (NEEDS IMPLEMENTATION)
│   ├── 📄 form.tsx              # 📋 Form Components (NEEDS IMPLEMENTATION)
│   ├── 📄 select.tsx            # 📝 Select Component (NEEDS IMPLEMENTATION)
│   ├── 📄 tabs.tsx              # 📑 Tabs Component (NEEDS IMPLEMENTATION)
│   ├── 📄 toast.tsx             # 🍞 Toast Notifications (NEEDS IMPLEMENTATION)
│   └── 📄 tooltip.tsx           # 💡 Tooltip Component (NEEDS IMPLEMENTATION)
│
├── 📄 providers.tsx              # 🔧 Application Providers
│   ├── React Query client setup
│   ├── Theme provider configuration
│   ├── Development tools integration
│   └── Global state management
│
└── 📁 dashboard/                 # 📊 Dashboard-Specific Components
    ├── 📄 command-console.tsx   # 💬 Command Console Interface
    │   ├── Natural language input
    │   ├── Message history display
    │   ├── Real-time status updates
    │   ├── AI response handling
    │   └── Goal creation triggers
    │
    ├── 📄 goals-overview.tsx    # 🎯 Goals Overview Component
    │   ├── Active goals display
    │   ├── Status indicators
    │   ├── Priority badges
    │   ├── Quick actions
    │   └── Pagination support
    │
    ├── 📄 run-timeline.tsx      # ⏱️ Run Timeline Component (NEEDS IMPLEMENTATION)
    ├── 📄 memory-explorer.tsx   # 🧠 Memory Explorer (NEEDS IMPLEMENTATION)
    ├── 📄 automation-triggers.tsx # 🤖 Automation Triggers (NEEDS IMPLEMENTATION)
    └── 📄 settings-panel.tsx    # ⚙️ Settings Panel (NEEDS IMPLEMENTATION)
```

### Utilities & Configuration (`frontend/lib/`)

```
frontend/lib/
├── 📄 utils.ts                   # 🛠️ Utility Functions
│   ├── Class name merging (cn)
│   ├── Date formatting utilities
│   ├── Text truncation helpers
│   ├── ID generation
│   ├── Debounce function
│   ├── Email validation
│   ├── File size formatting
│   └── Initials generation
│
├── 📄 api.ts                     # 🌐 API Client Configuration
│   ├── Axios instance setup
│   ├── Request/response interceptors
│   ├── JWT token management
│   ├── Refresh token handling
│   ├── Error handling and toasts
│   ├── File upload support
│   └── Generic HTTP methods
│
└── 📄 store.ts                   # 📦 Zustand State Management
    ├── Auth store (user, tokens, permissions)
    ├── UI store (theme, sidebar, notifications)
    ├── App store (goals, runs, filters)
    ├── Persistence configuration
    └── Type-safe state management
```

### Custom Hooks (`frontend/hooks/`)

```
frontend/hooks/
├── 📄 useAuth.ts                 # 🔐 Authentication Hook
│   ├── Login/logout functionality
│   ├── User registration
│   ├── Permission checking
│   ├── Role-based access control
│   ├── Token refresh handling
│   └── Authentication state management
│
├── 📄 useGoals.ts                # 🎯 Goals Management Hook
│   ├── Goals CRUD operations
│   ├── Goal execution triggers
│   ├── Status updates
│   ├── Filtering and pagination
│   └── Real-time updates
│
├── 📄 useRuns.ts                 # 🏃 Run Execution Hook (NEEDS IMPLEMENTATION)
├── 📄 useMemory.ts               # 🧠 Memory Management Hook (NEEDS IMPLEMENTATION)
├── 📄 useConnectors.ts           # 🔗 Connector Management Hook (NEEDS IMPLEMENTATION)
└── 📄 useAutomations.ts          # 🤖 Automation Hook (NEEDS IMPLEMENTATION)
```

### Type Definitions (`frontend/types/`)

```
frontend/types/
└── 📄 index.ts                   # 📋 TypeScript Type Definitions
    ├── API response types
    ├── Authentication types
    ├── User and tenant types
    ├── Goal and task types
    ├── Run execution types
    ├── Approval workflow types
    ├── Connector types
    ├── Memory types
    ├── Automation types
    ├── Audit types
    ├── Form data types
    ├── UI component types
    ├── WebSocket message types
    ├── Error handling types
    ├── Search and filter types
    └── Chart and metric types
```

### Configuration Files

```
frontend/
├── 📄 package.json               # 📦 Node.js Dependencies
│   ├── Next.js 14 and React 18
│   ├── TypeScript and Tailwind CSS
│   ├── shadcn/ui components
│   ├── React Query and Zustand
│   ├── Form handling (react-hook-form, zod)
│   ├── UI libraries (lucide-react, framer-motion)
│   ├── API client (axios, socket.io-client)
│   └── Development tools
│
├── 📄 next.config.js             # ⚙️ Next.js Configuration
│   ├── App directory setup
│   ├── Image domain configuration
│   ├── Environment variables
│   ├── API rewrites
│   └── Webpack fallbacks
│
├── 📄 tailwind.config.js         # 🎨 Tailwind CSS Configuration
│   ├── Custom color palette (brain, mesh)
│   ├── Custom animations
│   ├── Font family configuration
│   ├── Plugin integration
│   └── Responsive design utilities
│
├── 📄 tsconfig.json              # 📝 TypeScript Configuration (NEEDS IMPLEMENTATION)
├── 📄 postcss.config.js          # 🎨 PostCSS Configuration (NEEDS IMPLEMENTATION)
└── 📄 .env.example               # 🌍 Environment Variables Template
```

---

## 🤖 AI Engine Structure (`ai_engine/`)

### LangGraph Orchestration (`ai_engine/mindmesh/`)

```
ai_engine/mindmesh/
├── 📄 __init__.py                # 📦 Package initialization
│
├── 📁 graphs/                    # 🕸️ LangGraph Workflow Definitions
│   └── 📄 main_graph.py         # 🎯 Main MindMesh Orchestration Graph
│       ├── Node definitions and connections
│       ├── Conditional edge logic
│       ├── Checkpoint management
│       ├── Error handling and recovery
│       └── Human-in-the-loop gates
│
├── 📄 state.py                   # 📊 Workflow State Management
│   ├── Pydantic state model
│   ├── Goal and task tracking
│   ├── Memory and context management
│   ├── Tool call tracking
│   ├── Approval workflow state
│   ├── Cost and metrics tracking
│   └── Audit trail management
│
├── 📁 nodes/                     # 🔧 Individual LangGraph Nodes (NEEDS IMPLEMENTATION)
│   ├── 📄 intent_router.py      # 🎯 Intent Classification Node
│   │   ├── Goal type classification
│   │   ├── Autonomy level determination
│   │   ├── Constraint extraction
│   │   └── Priority assessment
│   │
│   ├── 📄 planner.py            # 📋 Goal Decomposition Node
│   │   ├── Task breakdown
│   │   ├── Dependency mapping
│   │   ├── Resource allocation
│   │   └── Timeline estimation
│   │
│   ├── 📄 memory_reader.py      # 🧠 RAG Retrieval Node
│   │   ├── Vector similarity search
│   │   ├── Context retrieval
│   │   ├── Relevance scoring
│   │   └── Source citation
│   │
│   ├── 📄 tool_router.py        # 🔧 Tool Selection Node
│   │   ├── Connector selection
│   │   ├── Tool capability matching
│   │   ├── Permission checking
│   │   └── Tool call generation
│   │
│   ├── 📄 executor.py           # ⚡ Action Execution Node
│   │   ├── Tool call execution
│   │   ├── Idempotency handling
│   │   ├── Error recovery
│   │   └── Result processing
│   │
│   ├── 📄 guardrails.py         # 🛡️ Safety & Policy Node
│   │   ├── Policy compliance checking
│   │   ├── Risk assessment
│   │   ├── Approval triggers
│   │   └── Safety validation
│   │
│   ├── 📄 reflector.py          # 🤔 Outcome Analysis Node
│   │   ├── Success evaluation
│   │   ├── Learning extraction
│   │   ├── Memory updates
│   │   └── Improvement suggestions
│   │
│   ├── 📄 scheduler.py          # ⏰ Task Scheduling Node
│   │   ├── Future task scheduling
│   │   ├── Dependency resolution
│   │   ├── Resource optimization
│   │   └── Timeline management
│   │
│   └── 📄 audit_logger.py       # 📋 Audit & Telemetry Node
│       ├── Action logging
│       ├── Cost tracking
│       ├── Performance metrics
│       └── Compliance reporting
│
├── 📁 tools/                     # 🔧 Tool Integrations (NEEDS IMPLEMENTATION)
│   ├── 📄 base.py               # 🔧 Base Tool Interface
│   │   ├── Tool abstraction layer
│   │   ├── Common tool patterns
│   │   ├── Error handling
│   │   └── Result formatting
│   │
│   ├── 📄 gmail.py              # 📧 Gmail Integration
│   │   ├── Email composition
│   │   ├── Thread management
│   │   ├── Label operations
│   │   └── Search and filtering
│   │
│   ├── 📄 calendar.py           # 📅 Calendar Integration
│   │   ├── Event creation
│   │   ├── Availability checking
│   │   ├── Meeting scheduling
│   │   └── Conflict resolution
│   │
│   ├── 📄 slack.py              # 💬 Slack Integration
│   │   ├── Message sending
│   │   ├── Channel management
│   │   ├── Thread operations
│   │   └── File sharing
│   │
│   ├── 📄 notion.py             # 📝 Notion Integration
│   │   ├── Page creation
│   │   ├── Database operations
│   │   ├── Content formatting
│   │   └── Template application
│   │
│   ├── 📄 jira.py               # 🎫 Jira Integration
│   │   ├── Issue creation
│   │   ├── Status updates
│   │   ├── Comment management
│   │   └── Workflow transitions
│   │
│   └── 📄 github.py             # 🐙 GitHub Integration
│       ├── Repository operations
│       ├── Issue management
│       ├── Pull request handling
│       └── Code review assistance
│
├── 📁 memory/                    # 🧠 Memory Management (NEEDS IMPLEMENTATION)
│   ├── 📄 vector_store.py       # 🗄️ Vector Database Operations
│   │   ├── pgvector integration
│   │   ├── Embedding storage
│   │   ├── Similarity search
│   │   └── Index management
│   │
│   ├── 📄 embeddings.py         # 🔤 Embedding Generation
│   │   ├── OpenAI embeddings
│   │   ├── Sentence transformers
│   │   ├── Batch processing
│   │   └── Caching strategies
│   │
│   ├── 📄 retrieval.py          # 🔍 Semantic Search
│   │   ├── Query processing
│   │   ├── Context retrieval
│   │   ├── Relevance ranking
│   │   └── Source attribution
│   │
│   ├── 📄 summarization.py      # 📝 Content Summarization
│   │   ├── Document summarization
│   │   ├── Episode compression
│   │   ├── Incremental updates
│   │   └── Quality assessment
│   │
│   └── 📄 compaction.py         # 🗜️ Memory Compaction
│       ├── Rolling summaries
│       ├── Retention policies
│       ├── Storage optimization
│       └── Archive management
│
├── 📁 config/                    # ⚙️ AI Configuration (NEEDS IMPLEMENTATION)
│   ├── 📄 models.py             # 🤖 Model Configuration
│   │   ├── LLM selection
│   │   ├── Model parameters
│   │   ├── Cost optimization
│   │   └── Fallback strategies
│   │
│   ├── 📄 prompts.py            # 💬 Prompt Templates
│   │   ├── System prompts
│   │   ├── Task-specific prompts
│   │   ├── Error handling prompts
│   │   └── Localization support
│   │
│   └── 📄 policies.py           # 📋 Policy Configuration
│       ├── Safety policies
│       ├── Approval thresholds
│       ├── Cost limits
│       └── Privacy rules
│
└── 📁 utils/                     # 🛠️ AI Utilities (NEEDS IMPLEMENTATION)
    ├── 📄 langsmith.py          # 📊 LangSmith Integration
    │   ├── Tracing setup
    │   ├── Evaluation metrics
    │   ├── Performance monitoring
    │   └── Debugging tools
    │
    ├── 📄 cost_tracking.py      # 💰 Cost Management
    │   ├── Token counting
    │   ├── Cost calculation
    │   ├── Budget enforcement
    │   └── Usage analytics
    │
    └── 📄 validation.py         # ✅ Input Validation
        ├── Schema validation
        ├── Content filtering
        ├── Safety checks
        └── Quality assurance
```

### Configuration Files

```
ai_engine/
├── 📄 requirements.txt           # 🐍 AI/ML Dependencies
│   ├── LangChain and LangGraph
│   ├── OpenAI and Anthropic
│   ├── Vector databases
│   ├── Embedding models
│   ├── Database drivers
│   └── Development tools
│
├── 📄 config.py                  # ⚙️ AI Engine Configuration (NEEDS IMPLEMENTATION)
├── 📄 .env.example               # 🌍 Environment Variables Template
└── 📄 README.md                  # 📖 AI Engine Documentation
```

---

## 🏗️ Infrastructure Structure (`infrastructure/`)

### Docker Configuration

```
infrastructure/
├── 📄 docker-compose.yml         # 🐳 Development Infrastructure
│   ├── PostgreSQL with pgvector
│   ├── Redis for caching
│   ├── MinIO for S3-compatible storage
│   └── LangSmith for AI tracing
│
├── 📁 docker/                    # 🐳 Docker Configuration Files
│   ├── 📄 Dockerfile.backend     # 🐍 Backend Docker Image
│   ├── 📄 Dockerfile.frontend    # ⚛️ Frontend Docker Image
│   ├── 📄 Dockerfile.ai-engine   # 🤖 AI Engine Docker Image
│   └── 📄 docker-compose.prod.yml # 🚀 Production Configuration
│
└── 📁 k8s/                       # ☸️ Kubernetes Configuration (NEEDS IMPLEMENTATION)
    ├── 📄 namespace.yaml         # Namespace definition
    ├── 📄 postgres.yaml          # PostgreSQL deployment
    ├── 📄 redis.yaml             # Redis deployment
    ├── 📄 backend.yaml           # Backend deployment
    ├── 📄 frontend.yaml          # Frontend deployment
    ├── 📄 ai-engine.yaml         # AI engine deployment
    └── 📄 ingress.yaml           # Ingress configuration
```

### Database Initialization

```
infrastructure/
└── 📁 init-scripts/              # 🗄️ Database Setup Scripts
    ├── 📄 01-init.sql           # 🎯 PostgreSQL Initialization
    │   ├── pgvector extension
    │   ├── Custom enum types
    │   ├── SQL functions
    │   ├── Database views
    │   └── Initial data setup
    │
    └── 📄 02-seed.sql           # 🌱 Seed Data (NEEDS IMPLEMENTATION)
        ├── Default tenants
        ├── Sample users
        ├── Test connectors
        └── Example workflows
```

---

## 📚 Documentation Structure (`docs/`)

```
docs/
├── 📄 architecture.md            # 🏗️ System Architecture Guide
├── 📄 api-reference.md           # 📋 API Reference Documentation
├── 📄 deployment.md              # 🚀 Deployment Guide
├── 📄 development.md             # 👨‍💻 Development Setup Guide
├── 📄 testing.md                 # 🧪 Testing Strategy
├── 📄 security.md                # 🔒 Security Guidelines
├── 📄 troubleshooting.md         # 🔧 Troubleshooting Guide
└── 📁 diagrams/                  # 📊 Architecture Diagrams
    ├── 📄 system-overview.png    # System overview diagram
    ├── 📄 data-flow.png          # Data flow diagram
    ├── 📄 api-architecture.png   # API architecture diagram
    └── 📄 deployment-diagram.png # Deployment diagram
```

---

## 🧪 Testing Structure (`tests/`)

```
tests/
├── 📁 e2e/                       # 🧪 End-to-End Tests
│   ├── 📄 auth.spec.ts           # Authentication flow tests
│   ├── 📄 goals.spec.ts          # Goal management tests
│   ├── 📄 runs.spec.ts           # Run execution tests
│   └── 📄 memory.spec.ts         # Memory management tests
│
├── 📁 integration/               # 🔗 Integration Tests
│   ├── 📄 api/                   # API integration tests
│   ├── 📄 database/              # Database integration tests
│   └── 📄 ai-engine/             # AI engine integration tests
│
├── 📁 unit/                      # 🧩 Unit Tests
│   ├── 📄 backend/               # Backend unit tests
│   ├── 📄 frontend/              # Frontend unit tests
│   └── 📄 ai-engine/             # AI engine unit tests
│
└── 📄 fixtures/                  # 🧪 Test Data
    ├── 📄 users.json             # Test user data
    ├── 📄 goals.json             # Test goal data
    └── 📄 documents.json         # Test document data
```

---

## 🛠️ Scripts Structure (`scripts/`)

```
scripts/
├── 📄 setup.sh                   # 🚀 Complete Setup Script
│   ├── Prerequisites checking
│   ├── Environment setup
│   ├── Infrastructure startup
│   ├── Backend setup
│   ├── Frontend setup
│   ├── AI engine setup
│   └── Health checks
│
├── 📄 deploy.sh                  # 🚀 Deployment Script (NEEDS IMPLEMENTATION)
├── 📄 backup.sh                  # 💾 Backup Script (NEEDS IMPLEMENTATION)
├── 📄 migrate.sh                 # 🗄️ Migration Script (NEEDS IMPLEMENTATION)
└── 📄 health-check.sh            # 🏥 Health Check Script (NEEDS IMPLEMENTATION)
```

---

## 📋 Implementation Status Legend

- **✅ COMPLETE** - Fully implemented and functional
- **🔄 IN PROGRESS** - Partially implemented
- **❌ NEEDS IMPLEMENTATION** - Not yet implemented
- **🎯 HIGH PRIORITY** - Should be implemented first
- **📊 MEDIUM PRIORITY** - Important but not critical
- **🔧 LOW PRIORITY** - Nice to have features

---

## 🎯 Quick Navigation for Claude Code

### **Start Here (High Priority):**
1. `backend/app/schemas/` - Create Pydantic schemas
2. `backend/app/crud/` - Implement database operations
3. `backend/app/api/v1/endpoints/` - Complete remaining endpoints
4. `frontend/app/auth/` - Create authentication pages
5. `ai_engine/mindmesh/nodes/` - Implement LangGraph nodes

### **Key Files to Understand:**
- `backend/app/main.py` - Backend entry point
- `frontend/app/layout.tsx` - Frontend root layout
- `ai_engine/mindmesh/graphs/main_graph.py` - AI orchestration
- `backend/app/models/` - Database structure
- `frontend/types/index.ts` - TypeScript definitions

### **Configuration Files:**
- `docker-compose.yml` - Development infrastructure
- `backend/requirements.txt` - Python dependencies
- `frontend/package.json` - Node.js dependencies
- `ai_engine/requirements.txt` - AI/ML dependencies

This repository map provides Claude Code with a comprehensive understanding of the codebase structure, implementation status, and clear guidance on what needs to be built next.
