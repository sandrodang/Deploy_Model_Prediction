from fastapi import APIRouter
from routes.catdogs_routes import router as catdogs_router

router = APIRouter()
router.include_router(catdogs_router, prefix="/catdogs_classification")
