import { useMutation, useQuery, useQueryClient } from '@tanstack/react-query'
import { useRouter } from 'next/navigation'
import { toast } from 'react-hot-toast'
import { apiClient } from '@/lib/api'
import { useAuthStore } from '@/lib/store'
import type { LoginRequest, RegisterRequest, User } from '@/types'

export function useAuth() {
  const router = useRouter()
  const queryClient = useQueryClient()
  const { user, isAuthenticated, login, logout, setLoading } = useAuthStore()

  // Get current user
  const { data: currentUser, isLoading: isLoadingUser } = useQuery({
    queryKey: ['auth', 'me'],
    queryFn: () => apiClient.get<User>('/auth/me'),
    enabled: isAuthenticated,
    retry: false,
  })

  // Login mutation
  const loginMutation = useMutation({
    mutationFn: (credentials: LoginRequest) =>
      apiClient.post('/auth/login', credentials),
    onSuccess: (data) => {
      login(data.user, data.access_token, data.refresh_token)
      toast.success('Welcome back!')
      router.push('/dashboard')
    },
    onError: (error: any) => {
      const message = error.response?.data?.detail || 'Login failed'
      toast.error(message)
    },
  })

  // Register mutation
  const registerMutation = useMutation({
    mutationFn: (userData: RegisterRequest) =>
      apiClient.post('/auth/register', userData),
    onSuccess: (data) => {
      login(data.user, data.access_token, data.refresh_token)
      toast.success('Account created successfully!')
      router.push('/dashboard')
    },
    onError: (error: any) => {
      const message = error.response?.data?.detail || 'Registration failed'
      toast.error(message)
    },
  })

  // Logout function
  const handleLogout = () => {
    logout()
    queryClient.clear()
    router.push('/auth/login')
    toast.success('Logged out successfully')
  }

  // Check if user has permission
  const hasPermission = (permission: string): boolean => {
    return user?.permissions?.includes(permission) || false
  }

  // Check if user has role
  const hasRole = (role: string): boolean => {
    return user?.role === role
  }

  // Check if user has any of the specified permissions
  const hasAnyPermission = (permissions: string[]): boolean => {
    return permissions.some((permission) => hasPermission(permission))
  }

  // Check if user has all of the specified permissions
  const hasAllPermissions = (permissions: string[]): boolean => {
    return permissions.every((permission) => hasPermission(permission))
  }

  return {
    user: currentUser || user,
    isAuthenticated,
    isLoading: isLoadingUser || loginMutation.isPending || registerMutation.isPending,
    login: loginMutation.mutate,
    register: registerMutation.mutate,
    logout: handleLogout,
    hasPermission,
    hasRole,
    hasAnyPermission,
    hasAllPermissions,
    isLoginLoading: loginMutation.isPending,
    isRegisterLoading: registerMutation.isPending,
  }
}
