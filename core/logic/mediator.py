from collections import defaultdict
from dataclasses import dataclass as datacls, field
from typing import Type, Iterable

from core.logic.commands.base import CT, BsCommandHandle, CR, BsCommand


@datacls(eq=False)
class Mediator:
    command_map: dict[Type[CT], list[BsCommandHandle[CT, CR]]] = field(
        default_factory=lambda: defaultdict(list),
        kw_only=True
    )

    def reg_command(self, command: Type[CT], command_handlers: Iterable[BsCommandHandle[CT, CR]]) -> None:
        self.command_map[command].extend(command_handlers)

    async def handle_command(self, command: BsCommand) -> Iterable[CR]:
        command_type = command.__class__
        handlers = self.command_map.get(command_type)
        return [await handler.handle(command) for handler in handlers]