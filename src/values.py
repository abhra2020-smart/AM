from dataclasses import dataclass


@dataclass
class Number:
    value: any

    def __repr__(self):
        return f"{self.value}"


@dataclass
class Bool:
    value: bool

    def __repr__(self):
        return f"{self.value}".lower()
