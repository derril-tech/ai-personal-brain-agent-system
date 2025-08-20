"""
MindMesh Logging Configuration
"""

import logging
import sys
from typing import Any, Dict
from structlog import configure, get_logger
from structlog.stdlib import LoggerFactory
from structlog.processors import (
    TimeStamper,
    JSONRenderer,
    add_log_level,
    format_exc_info,
    StackInfoRenderer,
    UnicodeDecoder,
)
from structlog.types import Processor

from app.core.config import settings


def setup_logging():
    """Setup structured logging for the application"""
    
    # Configure standard library logging
    logging.basicConfig(
        format="%(message)s",
        stream=sys.stdout,
        level=getattr(logging, settings.LOG_LEVEL.upper()),
    )
    
    # Custom processor to add request context
    def add_request_context(logger, method_name, event_dict):
        """Add request context to log entries"""
        # This will be populated by middleware
        if hasattr(logger, 'request_context'):
            event_dict.update(logger.request_context)
        return event_dict
    
    # Custom processor to add user context
    def add_user_context(logger, method_name, event_dict):
        """Add user context to log entries"""
        if hasattr(logger, 'user_context'):
            event_dict.update(logger.user_context)
        return event_dict
    
    # Configure structlog
    configure(
        processors=[
            # Add timestamp
            TimeStamper(fmt="iso"),
            
            # Add log level
            add_log_level,
            
            # Add stack info
            StackInfoRenderer(),
            
            # Add exception info
            format_exc_info,
            
            # Add request context
            add_request_context,
            
            # Add user context
            add_user_context,
            
            # Decode unicode
            UnicodeDecoder(),
            
            # Render as JSON
            JSONRenderer(),
        ],
        context_class=dict,
        logger_factory=LoggerFactory(),
        wrapper_class=logging.Logger,
        cache_logger_on_first_use=True,
    )


def get_logger(name: str = None) -> Any:
    """Get a structured logger instance"""
    return get_logger(name or "mindmesh")


class RequestContextLogger:
    """Logger with request context"""
    
    def __init__(self, logger, request_context: Dict[str, Any] = None):
        self.logger = logger
        self.request_context = request_context or {}
    
    def bind(self, **kwargs):
        """Bind additional context"""
        self.request_context.update(kwargs)
        return self
    
    def _log(self, level: str, message: str, **kwargs):
        """Log with request context"""
        self.logger.request_context = self.request_context
        getattr(self.logger, level)(message, **kwargs)
    
    def debug(self, message: str, **kwargs):
        self._log("debug", message, **kwargs)
    
    def info(self, message: str, **kwargs):
        self._log("info", message, **kwargs)
    
    def warning(self, message: str, **kwargs):
        self._log("warning", message, **kwargs)
    
    def error(self, message: str, **kwargs):
        self._log("error", message, **kwargs)
    
    def critical(self, message: str, **kwargs):
        self._log("critical", message, **kwargs)


class UserContextLogger:
    """Logger with user context"""
    
    def __init__(self, logger, user_context: Dict[str, Any] = None):
        self.logger = logger
        self.user_context = user_context or {}
    
    def bind(self, **kwargs):
        """Bind additional context"""
        self.user_context.update(kwargs)
        return self
    
    def _log(self, level: str, message: str, **kwargs):
        """Log with user context"""
        self.logger.user_context = self.user_context
        getattr(self.logger, level)(message, **kwargs)
    
    def debug(self, message: str, **kwargs):
        self._log("debug", message, **kwargs)
    
    def info(self, message: str, **kwargs):
        self._log("info", message, **kwargs)
    
    def warning(self, message: str, **kwargs):
        self._log("warning", message, **kwargs)
    
    def error(self, message: str, **kwargs):
        self._log("error", message, **kwargs)
    
    def critical(self, message: str, **kwargs):
        self._log("critical", message, **kwargs)


# Global logger instance
logger = get_logger()
