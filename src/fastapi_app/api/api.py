from fastapi import APIRouter

from fastapi_app.api.v1.v1 import router as v1_router

router = APIRouter()
router.include_router(v1_router, prefix="/v1")