from dataclasses import dataclass as datacls

from core.domain.exception.base import DomainExcept


@datacls(eq=False)
class ChatIdDoesNotExist(DomainExcept):
    id: int

    @property
    def msg(self) -> str:
        return f'Chat with id "{self.id}" does not exist'
