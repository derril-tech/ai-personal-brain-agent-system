"""
MindMesh Main LangGraph Orchestration
"""

from typing import Dict, Any, List
from langgraph.graph import StateGraph, END
from langgraph.checkpoint.memory import MemorySaver

from mindmesh.nodes.intent_router import IntentRouter
from mindmesh.nodes.planner import Planner
from mindmesh.nodes.memory_reader import MemoryReader
from mindmesh.nodes.tool_router import ToolRouter
from mindmesh.nodes.executor import Executor
from mindmesh.nodes.guardrails import Guardrails
from mindmesh.nodes.reflector import Reflector
from mindmesh.nodes.scheduler import Scheduler
from mindmesh.nodes.audit import AuditLogger
from mindmesh.state import MindMeshState


class MindMeshGraph:
    """Main orchestration graph for MindMesh"""
    
    def __init__(self):
        self.graph = self._build_graph()
        self.memory = MemorySaver()
        self.app = self.graph.compile(checkpointer=self.memory)
    
    def _build_graph(self) -> StateGraph:
        """Build the main orchestration graph"""
        
        # Create the graph
        workflow = StateGraph(MindMeshState)
        
        # Add nodes
        workflow.add_node("intent_router", IntentRouter())
        workflow.add_node("planner", Planner())
        workflow.add_node("memory_reader", MemoryReader())
        workflow.add_node("tool_router", ToolRouter())
        workflow.add_node("executor", Executor())
        workflow.add_node("guardrails", Guardrails())
        workflow.add_node("reflector", Reflector())
        workflow.add_node("scheduler", Scheduler())
        workflow.add_node("audit_logger", AuditLogger())
        
        # Define edges
        workflow.set_entry_point("intent_router")
        
        # Intent routing
        workflow.add_edge("intent_router", "planner")
        
        # Planning phase
        workflow.add_edge("planner", "memory_reader")
        
        # Memory retrieval
        workflow.add_edge("memory_reader", "tool_router")
        
        # Tool routing
        workflow.add_edge("tool_router", "guardrails")
        
        # Guardrails check
        workflow.add_conditional_edges(
            "guardrails",
            self._check_guardrails,
            {
                "approved": "executor",
                "needs_approval": "audit_logger",
                "rejected": "reflector"
            }
        )
        
        # Execution
        workflow.add_edge("executor", "reflector")
        
        # Reflection and memory update
        workflow.add_edge("reflector", "scheduler")
        
        # Scheduling and monitoring
        workflow.add_edge("scheduler", "audit_logger")
        
        # Final audit logging
        workflow.add_edge("audit_logger", END)
        
        return workflow
    
    def _check_guardrails(self, state: MindMeshState) -> str:
        """Check guardrails and determine next step"""
        if state.guardrails_status == "approved":
            return "approved"
        elif state.guardrails_status == "needs_approval":
            return "needs_approval"
        else:
            return "rejected"
    
    async def run(self, goal_text: str, autonomy_level: str = "L1", **kwargs) -> Dict[str, Any]:
        """Run the MindMesh workflow"""
        
        # Initialize state
        initial_state = MindMeshState(
            goal_text=goal_text,
            autonomy_level=autonomy_level,
            **kwargs
        )
        
        # Run the graph
        config = {"configurable": {"thread_id": f"goal_{hash(goal_text)}"}}
        result = await self.app.ainvoke(initial_state, config)
        
        return result
    
    def get_checkpoint(self, thread_id: str) -> Dict[str, Any]:
        """Get checkpoint for a specific thread"""
        return self.memory.get(config={"configurable": {"thread_id": thread_id}})
    
    async def resume(self, thread_id: str, **kwargs) -> Dict[str, Any]:
        """Resume execution from checkpoint"""
        config = {"configurable": {"thread_id": thread_id}}
        result = await self.app.ainvoke(kwargs, config)
        return result


# Global graph instance
mindmesh_graph = MindMeshGraph()
