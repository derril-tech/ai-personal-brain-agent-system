"""
MindMesh API v1 Router
"""

from fastapi import APIRouter

from app.api.v1.endpoints import (
    auth,
    goals,
    runs,
    approvals,
    connectors,
    memory,
    automations,
    audit,
)

api_router = APIRouter()

# Include all endpoint routers
api_router.include_router(auth.router, prefix="/auth", tags=["authentication"])
api_router.include_router(goals.router, prefix="/goals", tags=["goals"])
api_router.include_router(runs.router, prefix="/runs", tags=["runs"])
api_router.include_router(approvals.router, prefix="/approvals", tags=["approvals"])
api_router.include_router(connectors.router, prefix="/connectors", tags=["connectors"])
api_router.include_router(memory.router, prefix="/memory", tags=["memory"])
api_router.include_router(automations.router, prefix="/automations", tags=["automations"])
api_router.include_router(audit.router, prefix="/audit", tags=["audit"])
