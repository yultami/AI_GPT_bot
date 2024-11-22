from dataclasses import dataclass as datacls

from core.domain.entities.chat import Chat
from core.domain.entities.msg import Msg
from core.domain.values.base import Id
from core.domain.values.msg import MsgRole, MsgContent
from core.infra.repo.chat_repo.base import BsChatRepo
from core.logic.commands.base import BsCommand, BsCommandHandle


@datacls(frozen=True)
class GetChatsCommand(BsCommand):
    ...


@datacls(frozen=True)
class GetChatByIdCommand(BsCommand):
    id: int


@datacls(frozen=True)
class AddChatCommand(BsCommand):
    id: int
    msg: list


@datacls(frozen=True)
class AddMsgCommand(BsCommand):
    id: int
    chat_id: int
    role: str
    content: str


@datacls(frozen=True)
class GetChatsCommandHandle(BsCommandHandle[GetChatsCommand, list[Chat]]):
    chat_repo: BsChatRepo

    async def handle(self, command: GetChatsCommand) -> list[Chat]:
        return await self.chat_repo.get_chats()


@datacls(frozen=True)
class GetChatByIdCommandHandle(BsCommandHandle[GetChatsCommand, Chat]):
    chat_repo: BsChatRepo

    async def handle(self, command: GetChatByIdCommand) -> Chat:
        return await self.chat_repo.get_chat_by_id(command.id)


@datacls(frozen=True)
class AddChatCommandHandle(BsCommandHandle[AddChatCommand, None]):
    chat_repo: BsChatRepo

    async def handle(self, command: AddChatCommand) -> None:
        chat = Chat(
            id=Id(command.id),
            msg=command.msg
        )
        return await self.chat_repo.add_chat(chat)


@datacls(frozen=True)
class AddMsgCommandHandle(BsCommandHandle[AddChatCommand, Msg]):
    chat_repo: BsChatRepo

    async def handle(self, command: AddMsgCommand) -> None:
        chat = await self.chat_repo.get_chat_by_id(command.chat_id)
        msg = Msg(
            id=Id(command.id),
            chat_id=chat.id,
            role=MsgRole(command.role),
            content=MsgContent(command.content)
        )
        return await self.chat_repo.add_msg(msg)
