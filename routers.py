from fastapi import APIRouter
from view.notification.notificationRouter import notification_router


main_api_router = APIRouter(prefix='/v1')

main_api_router.include_router(notification_router, prefix="/notification")
