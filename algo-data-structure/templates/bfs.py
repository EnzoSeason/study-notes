from collections import deque


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

    def bfs(self, entryNode: Node) -> None:
        #  1. init a queue
        queue = deque([entryNode])

        while queue:
            #   2. pop the queue and visit the node
            node = queue.popleft()

            #  3. process data according to the demand
            if node not in self.visited:
                self.process(node)
                self.visited.add(node)

            #  4. push the node's children into the queue
            queue += node.children

    def process(self, node: Node) -> None:
        pass
