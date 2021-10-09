from typing import List


class Solution:
    """
    https://leetcode.com/problems/restore-ip-addresses/
    """

    def __init__(self) -> None:
        self.s = ""
        self.res = []

    def isVaild(self, s: str) -> bool:
        if len(s) > 1 and s[0] == "0":
            return False

        if 0 <= int(s) <= 255:
            return True

        return False

    def backTrack(self, path: List[str], start: int) -> None:
        if start == len(self.s) and len(path) == 4:
            self.res.append(".".join(path))
            return

        for end in range(start + 1, len(self.s) + 1):
            # prune
            if len(self.s) - end > 3 * (4 - len(path) - 1):
                continue
            if self.isVaild(self.s[start:end]):
                self.backTrack(path + [self.s[start:end]], end)

    def restoreIpAddresses(self, s: str) -> List[str]:
        # prune
        if len(s) > 3 * 4:
            return []
        self.s = s
        self.backTrack([], 0)
        return self.res