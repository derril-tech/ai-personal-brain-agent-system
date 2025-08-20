# 🤖 Claude Code Implementation Guide

## 🎯 Welcome to MindMesh!

You are about to implement a **Personal Brain Agent System** - an AI-powered assistant that helps users accomplish complex goals through intelligent orchestration, memory management, and tool integration.

## 📋 Your Mission

Transform this comprehensive scaffold into a fully functional AI agent system that can:
- **Understand user goals** and break them into actionable tasks
- **Access user knowledge** through semantic memory search
- **Execute actions** through integrated tools (Gmail, Calendar, Slack, etc.)
- **Learn and improve** from interactions and outcomes
- **Maintain privacy and security** throughout all operations

---

## 🚀 Implementation Strategy

### **Phase 1: Foundation (High Priority)**
Complete these core components first to establish a working system:

#### 1. **Backend Schemas** (`backend/app/schemas/`)
```bash
# Create Pydantic schemas for all models
backend/app/schemas/
├── auth.py          # User, login, register schemas
├── goals.py         # Goal, task schemas
├── runs.py          # Run execution schemas
├── approvals.py     # Approval workflow schemas
├── connectors.py    # Connector schemas
├── memory.py        # Document, episode, entity schemas
├── automations.py   # Automation schemas
└── audit.py         # Audit log schemas
```

**Key Requirements:**
- Use Pydantic v2 with proper validation
- Include field descriptions for OpenAPI docs
- Add example data for testing
- Implement proper error handling

#### 2. **Database Operations** (`backend/app/crud/`)
```bash
# Implement CRUD operations for all models
backend/app/crud/
├── base.py          # Base CRUD class with common operations
├── auth.py          # User authentication CRUD
├── goals.py         # Goal and task CRUD
├── runs.py          # Run execution CRUD
├── approvals.py     # Approval workflow CRUD
├── connectors.py    # Connector management CRUD
├── memory.py        # Memory operations CRUD
├── automations.py   # Automation CRUD
└── audit.py         # Audit logging CRUD
```

**Key Requirements:**
- Use async SQLAlchemy 2.0 patterns
- Implement proper error handling and logging
- Add tenant isolation for multi-tenancy
- Include pagination and filtering support

#### 3. **API Endpoints** (`backend/app/api/v1/endpoints/`)
Complete the remaining endpoint implementations:
- `runs.py` - Run execution management
- `approvals.py` - Human-in-the-loop approvals
- `connectors.py` - External service integrations
- `memory.py` - Memory management
- `automations.py` - Workflow automation
- `audit.py` - Audit and compliance

#### 4. **Authentication Pages** (`frontend/app/auth/`)
```bash
# Create authentication flow
frontend/app/auth/
├── login/page.tsx           # Login form
├── register/page.tsx        # Registration form
├── forgot-password/page.tsx # Password reset
└── components/              # Auth-specific components
    ├── login-form.tsx
    ├── register-form.tsx
    └── auth-layout.tsx
```

#### 5. **LangGraph Nodes** (`ai_engine/mindmesh/nodes/`)
Implement the core AI orchestration nodes:
- `intent_router.py` - Goal classification and intent extraction
- `planner.py` - Task decomposition and planning
- `memory_reader.py` - Semantic search and context retrieval
- `tool_router.py` - Tool selection and routing
- `executor.py` - Action execution and result processing
- `guardrails.py` - Safety checks and policy enforcement
- `reflector.py` - Outcome analysis and learning
- `scheduler.py` - Task scheduling and timing
- `audit_logger.py` - Audit trail and compliance logging

### **Phase 2: Core Features (Medium Priority)**

#### 6. **Memory Management** (`ai_engine/mindmesh/memory/`)
- `vector_store.py` - pgvector integration for embeddings
- `embeddings.py` - OpenAI/Anthropic embedding generation
- `retrieval.py` - Semantic search and context retrieval
- `summarization.py` - Content summarization and compression
- `compaction.py` - Memory optimization and retention

#### 7. **Tool Integrations** (`ai_engine/mindmesh/tools/`)
- `gmail.py` - Email composition and management
- `calendar.py` - Event scheduling and availability
- `slack.py` - Message sending and channel management
- `notion.py` - Document creation and database operations
- `jira.py` - Issue tracking and project management
- `github.py` - Repository operations and code management

