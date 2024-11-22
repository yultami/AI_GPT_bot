from aiogram import Router
from aiogram.types import Message
from punq import Container

from core.logic.commands.chat import AddMsgCommand
from core.logic.commands.chat_connection import GetConnectAICommand
from core.logic.container import init_container
from core.logic.mediator import Mediator
from core.settings.config import Settings

ai_router = Router()


@ai_router.message()
async def ai_connection_h(msg: Message):
    container: Container = init_container()
    mediator: Mediator = container.resolve(Mediator)
    settings: Settings = container.resolve(Settings)
    await mediator.handle_command(AddMsgCommand(id=msg.message_id, chat_id=msg.from_user.id, role='user', content=msg.text))
    answer, *_ = await mediator.handle_command(GetConnectAICommand(api_key=settings.api_key, id=msg.from_user.id))
    await mediator.handle_command(AddMsgCommand(id=msg.message_id, chat_id=msg.from_user.id, role='assistant', content=answer))
    await msg.answer(answer)
