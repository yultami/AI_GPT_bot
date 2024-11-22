from mistralai import Mistral

from core.domain.entities.chat import Chat
from core.infra.repo.chat_connection.base import BsConnectRepo
from core.settings.config import Settings


class ChatConnectRepo(BsConnectRepo):
    async def get_connect_ai(self, api_key: str, chat: Chat):
        client = Mistral(api_key=api_key)
        response = client.chat.complete(
            model="pixtral-12b-2409",
            messages=chat.convert_to_msg_list()
        )

        return response.choices[0].message.content