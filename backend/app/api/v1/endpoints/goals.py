"""
Goals Endpoints
"""

from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.core.database import get_db
from app.core.auth import get_current_user
from app.schemas.goal import (
    GoalCreate,
    GoalUpdate,
    GoalResponse,
    GoalList,
)
from app.models.user import User
from app.models.goal import Goal

router = APIRouter()


@router.post("/", response_model=GoalResponse)
async def create_goal(
    goal_in: GoalCreate,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
) -> Any:
    """Create a new goal"""
    goal = Goal(
        tenant_id=current_user.tenant_id,
        created_by=current_user.id,
        text=goal_in.text,
        autonomy_level=goal_in.autonomy_level,
        constraints=goal_in.constraints,
        priority=goal_in.priority,
        due_date=goal_in.due_date,
        estimated_hours=goal_in.estimated_hours,
        metadata=goal_in.metadata,
    )
    
    db.add(goal)
    await db.commit()
    await db.refresh(goal)
    
    return goal


@router.get("/", response_model=GoalList)
async def list_goals(
    skip: int = 0,
    limit: int = 100,
    status: str = None,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
) -> Any:
    """List user goals"""
    query = select(Goal).where(Goal.tenant_id == current_user.tenant_id)
    
    if status:
        query = query.where(Goal.status == status)
    
    query = query.offset(skip).limit(limit)
    result = await db.execute(query)
    goals = result.scalars().all()
    
    return {"goals": goals, "total": len(goals)}


@router.get("/{goal_id}", response_model=GoalResponse)
async def get_goal(
    goal_id: int,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
) -> Any:
    """Get a specific goal"""
    goal = await db.get(Goal, goal_id)
    if not goal or goal.tenant_id != current_user.tenant_id:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Goal not found",
        )
    
    return goal


@router.put("/{goal_id}", response_model=GoalResponse)
async def update_goal(
    goal_id: int,
    goal_in: GoalUpdate,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
) -> Any:
    """Update a goal"""
    goal = await db.get(Goal, goal_id)
    if not goal or goal.tenant_id != current_user.tenant_id:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Goal not found",
        )
    
    # Update goal fields
    for field, value in goal_in.dict(exclude_unset=True).items():
        setattr(goal, field, value)
    
    await db.commit()
    await db.refresh(goal)
    
    return goal


@router.delete("/{goal_id}")
async def delete_goal(
    goal_id: int,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
) -> Any:
    """Delete a goal"""
    goal = await db.get(Goal, goal_id)
    if not goal or goal.tenant_id != current_user.tenant_id:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Goal not found",
        )
    
    await db.delete(goal)
    await db.commit()
    
    return {"message": "Goal deleted successfully"}
