from other.notification import notify
from schemas import Message

from fastapi import APIRouter, BackgroundTasks
from asyncio import sleep

notification_router = APIRouter()

async def schedule_task(title: str, message: str) -> None:
    await sleep(5)
    notify(title, message)

@notification_router.get("/")
async def get_notification(msg: Message, tasks: BackgroundTasks):
    tasks.add_task(schedule_task, msg.title, msg.message)
    return {
        "notification": "scheduled"
    }