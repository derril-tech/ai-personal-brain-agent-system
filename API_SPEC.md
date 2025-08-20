# 📋 MindMesh API Specification

## 🌐 Base URL
```
Development: http://localhost:8000
Production: https://api.mindmesh.com
```

## 🔐 Authentication

### JWT Token Authentication
All API endpoints (except authentication endpoints) require a valid JWT access token in the Authorization header:

```
Authorization: Bearer <access_token>
```

### Token Types
- **Access Token**: Short-lived (15 minutes), used for API requests
- **Refresh Token**: Long-lived (7 days), used to obtain new access tokens

---

## 📚 API Endpoints

### 🔐 Authentication Endpoints

#### POST `/auth/login`
Authenticate user and obtain access/refresh tokens.

**Request Body:**
```json
{
  "email": "user@example.com",
  "password": "secure_password"
}
```

**Response:**
```json
{
  "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
  "refresh_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
  "token_type": "bearer",
  "expires_in": 900,
  "user": {
    "id": "user_123",
    "email": "user@example.com",
    "username": "johndoe",
    "full_name": "John Doe",
    "role": "user",
    "permissions": ["read:goals", "write:goals"],
    "is_active": true,
    "is_verified": true
  }
}
```

#### POST `/auth/register`
Register a new user account.

**Request Body:**
```json
{
  "email": "newuser@example.com",
  "username": "newuser",
  "password": "secure_password",
  "full_name": "New User"
}
```

**Response:**
```json
{
  "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
  "refresh_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
  "token_type": "bearer",
  "expires_in": 900,
  "user": {
    "id": "user_456",
    "email": "newuser@example.com",
    "username": "newuser",
    "full_name": "New User",
    "role": "user",
    "permissions": ["read:goals", "write:goals"],
    "is_active": true,
    "is_verified": false
  }
}
```

#### POST `/auth/refresh`
Refresh access token using refresh token.

**Request Body:**
```json
{
  "refresh_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..."
}
```

**Response:**
```json
{
  "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
  "refresh_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
  "token_type": "bearer",
  "expires_in": 900
}
```

#### GET `/auth/me`
Get current user information.

**Response:**
```json
{
  "id": "user_123",
  "tenant_id": "tenant_456",
  "email": "user@example.com",
  "username": "johndoe",
  "full_name": "John Doe",
  "role": "user",
  "permissions": ["read:goals", "write:goals", "read:runs"],
  "settings": {
    "theme": "dark",
    "notifications": true,
    "autonomy_level": "L2"
  },
  "is_active": true,
  "is_verified": true,
  "last_login": "2024-01-15T10:30:00Z",
  "created_at": "2024-01-01T00:00:00Z",
  "updated_at": "2024-01-15T10:30:00Z"
}
```

---

### 🎯 Goals Management Endpoints

#### GET `/goals`
List user goals with filtering and pagination.

**Query Parameters:**
- `page` (int, default: 1): Page number
- `size` (int, default: 20): Items per page
- `status` (string): Filter by status (draft, active, completed, cancelled)
- `priority` (string): Filter by priority (low, medium, high, urgent)
- `search` (string): Search in goal text
- `autonomy_level` (string): Filter by autonomy level (L0, L1, L2, L3)

**Response:**
```json
{
  "items": [
    {
      "id": "goal_123",
      "tenant_id": "tenant_456",
      "created_by": "user_123",
      "text": "Plan and execute product launch for Q2",
      "autonomy_level": "L2",
      "constraints": {
        "budget": 50000,
        "deadline": "2024-06-30"
      },
      "status": "active",
      "priority": "high",
      "due_date": "2024-06-30T23:59:59Z",
      "estimated_hours": 80,
      "actual_hours": 45,
      "metadata": {
        "category": "product",
        "team_size": 5
      },
      "created_at": "2024-01-15T10:00:00Z",
      "updated_at": "2024-01-20T15:30:00Z",
      "tasks": [
        {
          "id": "task_789",
          "title": "Market research",
          "status": "completed",
          "priority": "high"
        }
      ]
    }
  ],
  "total": 25,
  "page": 1,
  "size": 20,
  "pages": 2
}
```

