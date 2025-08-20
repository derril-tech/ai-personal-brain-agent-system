"""
MindMesh Middleware Classes
"""

import time
import uuid
from typing import Callable
from fastapi import Request, Response
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.types import ASGIApp

from app.core.logging import get_logger, RequestContextLogger

logger = get_logger(__name__)


class RequestLoggingMiddleware(BaseHTTPMiddleware):
    """Middleware for logging all requests"""
    
    def __init__(self, app: ASGIApp):
        super().__init__(app)
    
    async def dispatch(self, request: Request, call_next: Callable) -> Response:
        # Generate request ID
        request_id = str(uuid.uuid4())
        
        # Create request context logger
        request_logger = RequestContextLogger(logger).bind(
            request_id=request_id,
            method=request.method,
            url=str(request.url),
            client_ip=request.client.host if request.client else None,
            user_agent=request.headers.get("user-agent"),
        )
        
        # Log request start
        request_logger.info("Request started")
        
        # Track timing
        start_time = time.time()
        
        try:
            # Process request
            response = await call_next(request)
            
            # Calculate duration
            duration = time.time() - start_time
            
            # Log request completion
            request_logger.bind(
                status_code=response.status_code,
                duration=duration,
            ).info("Request completed")
            
            # Add request ID to response headers
            response.headers["X-Request-ID"] = request_id
            
            return response
            
        except Exception as e:
            # Calculate duration
            duration = time.time() - start_time
            
            # Log request error
            request_logger.bind(
                error=str(e),
                duration=duration,
            ).error("Request failed")
            
            raise


class ResponseTimeMiddleware(BaseHTTPMiddleware):
    """Middleware for tracking response times"""
    
    def __init__(self, app: ASGIApp):
        super().__init__(app)
    
    async def dispatch(self, request: Request, call_next: Callable) -> Response:
        start_time = time.time()
        
        response = await call_next(request)
        
        duration = time.time() - start_time
        
        # Add response time header
        response.headers["X-Response-Time"] = f"{duration:.3f}s"
        
        # Log slow requests
        if duration > 1.0:  # Log requests taking more than 1 second
            logger.warning(
                "Slow request detected",
                method=request.method,
                url=str(request.url),
                duration=duration,
            )
        
        return response


class SecurityHeadersMiddleware(BaseHTTPMiddleware):
    """Middleware for adding security headers"""
    
    def __init__(self, app: ASGIApp):
        super().__init__(app)
    
    async def dispatch(self, request: Request, call_next: Callable) -> Response:
        response = await call_next(request)
        
        # Add security headers
        response.headers["X-Content-Type-Options"] = "nosniff"
        response.headers["X-Frame-Options"] = "DENY"
        response.headers["X-XSS-Protection"] = "1; mode=block"
        response.headers["Referrer-Policy"] = "strict-origin-when-cross-origin"
        response.headers["Content-Security-Policy"] = (
            "default-src 'self'; "
            "script-src 'self' 'unsafe-inline' 'unsafe-eval'; "
            "style-src 'self' 'unsafe-inline'; "
            "img-src 'self' data: https:; "
            "font-src 'self' data:; "
            "connect-src 'self' ws: wss:;"
        )
        
        return response


class TenantMiddleware(BaseHTTPMiddleware):
    """Middleware for tenant identification and scoping"""
    
    def __init__(self, app: ASGIApp):
        super().__init__(app)
    
    async def dispatch(self, request: Request, call_next: Callable) -> Response:
        # Extract tenant from subdomain or header
        tenant_id = self._extract_tenant_id(request)
        
        if tenant_id:
            # Add tenant context to request state
            request.state.tenant_id = tenant_id
        
        response = await call_next(request)
        return response
    
    def _extract_tenant_id(self, request: Request) -> str:
        """Extract tenant ID from request"""
        # Check for tenant header
        tenant_header = request.headers.get("X-Tenant-ID")
        if tenant_header:
            return tenant_header
        
        # Check subdomain
        host = request.headers.get("host", "")
        if "." in host:
            subdomain = host.split(".")[0]
            if subdomain != "www" and subdomain != "api":
                return subdomain
        
        return None


class RateLimitMiddleware(BaseHTTPMiddleware):
    """Middleware for rate limiting"""
    
    def __init__(self, app: ASGIApp):
        super().__init__(app)
        # In production, use Redis for rate limiting
        self.rate_limits = {}
    
    async def dispatch(self, request: Request, call_next: Callable) -> Response:
        # Get client identifier
        client_id = self._get_client_id(request)
        
        # Check rate limit
        if not self._check_rate_limit(client_id):
            return Response(
                content="Rate limit exceeded",
                status_code=429,
                headers={"Retry-After": "60"},
            )
        
        response = await call_next(request)
        return response
    
    def _get_client_id(self, request: Request) -> str:
        """Get client identifier for rate limiting"""
        # Use IP address as client identifier
        return request.client.host if request.client else "unknown"
    
    def _check_rate_limit(self, client_id: str) -> bool:
        """Check if client is within rate limits"""
        # Simple in-memory rate limiting (use Redis in production)
        current_time = time.time()
        
        if client_id not in self.rate_limits:
            self.rate_limits[client_id] = []
        
        # Remove old requests (older than 1 minute)
        self.rate_limits[client_id] = [
            req_time for req_time in self.rate_limits[client_id]
            if current_time - req_time < 60
        ]
        
        # Check if within limit (100 requests per minute)
        if len(self.rate_limits[client_id]) >= 100:
            return False
        
        # Add current request
        self.rate_limits[client_id].append(current_time)
        return True
