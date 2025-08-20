// API Response Types
export interface ApiResponse<T = any> {
  data: T
  message?: string
  success: boolean
}

export interface PaginatedResponse<T> {
  items: T[]
  total: number
  page: number
  size: number
  pages: number
}

// Authentication Types
export interface LoginRequest {
  email: string
  password: string
}

export interface LoginResponse {
  access_token: string
  refresh_token: string
  token_type: string
  expires_in: number
  user: User
}

export interface RegisterRequest {
  email: string
  username: string
  password: string
  full_name: string
}

export interface RefreshTokenRequest {
  refresh_token: string
}

// User Types
export interface User {
  id: string
  tenant_id: string
  email: string
  username: string
  full_name: string
  role: string
  permissions: string[]
  settings: Record<string, any>
  is_active: boolean
  is_verified: boolean
  last_login: string
  created_at: string
  updated_at: string
}

export interface Tenant {
  id: string
  name: string
  slug: string
  domain: string
  settings: Record<string, any>
  is_active: boolean
  created_at: string
  updated_at: string
}

// Goal Types
export interface Goal {
  id: string
  tenant_id: string
  created_by: string
  text: string
  autonomy_level: 'L0' | 'L1' | 'L2' | 'L3'
  constraints: Record<string, any>
  status: 'draft' | 'active' | 'completed' | 'cancelled'
  priority: 'low' | 'medium' | 'high' | 'urgent'
  due_date: string | null
  estimated_hours: number | null
  actual_hours: number | null
  metadata: Record<string, any>
  created_at: string
  updated_at: string
  tasks: Task[]
  runs: Run[]
}

export interface Task {
  id: string
  goal_id: string
  title: string
  description: string
  status: 'pending' | 'in_progress' | 'completed' | 'blocked'
  assignee: string | null
  due_date: string | null
  priority: 'low' | 'medium' | 'high' | 'urgent'
  estimated_hours: number | null
  actual_hours: number | null
  dependencies: string[]
  tool_refs: string[]
  metadata: Record<string, any>
  created_at: string
  updated_at: string
}

// Run Types
export interface Run {
  id: string
  tenant_id: string
  goal_id: string
  created_by: string
  graph_version: string
  status: 'pending' | 'running' | 'completed' | 'failed' | 'paused'
  current_node: string | null
  checkpoints: Record<string, any>
  artifacts: Record<string, any>
  cost: number
  metrics: Record<string, any>
  error_message: string | null
  started_at: string | null
  completed_at: string | null
  created_at: string
  updated_at: string
  goal: Goal
  approvals: Approval[]
}

export interface Approval {
  id: string
  run_id: string
  decided_by: string | null
  payload: Record<string, any>
  state: 'pending' | 'approved' | 'rejected' | 'edited'
  decision: 'approve' | 'reject' | 'edit' | null
  comments: string | null
  created_at: string
  decided_at: string | null
  updated_at: string
}

// Connector Types
export interface Connector {
  id: string
  tenant_id: string
  provider: string
  name: string
  scopes: string[]
  credentials: Record<string, any>
  status: 'active' | 'inactive' | 'error' | 'syncing'
  last_sync: string | null
  sync_frequency: number
  settings: Record<string, any>
  is_enabled: boolean
  created_at: string
  updated_at: string
}

// Memory Types
export interface Document {
  id: string
  tenant_id: string
  source_uri: string
  app: string
  owner: string
  title: string
  content: string
  mime_type: string
  file_size: number
  hash: string
  vector: number[]
  metadata: Record<string, any>
  sensitivity: 'public' | 'private' | 'confidential'
  ttl_days: number | null
  is_indexed: boolean
  created_at: string
  updated_at: string
}

export interface Episode {
  id: string
  tenant_id: string
  type: 'email' | 'meeting' | 'call' | 'note'
  title: string
  summary: string
  content: string
  participants: string[]
  start_time: string | null
  end_time: string | null
  duration_minutes: number | null
  source_uri: string
  vector: number[]
  metadata: Record<string, any>
  tags: string[]
  created_at: string
  updated_at: string
}

export interface Entity {
  id: string
  tenant_id: string
  type: 'person' | 'organization' | 'project' | 'topic'
  name: string
  description: string
  attributes: Record<string, any>
  relations: Record<string, any>
  vector: number[]
  metadata: Record<string, any>
  is_active: boolean
  created_at: string
  updated_at: string
}

// Automation Types
export interface Automation {
  id: string
  tenant_id: string
  name: string
  description: string
  trigger: AutomationTrigger
  workflow: AutomationWorkflow
  is_active: boolean
  created_at: string
  updated_at: string
}

export interface AutomationTrigger {
  type: 'topic_watch' | 'inbox_label' | 'folder_change' | 'time' | 'webhook'
  config: Record<string, any>
}

export interface AutomationWorkflow {
  template: string
  parameters: Record<string, any>
}

// Audit Types
export interface AuditLog {
  id: string
  tenant_id: string
  user_id: string | null
  action: string
  resource_type: string
  resource_id: string
  details: Record<string, any>
  ip_address: string
  user_agent: string
  success: boolean
  error_message: string | null
  created_at: string
}

// Form Types
export interface GoalFormData {
  text: string
  autonomy_level: 'L0' | 'L1' | 'L2' | 'L3'
  constraints: Record<string, any>
  priority: 'low' | 'medium' | 'high' | 'urgent'
  due_date: string | null
  estimated_hours: number | null
}

export interface ConnectorFormData {
  provider: string
  name: string
  scopes: string[]
  settings: Record<string, any>
}

// UI Types
export interface SidebarItem {
  id: string
  label: string
  icon: string
  href: string
  badge?: string | number
  children?: SidebarItem[]
}

export interface TableColumn<T = any> {
  key: string
  label: string
  sortable?: boolean
  render?: (value: any, row: T) => React.ReactNode
  width?: string
}

export interface FilterOption {
  label: string
  value: string
  count?: number
}

export interface SortOption {
  key: string
  direction: 'asc' | 'desc'
}

// WebSocket Types
export interface WebSocketMessage {
  type: string
  payload: any
  timestamp: string
}

export interface RunUpdateMessage {
  run_id: string
  status: string
  current_node: string
  progress: number
  artifacts: Record<string, any>
}

export interface ApprovalRequestMessage {
  approval_id: string
  run_id: string
  payload: Record<string, any>
  deadline: string
}

// Error Types
export interface ApiError {
  detail: string
  status_code: number
  type: string
}

export interface ValidationError {
  field: string
  message: string
}

// Search Types
export interface SearchFilters {
  query?: string
  type?: string[]
  date_from?: string
  date_to?: string
  sensitivity?: string[]
  tags?: string[]
  owner?: string[]
}

export interface SearchResult<T> {
  item: T
  score: number
  highlights: Record<string, string[]>
}

// Chart Types
export interface ChartData {
  labels: string[]
  datasets: {
    label: string
    data: number[]
    backgroundColor?: string
    borderColor?: string
  }[]
}

export interface MetricCard {
  title: string
  value: string | number
  change?: number
  changeType?: 'increase' | 'decrease'
  icon?: string
}
