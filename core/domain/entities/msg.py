from dataclasses import dataclass as datacls

from core.domain.entities.base import BsEntity
from core.domain.values.base import Id
from core.domain.values.msg import MsgRole, MsgContent


@datacls(eq=False)
class Msg(BsEntity):
    chat_id: Id
    role: MsgRole
    content: MsgContent