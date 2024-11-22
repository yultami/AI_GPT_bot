from dataclasses import dataclass as datacls

from core.domain.entities.chat import Chat
from core.infra.repo.chat_connection.base import BsConnectRepo
from core.infra.repo.chat_repo.base import BsChatRepo
from core.logic.commands.base import BsCommand, BsCommandHandle


@datacls(frozen=True)
class GetConnectAICommand(BsCommand):
    api_key: str
    id: int


@datacls(frozen=True)
class GetConnectAICommandHandle(BsCommandHandle[GetConnectAICommand, list[Chat]]):
    connect_ai_repo: BsConnectRepo
    chat_repo: BsChatRepo

    async def handle(self, command: GetConnectAICommand):
        chat = await self.chat_repo.get_chat_by_id(command.id)
        return await self.connect_ai_repo.get_connect_ai(command.api_key, chat)