#### POST `/goals`
Create a new goal.

**Request Body:**
```json
{
  "text": "Research and implement new AI features",
  "autonomy_level": "L2",
  "constraints": {
    "budget": 25000,
    "team": ["user_123", "user_456"]
  },
  "priority": "medium",
  "due_date": "2024-03-31T23:59:59Z",
  "estimated_hours": 60
}
```

**Response:**
```json
{
  "id": "goal_789",
  "tenant_id": "tenant_456",
  "created_by": "user_123",
  "text": "Research and implement new AI features",
  "autonomy_level": "L2",
  "constraints": {
    "budget": 25000,
    "team": ["user_123", "user_456"]
  },
  "status": "draft",
  "priority": "medium",
  "due_date": "2024-03-31T23:59:59Z",
  "estimated_hours": 60,
  "actual_hours": null,
  "metadata": {},
  "created_at": "2024-01-21T14:00:00Z",
  "updated_at": "2024-01-21T14:00:00Z"
}
```

#### GET `/goals/{goal_id}`
Get a specific goal by ID.

**Response:**
```json
{
  "id": "goal_123",
  "tenant_id": "tenant_456",
  "created_by": "user_123",
  "text": "Plan and execute product launch for Q2",
  "autonomy_level": "L2",
  "constraints": {
    "budget": 50000,
    "deadline": "2024-06-30"
  },
  "status": "active",
  "priority": "high",
  "due_date": "2024-06-30T23:59:59Z",
  "estimated_hours": 80,
  "actual_hours": 45,
  "metadata": {
    "category": "product",
    "team_size": 5
  },
  "created_at": "2024-01-15T10:00:00Z",
  "updated_at": "2024-01-20T15:30:00Z",
  "tasks": [
    {
      "id": "task_789",
      "goal_id": "goal_123",
      "title": "Market research",
      "description": "Conduct comprehensive market analysis",
      "status": "completed",
      "assignee": "user_123",
      "due_date": "2024-01-25T23:59:59Z",
      "priority": "high",
      "estimated_hours": 8,
      "actual_hours": 6,
      "dependencies": [],
      "tool_refs": ["gmail", "calendar"],
      "metadata": {},
      "created_at": "2024-01-15T10:00:00Z",
      "updated_at": "2024-01-20T15:30:00Z"
    }
  ],
  "runs": [
    {
      "id": "run_456",
      "status": "completed",
      "current_node": null,
      "cost": 12.50,
      "started_at": "2024-01-15T10:00:00Z",
      "completed_at": "2024-01-15T10:30:00Z"
    }
  ]
}
```

#### PUT `/goals/{goal_id}`
Update a goal.

**Request Body:**
```json
{
  "text": "Updated goal description",
  "priority": "urgent",
  "due_date": "2024-04-15T23:59:59Z",
  "estimated_hours": 100
}
```

#### DELETE `/goals/{goal_id}`
Delete a goal.

**Response:**
```json
{
  "message": "Goal deleted successfully"
}
```

#### POST `/goals/{goal_id}/start`
Start goal execution.

**Response:**
```json
{
  "run_id": "run_789",
  "message": "Goal execution started"
}
```

---

### 🏃 Run Execution Endpoints

#### GET `/runs`
List run executions with filtering.

**Query Parameters:**
- `page` (int, default: 1): Page number
- `size` (int, default: 20): Items per page
- `status` (string): Filter by status (pending, running, completed, failed, paused)
- `goal_id` (string): Filter by goal ID
- `created_by` (string): Filter by creator

