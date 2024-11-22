from abc import ABC, abstractmethod as abstract
from typing import List

from core.domain.entities.chat import Chat
from core.domain.entities.msg import Msg


class BsChatRepo(ABC):
    @abstract
    async def get_chats(self) -> List[Chat]:
        ...

    @abstract
    async def get_chat_by_id(self, id: int) -> Chat:
        ...

    @abstract
    async def add_chat(self, chat: Chat) -> None:
        ...

    @abstract
    async def add_msg(self, msg: Msg) -> None:
        ...