#### 8. **Frontend Components** (`frontend/components/`)
Complete the remaining UI components:
- `ui/` - Additional shadcn/ui components
- `dashboard/` - Dashboard-specific components
- `forms/` - Form components with validation
- `charts/` - Data visualization components

### **Phase 3: Advanced Features (Low Priority)**

#### 9. **Real-time Features**
- WebSocket connections for live updates
- Real-time run status monitoring
- Live approval notifications
- Collaborative features

#### 10. **Advanced Analytics**
- Performance metrics and dashboards
- Cost tracking and optimization
- Usage analytics and insights
- A/B testing framework

---

## 🛠️ Implementation Guidelines

### **Backend Development**

#### **FastAPI Best Practices**
```python
# Use dependency injection
from fastapi import Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

async def get_goals(
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
    page: int = 1,
    size: int = 20
):
    # Implementation
    pass
```

#### **Database Patterns**
```python
# Use async SQLAlchemy 2.0
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

async def get_goals_by_user(
    db: AsyncSession, 
    user_id: str, 
    skip: int = 0, 
    limit: int = 100
) -> List[Goal]:
    query = select(Goal).where(Goal.created_by == user_id).offset(skip).limit(limit)
    result = await db.execute(query)
    return result.scalars().all()
```

#### **Error Handling**
```python
# Comprehensive error handling
from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError

try:
    # Database operation
    pass
except IntegrityError:
    raise HTTPException(status_code=400, detail="Resource already exists")
except Exception as e:
    logger.error(f"Unexpected error: {e}")
    raise HTTPException(status_code=500, detail="Internal server error")
```

### **Frontend Development**

#### **React Patterns**
```typescript
// Use React Query for server state
import { useQuery, useMutation } from '@tanstack/react-query'

const { data: goals, isLoading } = useQuery({
  queryKey: ['goals', filters],
  queryFn: () => apiClient.get('/goals', { params: filters })
})

const createGoal = useMutation({
  mutationFn: (data: GoalFormData) => apiClient.post('/goals', data),
  onSuccess: () => {
    queryClient.invalidateQueries({ queryKey: ['goals'] })
    toast.success('Goal created successfully!')
  }
})
```

#### **Component Structure**
```typescript
// Follow component composition patterns
interface GoalCardProps {
  goal: Goal
  onEdit?: (goal: Goal) => void
  onDelete?: (goalId: string) => void
}

export function GoalCard({ goal, onEdit, onDelete }: GoalCardProps) {
  return (
    <Card>
      <CardHeader>
        <CardTitle>{goal.text}</CardTitle>
        <GoalStatusBadge status={goal.status} />
      </CardHeader>
      <CardContent>
        <GoalProgress goal={goal} />
      </CardContent>
      <CardFooter>
        <Button onClick={() => onEdit?.(goal)}>Edit</Button>
        <Button variant="destructive" onClick={() => onDelete?.(goal.id)}>
          Delete
        </Button>
      </CardFooter>
    </Card>
  )
}
```

### **AI Engine Development**

#### **LangGraph Node Pattern**
```python
# Standard node structure
from langgraph.graph import StateGraph
from typing import Dict, Any

def intent_router(state: Dict[str, Any]) -> Dict[str, Any]:
    """Classify user intent and determine autonomy level."""
    try:
        # Extract goal text from state
        goal_text = state.get("goal_text", "")
        
        # Use LLM to classify intent
        intent_result = classify_intent(goal_text)
        
        # Update state with classification results
        state["intent"] = intent_result["intent"]
        state["autonomy_level"] = intent_result["autonomy_level"]
        state["confidence"] = intent_result["confidence"]
        
        return state
    except Exception as e:
        logger.error(f"Intent router error: {e}")
        state["error"] = str(e)
        return state
```

#### **Tool Integration Pattern**
```python
# Standard tool structure
from langchain.tools import BaseTool
from typing import Optional

class GmailSendTool(BaseTool):
    name = "gmail_send"
    description = "Send an email using Gmail"
    
    def _run(self, to: str, subject: str, body: str) -> str:
        try:
            # Implement Gmail sending logic
            result = send_gmail(to, subject, body)
            return f"Email sent successfully to {to}"
        except Exception as e:
            return f"Failed to send email: {str(e)}"
    
    async def _arun(self, to: str, subject: str, body: str) -> str:
        # Async implementation
        return await self._run(to, subject, body)
```

---

## 🧪 Testing Strategy