**Response:**
```json
{
  "items": [
    {
      "id": "run_123",
      "tenant_id": "tenant_456",
      "goal_id": "goal_789",
      "created_by": "user_123",
      "graph_version": "1.0.0",
      "status": "running",
      "current_node": "planner",
      "checkpoints": {
        "intent_router": {
          "completed_at": "2024-01-21T14:00:00Z",
          "result": {
            "intent": "research",
            "autonomy_level": "L2"
          }
        }
      },
      "artifacts": {
        "research_summary": "file://artifacts/research_123.pdf"
      },
      "cost": 8.75,
      "metrics": {
        "tokens_used": 1500,
        "api_calls": 12,
        "execution_time": 1800
      },
      "error_message": null,
      "started_at": "2024-01-21T14:00:00Z",
      "completed_at": null,
      "created_at": "2024-01-21T14:00:00Z",
      "updated_at": "2024-01-21T14:15:00Z"
    }
  ],
  "total": 15,
  "page": 1,
  "size": 20,
  "pages": 1
}
```

#### GET `/runs/{run_id}`
Get a specific run by ID.

**Response:**
```json
{
  "id": "run_123",
  "tenant_id": "tenant_456",
  "goal_id": "goal_789",
  "created_by": "user_123",
  "graph_version": "1.0.0",
  "status": "running",
  "current_node": "planner",
  "checkpoints": {
    "intent_router": {
      "completed_at": "2024-01-21T14:00:00Z",
      "result": {
        "intent": "research",
        "autonomy_level": "L2"
      }
    },
    "planner": {
      "started_at": "2024-01-21T14:05:00Z",
      "status": "running"
    }
  },
  "artifacts": {
    "research_summary": "file://artifacts/research_123.pdf"
  },
  "cost": 8.75,
  "metrics": {
    "tokens_used": 1500,
    "api_calls": 12,
    "execution_time": 1800
  },
  "error_message": null,
  "started_at": "2024-01-21T14:00:00Z",
  "completed_at": null,
  "created_at": "2024-01-21T14:00:00Z",
  "updated_at": "2024-01-21T14:15:00Z",
  "goal": {
    "id": "goal_789",
    "text": "Research and implement new AI features",
    "status": "active"
  },
  "approvals": [
    {
      "id": "approval_456",
      "state": "pending",
      "payload": {
        "action": "send_email",
        "recipients": ["client@example.com"],
        "subject": "Project Update"
      },
      "deadline": "2024-01-21T16:00:00Z"
    }
  ]
}
```

#### POST `/runs/{run_id}/pause`
Pause a running execution.

**Response:**
```json
{
  "message": "Run paused successfully"
}
```

#### POST `/runs/{run_id}/resume`
Resume a paused execution.

**Response:**
```json
{
  "message": "Run resumed successfully"
}
```

#### DELETE `/runs/{run_id}`
Cancel a run execution.

**Response:**
```json
{
  "message": "Run cancelled successfully"
}
```

---

### ✅ Approval Workflow Endpoints

#### GET `/approvals`
List pending approvals.

**Query Parameters:**
- `page` (int, default: 1): Page number
- `size` (int, default: 20): Items per page
- `state` (string): Filter by state (pending, approved, rejected, edited)
- `run_id` (string): Filter by run ID

**Response:**
```json
{
  "items": [
    {
      "id": "approval_123",
      "run_id": "run_456",
      "decided_by": null,
      "payload": {
        "action": "send_email",
        "recipients": ["client@example.com"],
        "subject": "Project Update",
        "body": "Here's the latest update on your project..."
      },
      "state": "pending",
      "decision": null,
      "comments": null,
      "created_at": "2024-01-21T14:00:00Z",
      "decided_at": null,
      "updated_at": "2024-01-21T14:00:00Z"
    }
  ],
  "total": 5,
  "page": 1,
  "size": 20,
  "pages": 1
}
```

#### GET `/approvals/{approval_id}`
Get a specific approval by ID.

**Response:**
```json
{
  "id": "approval_123",
  "run_id": "run_456",
  "decided_by": null,
  "payload": {
    "action": "send_email",
    "recipients": ["client@example.com"],
    "subject": "Project Update",
    "body": "Here's the latest update on your project..."
  },
  "state": "pending",
  "decision": null,
  "comments": null,
  "created_at": "2024-01-21T14:00:00Z",
  "decided_at": null,
  "updated_at": "2024-01-21T14:00:00Z",
  "run": {
    "id": "run_456",
    "goal_id": "goal_789",
    "status": "paused"
  }
}
```

