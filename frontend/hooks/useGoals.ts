import { useMutation, useQuery, useQueryClient } from '@tanstack/react-query'
import { toast } from 'react-hot-toast'
import { apiClient } from '@/lib/api'
import type { Goal, GoalFormData, PaginatedResponse } from '@/types'

export function useGoals() {
  const queryClient = useQueryClient()

  // Get goals list
  const useGoalsList = (params?: {
    page?: number
    size?: number
    status?: string
    priority?: string
    search?: string
  }) => {
    return useQuery({
      queryKey: ['goals', params],
      queryFn: () =>
        apiClient.get<PaginatedResponse<Goal>>('/goals', { params }),
      keepPreviousData: true,
    })
  }

  // Get single goal
  const useGoal = (goalId: string) => {
    return useQuery({
      queryKey: ['goals', goalId],
      queryFn: () => apiClient.get<Goal>(`/goals/${goalId}`),
      enabled: !!goalId,
    })
  }

  // Create goal mutation
  const createGoalMutation = useMutation({
    mutationFn: (data: GoalFormData) => apiClient.post<Goal>('/goals', data),
    onSuccess: (data) => {
      queryClient.invalidateQueries({ queryKey: ['goals'] })
      queryClient.setQueryData(['goals', data.id], data)
      toast.success('Goal created successfully!')
    },
    onError: (error: any) => {
      const message = error.response?.data?.detail || 'Failed to create goal'
      toast.error(message)
    },
  })

  // Update goal mutation
  const updateGoalMutation = useMutation({
    mutationFn: ({ id, data }: { id: string; data: Partial<GoalFormData> }) =>
      apiClient.put<Goal>(`/goals/${id}`, data),
    onSuccess: (data, variables) => {
      queryClient.invalidateQueries({ queryKey: ['goals'] })
      queryClient.setQueryData(['goals', variables.id], data)
      toast.success('Goal updated successfully!')
    },
    onError: (error: any) => {
      const message = error.response?.data?.detail || 'Failed to update goal'
      toast.error(message)
    },
  })

  // Delete goal mutation
  const deleteGoalMutation = useMutation({
    mutationFn: (goalId: string) => apiClient.delete(`/goals/${goalId}`),
    onSuccess: (_, goalId) => {
      queryClient.invalidateQueries({ queryKey: ['goals'] })
      queryClient.removeQueries({ queryKey: ['goals', goalId] })
      toast.success('Goal deleted successfully!')
    },
    onError: (error: any) => {
      const message = error.response?.data?.detail || 'Failed to delete goal'
      toast.error(message)
    },
  })

  // Start goal execution mutation
  const startGoalMutation = useMutation({
    mutationFn: (goalId: string) =>
      apiClient.post<{ run_id: string }>(`/goals/${goalId}/start`),
    onSuccess: (data) => {
      queryClient.invalidateQueries({ queryKey: ['goals'] })
      queryClient.invalidateQueries({ queryKey: ['runs'] })
      toast.success('Goal execution started!')
      return data.run_id
    },
    onError: (error: any) => {
      const message = error.response?.data?.detail || 'Failed to start goal'
      toast.error(message)
    },
  })

  return {
    useGoalsList,
    useGoal,
    createGoal: createGoalMutation.mutate,
    updateGoal: updateGoalMutation.mutate,
    deleteGoal: deleteGoalMutation.mutate,
    startGoal: startGoalMutation.mutate,
    isCreating: createGoalMutation.isPending,
    isUpdating: updateGoalMutation.isPending,
    isDeleting: deleteGoalMutation.isPending,
    isStarting: startGoalMutation.isPending,
  }
}
