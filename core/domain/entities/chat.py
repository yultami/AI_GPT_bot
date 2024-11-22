from dataclasses import dataclass as datacls

from core.domain.entities.base import BsEntity
from core.domain.entities.msg import Msg


@datacls(eq=False)
class Chat(BsEntity):
    msg: list[Msg]

    def convert_to_msg_list(self):
        return [{'role': msg.role.as_generic_type(),
                 'content': msg.content.as_generic_type()} for msg in self.msg]