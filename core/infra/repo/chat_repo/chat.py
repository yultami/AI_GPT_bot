import os
from typing import List

import django
from asgiref.sync import sync_to_async as sy_to_as

from core.domain.entities.chat import Chat
from core.domain.entities.msg import Msg
from core.domain.exception.chat import ChatIdDoesNotExist
from core.infra.repo.chat_repo.base import BsChatRepo

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.app.settings.developing')
django.setup()

from app.app_admin.models import Chat as ChatM, Msg as MsgM


class ORMChatRepo(BsChatRepo):
    @sy_to_as
    def get_chats(self) -> List[Chat]:
        chats_m = ChatM.objects.get()
        return [chat_m.to_enity() for chat_m in chats_m]

    @sy_to_as
    def get_chat_by_id(self, id: int) -> Chat:
        try:
            chat_m = ChatM.objects.get(id=id)
        except ChatM.DoesNotExist:
            raise ChatIdDoesNotExist(id=id)
        return chat_m.to_entity()

    @sy_to_as
    def add_chat(self, chat: Chat) -> None:
        chat_m = ChatM(
            id=chat.id.as_generic_type()
        )
        chat_m.save()

    @sy_to_as
    def add_msg(self, msg: Msg) -> None:
        try:
            ChatM.objects.get(id=msg.chat_id.as_generic_type())
        except ChatM.DoesNotExist:
            raise ChatIdDoesNotExist(id=id)
        msg_m = MsgM(
            id=msg.id.as_generic_type(),
            chat_id=msg.chat_id.as_generic_type(),
            role=msg.role.as_generic_type(),
            content=msg.content.as_generic_type()
        )
        msg_m.save()