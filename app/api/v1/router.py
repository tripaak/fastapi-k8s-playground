"""
API v1 router - aggregates all v1 endpoints.

Objective: Create a router that includes all v1 API endpoints.
Why: Keeps the API versioned and organized. Makes it easy to add/remove endpoints per version.
Gotcha: Import the router from endpoints, don't create duplicate routers.
"""

from fastapi import APIRouter
from app.api.v1.endpoints import router as items_router

# Keep this router unprefixed so the application's `settings.API_V1_PREFIX`
# can control the full path (e.g. "/api/v1"). Mounting with a prefix in
# `app.main` prevents duplicated or mismatched prefixes.
router = APIRouter()
router.include_router(items_router)