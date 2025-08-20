'use client'

import { useGoals } from '@/hooks/useGoals'
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card'
import { Badge } from '@/components/ui/badge'
import { Button } from '@/components/ui/button'
import { cn, formatDate, truncateText } from '@/lib/utils'
import { Target, Clock, CheckCircle, AlertCircle, Play, Plus } from 'lucide-react'
import Link from 'next/link'

export function GoalsOverview() {
  const { useGoalsList } = useGoals()
  const { data: goalsData, isLoading } = useGoalsList({ size: 5 })

  const getStatusIcon = (status: string) => {
    switch (status) {
      case 'active':
        return <Clock className="w-4 h-4 text-blue-500" />
      case 'completed':
        return <CheckCircle className="w-4 h-4 text-green-500" />
      case 'cancelled':
        return <AlertCircle className="w-4 h-4 text-red-500" />
      default:
        return <Target className="w-4 h-4 text-gray-500" />
    }
  }

  const getStatusBadge = (status: string) => {
    switch (status) {
      case 'active':
        return <Badge variant="info">Active</Badge>
      case 'completed':
        return <Badge variant="success">Completed</Badge>
      case 'cancelled':
        return <Badge variant="destructive">Cancelled</Badge>
      case 'draft':
        return <Badge variant="secondary">Draft</Badge>
      default:
        return <Badge variant="outline">{status}</Badge>
    }
  }

  const getPriorityBadge = (priority: string) => {
    switch (priority) {
      case 'urgent':
        return <Badge variant="destructive">Urgent</Badge>
      case 'high':
        return <Badge variant="warning">High</Badge>
      case 'medium':
        return <Badge variant="info">Medium</Badge>
      case 'low':
        return <Badge variant="secondary">Low</Badge>
      default:
        return <Badge variant="outline">{priority}</Badge>
    }
  }

  if (isLoading) {
    return (
      <Card>
        <CardHeader>
          <CardTitle className="flex items-center space-x-2">
            <Target className="w-5 h-5" />
            <span>Goals Overview</span>
          </CardTitle>
        </CardHeader>
        <CardContent>
          <div className="space-y-4">
            {[...Array(3)].map((_, i) => (
              <div key={i} className="animate-pulse">
                <div className="h-4 bg-gray-200 rounded w-3/4 mb-2"></div>
                <div className="h-3 bg-gray-200 rounded w-1/2"></div>
              </div>
            ))}
          </div>
        </CardContent>
      </Card>
    )
  }

  const goals = goalsData?.items || []

  return (
    <Card>
      <CardHeader>
        <div className="flex items-center justify-between">
          <CardTitle className="flex items-center space-x-2">
            <Target className="w-5 h-5" />
            <span>Goals Overview</span>
          </CardTitle>
          <Button size="sm" variant="outline" asChild>
            <Link href="/goals">
              <Plus className="w-4 h-4 mr-1" />
              New Goal
            </Link>
          </Button>
        </div>
      </CardHeader>
      <CardContent>
        {goals.length === 0 ? (
          <div className="text-center py-8">
            <Target className="w-12 h-12 mx-auto mb-4 text-gray-400" />
            <p className="text-lg font-medium text-gray-900 mb-2">No goals yet</p>
            <p className="text-sm text-gray-500 mb-4">
              Create your first goal to get started with MindMesh
            </p>
            <Button asChild>
              <Link href="/goals/new">
                <Plus className="w-4 h-4 mr-2" />
                Create Goal
              </Link>
            </Button>
          </div>
        ) : (
          <div className="space-y-4">
            {goals.map((goal) => (
              <div
                key={goal.id}
                className="p-4 border rounded-lg hover:bg-gray-50 transition-colors"
              >
                <div className="flex items-start justify-between mb-2">
                  <div className="flex items-center space-x-2">
                    {getStatusIcon(goal.status)}
                    <h3 className="font-medium text-gray-900">
                      {truncateText(goal.text, 60)}
                    </h3>
                  </div>
                  <div className="flex items-center space-x-2">
                    {getStatusBadge(goal.status)}
                    {getPriorityBadge(goal.priority)}
                  </div>
                </div>
                
                <div className="flex items-center justify-between text-sm text-gray-500">
                  <div className="flex items-center space-x-4">
                    <span>Autonomy: {goal.autonomy_level}</span>
                    {goal.due_date && (
                      <span>Due: {formatDate(goal.due_date)}</span>
                    )}
                    {goal.estimated_hours && (
                      <span>Est: {goal.estimated_hours}h</span>
                    )}
                  </div>
                  
                  <div className="flex items-center space-x-2">
                    {goal.status === 'draft' && (
                      <Button size="sm" variant="outline">
                        <Play className="w-3 h-3 mr-1" />
                        Start
                      </Button>
                    )}
                    <Button size="sm" variant="ghost" asChild>
                      <Link href={`/goals/${goal.id}`}>View</Link>
                    </Button>
                  </div>
                </div>
              </div>
            ))}
            
            {goalsData && goalsData.total > goals.length && (
              <div className="text-center pt-4">
                <Button variant="outline" asChild>
                  <Link href="/goals">
                    View all {goalsData.total} goals
                  </Link>
                </Button>
              </div>
            )}
          </div>
        )}
      </CardContent>
    </Card>
  )
}
