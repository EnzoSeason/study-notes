from abc import ABC, abstractmethod
from typing import List, Optional

"""
This is the interface for the expression tree Node.
You should not remove it, and you can define some classes to implement it.
"""


class Node(ABC):
    @abstractmethod
    ## define your fields here
    def evaluate(self) -> int:
        pass


class TreeNode(Node):
    def __init__(self, num=0, ops: Optional[str] = None) -> None:
        self.num = num
        self.ops = ops
        self.left, self.right = None, None

    def evaluate(self) -> int:
        if not (self.left and self.right):
            return self.num

        if self.ops == "+":
            return self.left.evaluate() + self.right.evaluate()
        if self.ops == "-":
            return self.left.evaluate() - self.right.evaluate()
        if self.ops == "*":
            return self.left.evaluate() * self.right.evaluate()
        if self.ops == "/":
            return self.left.evaluate() // self.right.evaluate()

        return 0


"""    
This is the TreeBuilder class.
You can treat it as the driver code that takes the postinfix input
and returns the expression tree represnting it as a Node.
"""


class TreeBuilder(object):
    def buildTree(self, postfix: List[str]) -> "Node":
        stack = []
        ops = ["+", "-", "*", "/"]

        for ele in postfix:
            if ele not in ops:
                node = TreeNode(num=int(ele))
                stack.append(node)
            else:
                node = TreeNode(ops=ele)
                right = stack.pop()
                left = stack.pop()

                node.left, node.right = left, right
                stack.append(node)

        return stack.pop()


"""
Your TreeBuilder object will be instantiated and called as such:
obj = TreeBuilder();
expTree = obj.buildTree(postfix);
ans = expTree.evaluate();
"""
