from fastapi import APIRouter


router = APIRouter()
router.include_router(api_router, prefix="/v1")