#### POST `/approvals/{approval_id}`
Submit approval decision.

**Request Body:**
```json
{
  "decision": "approve",
  "comments": "Looks good, proceed with sending the email"
}
```

**Response:**
```json
{
  "message": "Approval decision submitted successfully"
}
```

---

### 🔗 Connector Management Endpoints

#### GET `/connectors`
List configured connectors.

**Response:**
```json
{
  "items": [
    {
      "id": "connector_123",
      "tenant_id": "tenant_456",
      "provider": "gmail",
      "name": "Work Email",
      "scopes": ["https://www.googleapis.com/auth/gmail.send"],
      "status": "active",
      "last_sync": "2024-01-21T13:00:00Z",
      "sync_frequency": 300,
      "settings": {
        "labels": ["MindMesh", "Important"],
        "auto_archive": true
      },
      "is_enabled": true,
      "created_at": "2024-01-15T10:00:00Z",
      "updated_at": "2024-01-21T13:00:00Z"
    }
  ],
  "total": 3,
  "page": 1,
  "size": 20,
  "pages": 1
}
```

#### POST `/connectors/{provider}/oauth/callback`
Handle OAuth2 callback for connector setup.

**Request Body:**
```json
{
  "code": "oauth_authorization_code",
  "state": "csrf_token"
}
```

**Response:**
```json
{
  "connector_id": "connector_456",
  "message": "Connector configured successfully"
}
```

#### PUT `/connectors/{connector_id}`
Update connector configuration.

**Request Body:**
```json
{
  "name": "Updated Connector Name",
  "settings": {
    "labels": ["MindMesh", "Important", "Urgent"],
    "auto_archive": false
  },
  "sync_frequency": 600
}
```

#### DELETE `/connectors/{connector_id}`
Remove a connector.

**Response:**
```json
{
  "message": "Connector removed successfully"
}
```

#### POST `/connectors/{connector_id}/sync`
Trigger manual sync for a connector.

**Response:**
```json
{
  "message": "Sync started successfully",
  "sync_id": "sync_789"
}
```

---

### 🧠 Memory Management Endpoints

#### POST `/memory/upsert`
Add or update documents in memory.

**Request Body:**
```json
{
  "source_uri": "gmail://message/123",
  "app": "gmail",
  "owner": "user@example.com",
  "title": "Project Update Email",
  "content": "Here's the latest update on the project...",
  "mime_type": "text/plain",
  "file_size": 1024,
  "hash": "sha256:abc123...",
  "metadata": {
    "thread_id": "thread_456",
    "labels": ["Important", "Project"]
  },
  "sensitivity": "private",
  "ttl_days": 365
}
```

**Response:**
```json
{
  "document_id": "doc_123",
  "message": "Document indexed successfully"
}
```

#### GET `/memory/search`
Search memory using semantic search.

**Query Parameters:**
- `q` (string): Search query
- `type` (string): Filter by type (document, episode, entity)
- `date_from` (string): Filter by start date
- `date_to` (string): Filter by end date
- `sensitivity` (string): Filter by sensitivity level
- `tags` (string): Filter by tags (comma-separated)
- `owner` (string): Filter by owner
- `limit` (int, default: 10): Number of results

**Response:**
```json
{
  "results": [
    {
      "item": {
        "id": "doc_123",
        "source_uri": "gmail://message/123",
        "app": "gmail",
        "title": "Project Update Email",
        "content": "Here's the latest update on the project...",
        "metadata": {
          "thread_id": "thread_456",
          "labels": ["Important", "Project"]
        },
        "created_at": "2024-01-21T14:00:00Z"
      },
      "score": 0.95,
      "highlights": {
        "content": ["Here's the latest <em>update</em> on the <em>project</em>..."]
      }
    }
  ],
  "total": 25,
  "query": "project update"
}
```

#### GET `/memory/documents`
List documents in memory.

