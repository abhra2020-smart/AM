from dataclasses import dataclass


@dataclass
class NumberNode:
    value: any

    def __repr__(self):
        return f"{self.value}"

    def __add__(self, other):
        return self.value + other.value


@dataclass
class AddNode:
    node_a: any
    node_b: any

    def __repr__(self):
        return f"({self.node_a}+{self.node_b})"


@dataclass
class PowerNode:
    node_a: any
    node_b: any

    def __repr__(self):
        return f"({self.node_a}^{self.node_b})"


@dataclass
class ModNode:
    node_a: any
    node_b: any

    def __repr__(self):
        return f"({self.node_a}%{self.node_b})"


@dataclass
class SubtractNode:
    node_a: any
    node_b: any

    def __repr__(self):
        return f"({self.node_a}-{self.node_b})"


@dataclass
class MultiplyNode:
    node_a: any
    node_b: any

    def __repr__(self):
        return f"({self.node_a}*{self.node_b})"


@dataclass
class DivideNode:
    node_a: any
    node_b: any

    def __repr__(self):
        return f"({self.node_a}/{self.node_b})"


@dataclass
class IntDivNode:
    node_a: any
    node_b: any

    def __repr__(self):
        return f"({self.node_a}//{self.node_b})"


@dataclass
class PlusNode:
    node: any

    def __repr__(self):
        return f"(+{self.node})"


@dataclass
class MinusNode:
    node: any

    def __repr__(self):
        return f"(-{self.node})"
