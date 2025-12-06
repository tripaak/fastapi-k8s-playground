from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from app.config import get_settings
import time
import logging

logger = logging.getLogger(__name__)

def add_middlewares(app: FastAPI):
    settings = get_settings()
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.ALLOWED_ORIGINS,
        allow_credentials=True,
        allow_methods=settings.ALLOWED_METHODS,
        allow_headers=settings.ALLOWED_HEADERS,
    )


async def log_requests_middleware(request: Request, call_next):
    """Middleware to log HTTP requests and responses."""
    start_time = time.time()
    
    response = await call_next(request)
    
    process_time = time.time() - start_time
    logger.info(
        f"method={request.method} path={request.url.path} status={response.status_code} duration={process_time:.3f}s"
    )
    
    return response