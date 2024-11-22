import asyncio

from aiogram import Dispatcher, Bot
from punq import Container

from core.app.handl.ai_h import ai_router
from core.app.handl.authorize_h import authorize_router
from core.app.handl.start_h import start_router
from core.logic.container import init_container


async def main():
    container: Container = init_container()
    bot: Bot = container.resolve(Bot)
    dp: Dispatcher = container.resolve(Dispatcher)
    dp.include_routers(start_router, authorize_router, ai_router)

    await asyncio.gather(dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types()))


if __name__ == "__main__":
    asyncio.run(main())
