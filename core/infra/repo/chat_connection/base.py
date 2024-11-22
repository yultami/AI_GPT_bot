from abc import ABC, abstractmethod as abstract

from core.domain.entities.chat import Chat


class BsConnectRepo(ABC):
    @abstract
    async def get_connect_ai(self, api_key: str, chat: Chat) -> list[Chat]:
        ...