**Query Parameters:**
- `page` (int, default: 1): Page number
- `size` (int, default: 20): Items per page
- `app` (string): Filter by application
- `sensitivity` (string): Filter by sensitivity level
- `is_indexed` (boolean): Filter by indexing status

#### GET `/memory/episodes`
List episodes in memory.

**Query Parameters:**
- `page` (int, default: 1): Page number
- `size` (int, default: 20): Items per page
- `type` (string): Filter by type (email, meeting, call, note)
- `participants` (string): Filter by participants

#### GET `/memory/entities`
List entities in memory.

**Query Parameters:**
- `page` (int, default: 1): Page number
- `size` (int, default: 20): Items per page
- `type` (string): Filter by type (person, organization, project, topic)
- `is_active` (boolean): Filter by active status

---

### 🤖 Automation Workflow Endpoints

#### GET `/automations`
List automation workflows.

**Response:**
```json
{
  "items": [
    {
      "id": "automation_123",
      "tenant_id": "tenant_456",
      "name": "Meeting Follow-up",
      "description": "Automatically create follow-up tasks after meetings",
      "trigger": {
        "type": "calendar",
        "config": {
          "event_types": ["meeting"],
          "keywords": ["follow-up", "action items"]
        }
      },
      "workflow": {
        "template": "meeting_followup",
        "parameters": {
          "task_priority": "medium",
          "due_date_offset": 7
        }
      },
      "is_active": true,
      "created_at": "2024-01-15T10:00:00Z",
      "updated_at": "2024-01-21T14:00:00Z"
    }
  ],
  "total": 5,
  "page": 1,
  "size": 20,
  "pages": 1
}
```

#### POST `/automations`
Create a new automation workflow.

**Request Body:**
```json
{
  "name": "Email Classification",
  "description": "Automatically classify incoming emails",
  "trigger": {
    "type": "gmail",
    "config": {
      "labels": ["INBOX"],
      "keywords": ["urgent", "important"]
    }
  },
  "workflow": {
    "template": "email_classification",
    "parameters": {
      "priority_threshold": 0.8,
      "auto_label": true
    }
  }
}
```

#### PUT `/automations/{automation_id}`
Update automation workflow.

#### DELETE `/automations/{automation_id}`
Delete automation workflow.

#### GET `/automations/templates`
List available workflow templates.

**Response:**
```json
{
  "templates": [
    {
      "id": "meeting_followup",
      "name": "Meeting Follow-up",
      "description": "Create follow-up tasks from meeting notes",
      "parameters": {
        "task_priority": {
          "type": "string",
          "enum": ["low", "medium", "high", "urgent"],
          "default": "medium"
        },
        "due_date_offset": {
          "type": "integer",
          "description": "Days from meeting date",
          "default": 7
        }
      }
    }
  ]
}
```

---

### 📋 Audit and Compliance Endpoints

#### GET `/audit/logs`
List audit logs.

**Query Parameters:**
- `page` (int, default: 1): Page number
- `size` (int, default: 20): Items per page
- `user_id` (string): Filter by user
- `action` (string): Filter by action
- `resource_type` (string): Filter by resource type
- `success` (boolean): Filter by success status
- `date_from` (string): Filter by start date
- `date_to` (string): Filter by end date

**Response:**
```json
{
  "items": [
    {
      "id": "audit_123",
      "tenant_id": "tenant_456",
      "user_id": "user_123",
      "action": "goal.create",
      "resource_type": "goal",
      "resource_id": "goal_789",
      "details": {
        "goal_text": "Research and implement new AI features",
        "autonomy_level": "L2"
      },
      "ip_address": "192.168.1.100",
      "user_agent": "Mozilla/5.0...",
      "success": true,
      "error_message": null,
      "created_at": "2024-01-21T14:00:00Z"
    }
  ],
  "total": 150,
  "page": 1,
  "size": 20,
  "pages": 8
}
```

#### GET `/audit/{run_id}`
Get audit trail for a specific run.