### **Backend Testing**
```python
# Unit tests for endpoints
import pytest
from fastapi.testclient import TestClient

def test_create_goal(client: TestClient, auth_headers: dict):
    response = client.post(
        "/goals",
        json={
            "text": "Test goal",
            "autonomy_level": "L2",
            "priority": "medium"
        },
        headers=auth_headers
    )
    assert response.status_code == 200
    data = response.json()
    assert data["text"] == "Test goal"
```

### **Frontend Testing**
```typescript
// Component tests
import { render, screen, fireEvent } from '@testing-library/react'
import { GoalCard } from './GoalCard'

test('renders goal information', () => {
  const goal = { id: '1', text: 'Test Goal', status: 'active' }
  render(<GoalCard goal={goal} />)
  
  expect(screen.getByText('Test Goal')).toBeInTheDocument()
  expect(screen.getByText('active')).toBeInTheDocument()
})
```

### **AI Engine Testing**
```python
# Node testing
def test_intent_router():
    state = {"goal_text": "Research AI trends"}
    result = intent_router(state)
    
    assert "intent" in result
    assert "autonomy_level" in result
    assert result["intent"] == "research"
```

---

## 🔒 Security Considerations

### **Authentication & Authorization**
- Implement proper JWT token validation
- Use role-based access control (RBAC)
- Validate all user inputs
- Implement rate limiting

### **Data Privacy**
- Encrypt sensitive data at rest
- Use secure communication (HTTPS/WSS)
- Implement data retention policies
- Add audit logging for compliance

### **AI Safety**
- Validate all LLM inputs and outputs
- Implement content filtering
- Add approval gates for sensitive actions
- Monitor for prompt injection attempts

---

## 📊 Performance Optimization

### **Database Optimization**
- Use proper indexing for frequently queried fields
- Implement connection pooling
- Add query optimization and caching
- Use database migrations for schema changes

### **Frontend Optimization**
- Implement code splitting and lazy loading
- Use React Query for efficient caching
- Optimize bundle size with tree shaking
- Add service worker for offline support

### **AI Engine Optimization**
- Implement embedding caching
- Use batch processing for vector operations
- Add cost tracking and optimization
- Implement retry logic with exponential backoff

---

## 🚀 Deployment Checklist

### **Environment Setup**
- [ ] Configure all environment variables
- [ ] Set up database migrations
- [ ] Configure SSL certificates
- [ ] Set up monitoring and logging

### **Security Configuration**
- [ ] Enable security headers
- [ ] Configure CORS properly
- [ ] Set up rate limiting
- [ ] Enable audit logging

### **Performance Configuration**
- [ ] Configure connection pooling
- [ ] Set up caching layers
- [ ] Enable compression
- [ ] Configure CDN for static assets

---

## 🎯 Success Criteria

### **Functional Requirements**
- [ ] Users can create and manage goals
- [ ] AI can understand and decompose goals into tasks
- [ ] System can execute actions through integrated tools
- [ ] Memory system provides relevant context
- [ ] Approval workflow functions correctly
- [ ] Real-time updates work properly

### **Non-Functional Requirements**
- [ ] System responds within 2 seconds for most operations
- [ ] 99.9% uptime for production deployment
- [ ] Proper error handling and user feedback
- [ ] Comprehensive audit trail
- [ ] GDPR compliance for data handling

---

## 🆘 Getting Help

### **Documentation References**
- `REPO_MAP.md` - Complete repository structure
- `API_SPEC.md` - Detailed API documentation
- `README.md` - Project overview and setup

### **Key Files to Reference**
- `backend/app/models/` - Database schema definitions
- `frontend/types/index.ts` - TypeScript type definitions
- `ai_engine/mindmesh/state.py` - LangGraph state management
- `docker-compose.yml` - Development infrastructure

### **Implementation Patterns**
- Follow the established patterns in existing files
- Use the provided utility functions and components
- Maintain consistency with the existing codebase
- Add comprehensive error handling and logging

---

## 🎉 You're Ready!

You now have everything you need to build MindMesh:

1. **Complete scaffold** with 80% of the foundation
2. **Clear implementation priorities** and guidelines
3. **Comprehensive documentation** and specifications
4. **Established patterns** and best practices

**Start with Phase 1** and build incrementally. Each component you complete will bring the system closer to being a fully functional AI agent that can help users accomplish their goals intelligently and securely.

**Good luck, and happy coding! 🚀**
