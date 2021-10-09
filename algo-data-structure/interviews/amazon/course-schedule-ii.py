from typing import List
from collections import deque


class SolutionDFS:
    NOT_VISITED = 0
    VISITED = 1
    REMOVED = 2

    def __init__(self) -> None:
        self.adj_list = {}
        self.memo = {}
        self.hasCycle = False
        self.res = []

    def dfs(self, node: int) -> None:
        if self.hasCycle:
            return

        self.memo[node] = SolutionDFS.VISITED

        if node in self.adj_list:
            for vertex in self.adj_list[node]:
                if self.memo[vertex] == SolutionDFS.NOT_VISITED:
                    self.dfs(vertex)
                elif self.memo[vertex] == SolutionDFS.VISITED:
                    self.hasCycle = True

        self.res.append(node)
        self.memo[node] = SolutionDFS.REMOVED

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        #   creat adg list, src: [dests]
        for dest, src in prerequisites:
            if src in self.adj_list:
                self.adj_list[src].append(dest)
            else:
                self.adj_list[src] = [dest]

        #  init memo
        self.memo = {i: SolutionDFS.NOT_VISITED for i in range(numCourses)}

        #  dfs
        for vertex in range(numCourses):
            if self.memo[vertex] == SolutionDFS.NOT_VISITED:
                self.dfs(vertex)

        return self.res[::-1] if not self.hasCycle else []


class SolutionBFS:
    """
    The vertex in the queue has 0 in-degree, implying no prerequisite courses required.
    """
    
    def __init__(self) -> None:
        self.adj_list = []
        self.in_degree = {}
        self.zero_degree_queue = []
        self.res = []

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        #   creat adg list and in_degree
        for dest, src in prerequisites:
            if src in self.adj_list:
                self.adj_list[src].append(dest)
            else:
                self.adj_list[src] = [dest]
            self.in_degree[dest] = self.in_degree.get(dest, 0) + 1

        #  init zero degree queue
        self.zero_degree_queue = deque(
            [i for i in range(numCourses) if i not in self.in_degree]
        )

        #  bfs
        while self.zero_degree_queue:
            node = self.zero_degree_queue.popleft()
            self.res.append(node)
            #  reduce in_degree
            if node in self.adj_list:
                for vertex in self.adj_list[node]:
                    self.in_degree[vertex] -= 1

                    if self.in_degree[vertex] == 0:
                        self.zero_degree_queue.append(vertex)

        return self.res if len(self.res) == numCourses else []