**Response:**
```json
{
  "run_id": "run_123",
  "logs": [
    {
      "timestamp": "2024-01-21T14:00:00Z",
      "node": "intent_router",
      "action": "intent.classify",
      "details": {
        "input": "Research and implement new AI features",
        "output": {
          "intent": "research",
          "confidence": 0.95
        }
      }
    },
    {
      "timestamp": "2024-01-21T14:05:00Z",
      "node": "planner",
      "action": "task.decompose",
      "details": {
        "tasks_created": 5,
        "estimated_duration": "2 weeks"
      }
    }
  ]
}
```

---

## 🔧 Health and System Endpoints

#### GET `/health`
System health check.

**Response:**
```json
{
  "status": "healthy",
  "timestamp": "2024-01-21T14:00:00Z",
  "version": "1.0.0",
  "services": {
    "database": "healthy",
    "redis": "healthy",
    "ai_engine": "healthy"
  }
}
```

#### GET `/metrics`
System metrics.

**Response:**
```json
{
  "requests_per_minute": 150,
  "average_response_time": 250,
  "error_rate": 0.02,
  "active_users": 45,
  "total_goals": 1250,
  "total_runs": 8900,
  "ai_cost_today": 125.50
}
```

---

## 📊 Error Responses

All endpoints may return the following error responses:

### 400 Bad Request
```json
{
  "detail": "Validation error",
  "errors": [
    {
      "field": "email",
      "message": "Invalid email format"
    }
  ]
}
```

### 401 Unauthorized
```json
{
  "detail": "Invalid or expired token"
}
```

### 403 Forbidden
```json
{
  "detail": "Insufficient permissions"
}
```

### 404 Not Found
```json
{
  "detail": "Resource not found"
}
```

### 422 Unprocessable Entity
```json
{
  "detail": "Request validation failed",
  "errors": [
    {
      "field": "autonomy_level",
      "message": "Invalid autonomy level"
    }
  ]
}
```

### 500 Internal Server Error
```json
{
  "detail": "Internal server error",
  "error_id": "err_123"
}
```

---

## 🔄 Rate Limiting

API endpoints are rate-limited to prevent abuse:

- **Authentication endpoints**: 5 requests per minute
- **Read endpoints**: 100 requests per minute
- **Write endpoints**: 20 requests per minute
- **AI-intensive endpoints**: 10 requests per minute

Rate limit headers are included in responses:
```
X-RateLimit-Limit: 100
X-RateLimit-Remaining: 95
X-RateLimit-Reset: 1642771200
```

---

## 📝 Pagination

List endpoints support pagination with the following parameters:

- `page`: Page number (1-based)
- `size`: Items per page (max 100)

Response includes pagination metadata:
```json
{
  "items": [...],
  "total": 1250,
  "page": 1,
  "size": 20,
  "pages": 63
}
```

---

## 🔍 Filtering and Search

Many endpoints support filtering and search:

- **Text search**: Use `search` parameter for full-text search
- **Date ranges**: Use `date_from` and `date_to` parameters
- **Status filters**: Use `status` parameter for state-based filtering
- **Custom filters**: Endpoint-specific filter parameters

---

## 📋 WebSocket Events

Real-time updates are available via WebSocket connections:

### Connection
```
ws://localhost:8000/ws?token=<access_token>
```

### Events

#### Run Status Update
```json
{
  "type": "run.update",
  "data": {
    "run_id": "run_123",
    "status": "running",
    "current_node": "planner",
    "progress": 0.6
  }
}
```

#### Approval Request
```json
{
  "type": "approval.request",
  "data": {
    "approval_id": "approval_123",
    "run_id": "run_456",
    "payload": {
      "action": "send_email",
      "recipients": ["client@example.com"]
    },
    "deadline": "2024-01-21T16:00:00Z"
  }
}
```

#### Goal Completion
```json
{
  "type": "goal.completed",
  "data": {
    "goal_id": "goal_123",
    "run_id": "run_456",
    "summary": "Goal completed successfully",
    "artifacts": ["file://artifacts/summary.pdf"]
  }
}
```

---

This API specification provides Claude Code with comprehensive documentation of all endpoints, request/response formats, authentication requirements, and real-time communication patterns needed to implement the MindMesh system.
