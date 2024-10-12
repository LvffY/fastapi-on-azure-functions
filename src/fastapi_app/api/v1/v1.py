from fastapi import APIRouter

from fastapi_app.api.v1.endpoints.users import router as users_router

router = APIRouter()
router.include_router(users_router, prefix="/users")