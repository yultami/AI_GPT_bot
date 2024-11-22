from dataclasses import dataclass as datacls


@datacls(eq=False)
class DomainExcept(Exception):
    @property
    def msg(self) -> str:
        return 'An error occurred in domain entity'

    def __str__(self) -> str:
        return self.msg