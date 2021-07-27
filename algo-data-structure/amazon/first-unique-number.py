from typing import List
from collections import deque


class FirstUnique:
    def __init__(self, nums: List[int]):
        self.queue = deque(nums)
        self.is_unique = dict()
        for value in self.queue:
            if value in self.is_unique:
                self.is_unique[value] = False
            else:
                self.is_unique[value] = True

    def showFirstUnique(self) -> int:
        while self.queue and not self.is_unique[self.queue[0]]:
            self.queue.popleft()
        return self.queue[0] if self.queue else -1

    def add(self, value: int) -> None:
        if value in self.is_unique:
            self.is_unique[value] = False
        else:
            self.is_unique[value] = True
            self.queue.append(value)