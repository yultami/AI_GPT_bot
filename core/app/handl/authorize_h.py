from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from punq import Container

from core.logic.commands.chat import AddChatCommand, GetChatByIdCommand
from core.logic.container import init_container
from core.logic.mediator import Mediator

authorize_router = Router()


@authorize_router.callback_query(F.data == "create_chat")
async def authorize_chat(callback: CallbackQuery):
    container: Container = init_container()
    mediator: Mediator = container.resolve(Mediator)
    try:
        await mediator.handle_command(GetChatByIdCommand(id=callback.from_user.id))
    except:
        await mediator.handle_command(AddChatCommand(id=callback.from_user.id, msg=[]))

    await callback.message.edit_text("Вы прошли авторицазию, можете приступить к использованию AI")