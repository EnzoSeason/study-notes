class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.children = []


class Solution:
    def __init__(self) -> None:
        """
        "visited" is indispensable when a node can be visited twice.

        So, it's IMPORTANT for the graphic, optional for the tree.
        """
        self.visited = set()

    def dfs(self, node: Node) -> None:
        ## 1. process data according to the demand
        self.process(node)
        self.visited.add(node)

        ## 2. do DFS on the not-visited children
        for child in node.children:
            if child not in self.visited:
                self.dfs(child)

    def process(self, node: Node) -> None:
        pass
