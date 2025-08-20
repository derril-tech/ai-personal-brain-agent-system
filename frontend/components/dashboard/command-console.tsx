'use client'

import { useState, useRef, useEffect } from 'react'
import { Button } from '@/components/ui/button'
import { Input } from '@/components/ui/input'
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card'
import { Badge } from '@/components/ui/badge'
import { useGoals } from '@/hooks/useGoals'
import { useAuth } from '@/hooks/useAuth'
import { cn } from '@/lib/utils'
import { Brain, Send, Sparkles, Target, Clock, CheckCircle, AlertCircle } from 'lucide-react'

interface Message {
  id: string
  type: 'user' | 'assistant' | 'system'
  content: string
  timestamp: Date
  goalId?: string
  runId?: string
  status?: 'pending' | 'running' | 'completed' | 'failed'
}

export function CommandConsole() {
  const [messages, setMessages] = useState<Message[]>([])
  const [input, setInput] = useState('')
  const [isProcessing, setIsProcessing] = useState(false)
  const messagesEndRef = useRef<HTMLDivElement>(null)
  const { user } = useAuth()
  const { startGoal } = useGoals()

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' })
  }

  useEffect(() => {
    scrollToBottom()
  }, [messages])

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault()
    if (!input.trim() || isProcessing) return

    const userMessage: Message = {
      id: Date.now().toString(),
      type: 'user',
      content: input,
      timestamp: new Date(),
    }

    setMessages(prev => [...prev, userMessage])
    setInput('')
    setIsProcessing(true)

    try {
      // Simulate goal creation and execution
      const systemMessage: Message = {
        id: (Date.now() + 1).toString(),
        type: 'system',
        content: 'Processing your request...',
        timestamp: new Date(),
        status: 'running',
      }

      setMessages(prev => [...prev, systemMessage])

      // TODO: Replace with actual API call
      await new Promise(resolve => setTimeout(resolve, 2000))

      const assistantMessage: Message = {
        id: (Date.now() + 2).toString(),
        type: 'assistant',
        content: `I've created a goal for: "${input}". The system is now planning and executing the necessary steps.`,
        timestamp: new Date(),
        status: 'completed',
      }

      setMessages(prev => [...prev.slice(0, -1), assistantMessage])
    } catch (error) {
      const errorMessage: Message = {
        id: (Date.now() + 2).toString(),
        type: 'assistant',
        content: 'Sorry, I encountered an error while processing your request. Please try again.',
        timestamp: new Date(),
        status: 'failed',
      }

      setMessages(prev => [...prev.slice(0, -1), errorMessage])
    } finally {
      setIsProcessing(false)
    }
  }

  const getStatusIcon = (status?: string) => {
    switch (status) {
      case 'running':
        return <Clock className="w-4 h-4 text-blue-500 animate-spin" />
      case 'completed':
        return <CheckCircle className="w-4 h-4 text-green-500" />
      case 'failed':
        return <AlertCircle className="w-4 h-4 text-red-500" />
      default:
        return null
    }
  }

  const getMessageStyle = (type: string) => {
    switch (type) {
      case 'user':
        return 'bg-primary text-primary-foreground ml-auto max-w-[80%]'
      case 'assistant':
        return 'bg-muted max-w-[80%]'
      case 'system':
        return 'bg-blue-50 border border-blue-200 max-w-[80%]'
      default:
        return 'bg-muted max-w-[80%]'
    }
  }

  return (
    <Card className="h-full flex flex-col">
      <CardHeader className="border-b">
        <div className="flex items-center justify-between">
          <div className="flex items-center space-x-2">
            <Brain className="w-5 h-5 text-brain-500" />
            <CardTitle className="text-lg">Command Console</CardTitle>
          </div>
          <Badge variant="neural" className="flex items-center space-x-1">
            <Sparkles className="w-3 h-3" />
            <span>AI Ready</span>
          </Badge>
        </div>
        <p className="text-sm text-muted-foreground">
          Describe what you want to accomplish and I'll help you get it done.
        </p>
      </CardHeader>

      <CardContent className="flex-1 flex flex-col p-0">
        {/* Messages Area */}
        <div className="flex-1 overflow-y-auto p-4 space-y-4">
          {messages.length === 0 && (
            <div className="text-center text-muted-foreground py-8">
              <Target className="w-12 h-12 mx-auto mb-4 opacity-50" />
              <p className="text-lg font-medium mb-2">What would you like to accomplish?</p>
              <p className="text-sm">
                Try saying something like "Plan my product launch" or "Summarize my recent emails"
              </p>
            </div>
          )}

          {messages.map((message) => (
            <div
              key={message.id}
              className={cn(
                'flex items-start space-x-3',
                message.type === 'user' ? 'justify-end' : 'justify-start'
              )}
            >
              {message.type !== 'user' && (
                <div className="w-8 h-8 rounded-full bg-gradient-to-r from-brain-500 to-mesh-500 flex items-center justify-center flex-shrink-0">
                  <Brain className="w-4 h-4 text-white" />
                </div>
              )}
              
              <div
                className={cn(
                  'rounded-lg px-4 py-2 text-sm',
                  getMessageStyle(message.type)
                )}
              >
                <div className="flex items-center space-x-2 mb-1">
                  {getStatusIcon(message.status)}
                  <span className="text-xs text-muted-foreground">
                    {message.timestamp.toLocaleTimeString()}
                  </span>
                </div>
                <p>{message.content}</p>
              </div>

              {message.type === 'user' && (
                <div className="w-8 h-8 rounded-full bg-primary flex items-center justify-center flex-shrink-0">
                  <span className="text-xs font-medium text-primary-foreground">
                    {user?.full_name?.charAt(0) || user?.username?.charAt(0) || 'U'}
                  </span>
                </div>
              )}
            </div>
          ))}
          
          <div ref={messagesEndRef} />
        </div>

        {/* Input Area */}
        <div className="border-t p-4">
          <form onSubmit={handleSubmit} className="flex space-x-2">
            <Input
              value={input}
              onChange={(e) => setInput(e.target.value)}
              placeholder="Describe your goal or task..."
              disabled={isProcessing}
              className="flex-1"
            />
            <Button
              type="submit"
              disabled={!input.trim() || isProcessing}
              className="px-4"
            >
              {isProcessing ? (
                <div className="w-4 h-4 border-2 border-white border-t-transparent rounded-full animate-spin" />
              ) : (
                <Send className="w-4 h-4" />
              )}
            </Button>
          </form>
        </div>
      </CardContent>
    </Card>
  )
}
