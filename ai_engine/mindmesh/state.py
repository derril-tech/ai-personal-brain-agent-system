"""
MindMesh State Management
"""

from typing import Dict, Any, List, Optional
from datetime import datetime
from pydantic import BaseModel, Field


class MindMeshState(BaseModel):
    """State for MindMesh LangGraph workflow"""
    
    # Goal and context
    goal_text: str = Field(description="The user's goal text")
    autonomy_level: str = Field(default="L1", description="Autonomy level: L0, L1, L2, L3")
    constraints: Optional[Dict[str, Any]] = Field(default=None, description="Goal constraints")
    
    # Intent classification
    intent: Optional[str] = Field(default=None, description="Classified intent")
    intent_confidence: Optional[float] = Field(default=None, description="Intent confidence score")
    
    # Planning
    plan: Optional[List[Dict[str, Any]]] = Field(default=None, description="Generated plan")
    tasks: Optional[List[Dict[str, Any]]] = Field(default=None, description="Decomposed tasks")
    
    # Memory and context
    retrieved_documents: Optional[List[Dict[str, Any]]] = Field(default=None, description="Retrieved documents")
    retrieved_episodes: Optional[List[Dict[str, Any]]] = Field(default=None, description="Retrieved episodes")
    retrieved_entities: Optional[List[Dict[str, Any]]] = Field(default=None, description="Retrieved entities")
    context_summary: Optional[str] = Field(default=None, description="Context summary")
    
    # Tool selection and execution
    selected_tools: Optional[List[str]] = Field(default=None, description="Selected tools")
    tool_calls: Optional[List[Dict[str, Any]]] = Field(default=None, description="Tool calls to execute")
    tool_results: Optional[List[Dict[str, Any]]] = Field(default=None, description="Tool execution results")
    
    # Guardrails and safety
    guardrails_status: str = Field(default="pending", description="Guardrails status")
    guardrails_checks: Optional[List[Dict[str, Any]]] = Field(default=None, description="Guardrails check results")
    approval_required: bool = Field(default=False, description="Whether approval is required")
    approval_payload: Optional[Dict[str, Any]] = Field(default=None, description="Approval payload")
    
    # Execution tracking
    current_step: Optional[str] = Field(default=None, description="Current execution step")
    execution_log: Optional[List[Dict[str, Any]]] = Field(default=None, description="Execution log")
    errors: Optional[List[str]] = Field(default=None, description="Execution errors")
    
    # Reflection and learning
    reflection: Optional[str] = Field(default=None, description="Execution reflection")
    lessons_learned: Optional[List[str]] = Field(default=None, description="Lessons learned")
    memory_updates: Optional[List[Dict[str, Any]]] = Field(default=None, description="Memory updates")
    
    # Scheduling and monitoring
    scheduled_tasks: Optional[List[Dict[str, Any]]] = Field(default=None, description="Scheduled follow-up tasks")
    monitoring_rules: Optional[List[Dict[str, Any]]] = Field(default=None, description="Monitoring rules")
    
    # Audit and telemetry
    audit_log: Optional[List[Dict[str, Any]]] = Field(default=None, description="Audit log entries")
    cost_tracking: Optional[Dict[str, Any]] = Field(default=None, description="Cost tracking")
    performance_metrics: Optional[Dict[str, Any]] = Field(default=None, description="Performance metrics")
    
    # Metadata
    run_id: Optional[str] = Field(default=None, description="Unique run identifier")
    tenant_id: Optional[str] = Field(default=None, description="Tenant identifier")
    user_id: Optional[str] = Field(default=None, description="User identifier")
    created_at: datetime = Field(default_factory=datetime.utcnow, description="Creation timestamp")
    updated_at: datetime = Field(default_factory=datetime.utcnow, description="Last update timestamp")
    
    class Config:
        arbitrary_types_allowed = True
