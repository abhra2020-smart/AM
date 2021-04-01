from AM.src.values import *


class Interpreter:
    def __init__(self):
        pass

    def visit(self, node):
        method_name = f'visit_{type(node).__name__}'
        method = getattr(self, method_name)
        return method(node)

    @classmethod
    def visit_NumberNode(cls, node):
        return Number(node.value)

    def visit_AddNode(self, node):
        return Number(self.visit(node.node_a).value + self.visit(node.node_b).value)

    def visit_RSNode(self, node):
        return Number(self.visit(node.node_a).value >> self.visit(node.node_b).value)

    def visit_LSNode(self, node):
        return Number(self.visit(node.node_a).value << self.visit(node.node_b).value)

    def visit_GreaterNode(self, node):
        return Bool(self.visit(node.node_a).value > self.visit(node.node_b).value)

    def visit_SmallerNode(self, node):
        return Bool(self.visit(node.node_a).value < self.visit(node.node_b).value)

    def visit_SubtractNode(self, node):
        return Number(self.visit(node.node_a).value - self.visit(node.node_b).value)

    def visit_MultiplyNode(self, node):
        return Number(self.visit(node.node_a).value * self.visit(node.node_b).value)

    def visit_PowerNode(self, node):
        return Number(self.visit(node.node_a).value ** self.visit(node.node_b).value)

    def visit_ModNode(self, node):
        return Number(self.visit(node.node_a).value % self.visit(node.node_b).value)

    def visit_EqualsNode(self, node):
        return Bool(self.visit(node.node_a).value == self.visit(node.node_b).value)

    def visit_DivideNode(self, node):
        try:
            return Number(self.visit(node.node_a).value / self.visit(node.node_b).value)
        except Exception as e:
            raise Exception("Runtime math error: " + str(e))

    def visit_IntDivNode(self, node):
        try:
            return Number(self.visit(node.node_a).value // self.visit(node.node_b).value)
        except:
            raise Exception("Runtime math error")
