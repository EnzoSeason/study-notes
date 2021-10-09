from typing import List
from collections import defaultdict


class Solution:
    """
    https://leetcode.com/problems/accounts-merge/

    1. create undirected graph for emails and hash map for users.

    2. use BFS or DFS to traversel the graph and merge the accounts.
    """

    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        adj_list = defaultdict(set)  #  adj list for emails
        users = dict()  #  hash map for email: name

        #  init adj_list and users
        for acc in accounts:
            name = acc[0]
            for email in acc[1:]:
                adj_list[acc[1]].add(email)
                adj_list[email].add(acc[1])
                users[email] = name

        #  use DFS
        visited = set()
        res = []
        for vertex in adj_list:
            if vertex not in visited:
                stack = [vertex]
                emails = []

                while stack:
                    node = stack.pop()
                    if node in visited:
                        continue
                    visited.add(node)
                    emails.append(node)

                    for neighbour in adj_list[node]:
                        stack.append(neighbour)

                res.append([users[vertex]] + sorted(emails))

        return res