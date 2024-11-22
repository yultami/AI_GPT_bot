from django.db import models

from core.domain.entities.chat import Chat as ChatE
from core.domain.entities.msg import Msg as MsgE
from core.domain.values.base import Id
from core.domain.values.msg import MsgRole, MsgContent


class Chat(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)

    def get_msgs(self):
        return self.msg.all()

    def to_entity(self):
        return ChatE(
            id=Id(self.id),
            msg=[msg.to_entity() for msg in self.get_msgs()]
        )

    class Meta:
        verbose_name = 'Чат пользователя'
        verbose_name_plural = 'Чаты поьзователей'


class Msg(models.Model):
    id = models.AutoField(primary_key=True)
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name='msg')
    content = models.TextField()
    roles = (
        ('user', 'user'),
        ('assistant', 'assistant'),
        ('system', 'system')
    )
    role = models.CharField(choices=roles, max_length=50)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.role

    def to_entity(self):
        return MsgE(
            id=Id(self.id),
            chat_id=Id(self.chat.id),
            role=MsgRole(self.role),
            content=MsgContent(self.content)
        )

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'