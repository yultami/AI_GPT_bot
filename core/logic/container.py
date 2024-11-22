from functools import lru_cache

from aiogram import Bot, Dispatcher
from punq import Container, Scope

from core.infra.repo.chat_connection.base import BsConnectRepo
from core.infra.repo.chat_connection.chat_connection import ChatConnectRepo
from core.infra.repo.chat_repo.base import BsChatRepo
from core.infra.repo.chat_repo.chat import ORMChatRepo
from core.logic.commands.chat import GetChatsCommandHandle, AddChatCommandHandle, AddMsgCommandHandle, GetChatsCommand, \
    AddChatCommand, AddMsgCommand, GetChatByIdCommandHandle, GetChatByIdCommand
from core.logic.commands.chat_connection import GetConnectAICommandHandle, GetConnectAICommand
from core.logic.mediator import Mediator
from core.settings.config import Settings


@lru_cache(1)
def init_container():
    return _init_container()


def _init_container() -> Container:
    container = Container()

    container.register(GetChatsCommandHandle)
    container.register(GetChatByIdCommandHandle)
    container.register(AddChatCommandHandle)
    container.register(AddMsgCommandHandle)

    container.register(GetConnectAICommandHandle)

    container.register(Settings, scope=Scope.singleton)

    def init_bot() -> Bot:
        settings = container.resolve(Settings)
        bot = Bot(token=settings.token_bot)
        return bot

    def init_dispatcher() -> Dispatcher:
        dp = Dispatcher()
        return dp

    def init_chat_repo() -> BsChatRepo:
        return ORMChatRepo()

    def init_chat_connection() -> BsConnectRepo:
        return ChatConnectRepo()

    def init_mediator() -> Mediator:
        mediator = Mediator()

        mediator.reg_command(GetChatsCommand, [container.resolve(GetChatsCommandHandle)])
        mediator.reg_command(GetChatByIdCommand, [container.resolve(GetChatByIdCommandHandle)])
        mediator.reg_command(AddChatCommand, [container.resolve(AddChatCommandHandle)])
        mediator.reg_command(AddMsgCommand, [container.resolve(AddMsgCommandHandle)])

        mediator.reg_command(GetConnectAICommand, [container.resolve(GetConnectAICommandHandle)])

        return mediator

    container.register(Bot, factory=init_bot, scope=Scope.singleton)
    container.register(Dispatcher, factory=init_dispatcher, scope=Scope.singleton)

    container.register(BsChatRepo, factory=init_chat_repo, scope=Scope.singleton)
    container.register(BsConnectRepo, factory=init_chat_connection, scope=Scope.singleton)

    container.register(Mediator, factory=init_mediator, scope=Scope.singleton)

    return container
