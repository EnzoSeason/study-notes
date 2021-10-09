from typing import Deque, Dict, List, Tuple
from collections import defaultdict, deque


class SolutionBFS:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        n = len(beginWord)
        combo = defaultdict(list)  # adj list
        for word in wordList:
            for i in range(n):
                combo[word[:i] + "*" + word[i + 1 :]].append(word)

        queue = deque([(beginWord, 1)])
        visited = {beginWord: True}

        while queue:
            current_word, level = queue.popleft()
            for i in range(n):
                for word in combo[current_word[:i] + "*" + current_word[i + 1 :]]:
                    if word == endWord:
                        return level + 1
                    if word not in visited:
                        visited[word] = True
                        queue.append((word, level + 1))
        return 0


class Solution:
    """
    use 2 queue, run 2 BFS at the same time.
    """
    
    def __init__(self) -> None:
        self.endWord = ""
        self.res = []
        self.n = 0
        self.combo = defaultdict(list)

    def visiteNodes(
        self,
        queue: Deque[Tuple[str, int]],
        visited: Dict[str, int],
        other_visited: Dict[str, int],
    ) -> int:
        current_word, level = queue.popleft()
        for i in range(self.n):
            for word in self.combo[current_word[:i] + "*" + current_word[i + 1 :]]:
                if word in other_visited:
                    return other_visited[word] + level
                if word not in visited:
                    visited[word] = level + 1
                    queue.append((word, level + 1))
        return 0

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        self.n = len(beginWord)
        for word in wordList:
            for i in range(self.n):
                self.combo[word[:i] + "*" + word[i + 1 :]].append(word)

        queues = [deque([(beginWord, 1)]), deque([(endWord, 1)])]
        visiteds = [{beginWord: 1}, {endWord: 1}]

        while queues[0] and queues[1]:
            for i in range(2):
                ans = self.visiteNodes(queues[i], visiteds[i], visiteds[(i + 1) % 2])
                if ans:
                    return ans

        return 0