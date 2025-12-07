from fastapi import FastAPI
from app.api.v1.router import router as api_router
from app.config import get_settings
from app.core.middleware import add_middlewares, log_requests_middleware
import uvicorn

settings = get_settings()

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.VERSION,
    docs_url="/docs" if settings.ENABLE_DOCS else None,
    openapi_url="/openapi.json" if settings.ENABLE_DOCS else None,
)

# Add all middlewares
add_middlewares(app)

# Custom middleware
app.middleware("http")(log_requests_middleware)

# Include API routers (mount v1 router at configured prefix)
app.include_router(api_router, prefix=settings.API_V1_PREFIX)


@app.get("/health")
def health_check():
    """Health check endpoint."""
    return {"status": "healthy", "version": settings.VERSION}


if __name__ == "__main__":
    
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=settings.ENVIRONMENT == "development",
    )