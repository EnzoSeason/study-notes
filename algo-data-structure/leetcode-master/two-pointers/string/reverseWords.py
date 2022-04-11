from typing import List


class Solution:
    """
    https://leetcode.com/problems/reverse-words-in-a-string/
    """

    def reverse(self, arr: list, start: int, end: int) -> None:
        l, r = start, end - 1
        while l <= r:
            arr[l], arr[r] = arr[r], arr[l]
            l += 1
            r -= 1

    def removeExtraSpace(self, arr) -> List[str]:
        slow, fast = 0, 0
        ##  remove the spaces at the head.
        while fast < len(arr) and arr[fast] == " ":
            fast += 1

        while fast < len(arr):
            while 0 < fast < len(arr) and arr[fast - 1] == arr[fast] == " ":
                ## remove the space between the words
                fast += 1
            if fast < len(arr):
                arr[slow] = arr[fast]
                slow += 1
                fast += 1

        ## remove the extra spaces at the tail
        return arr[0 : slow - 1] if slow > 0 and arr[slow - 1] == " " else arr[0:slow]

    def reverseWords(self, s: str) -> str:
        arr = list(s)
        ## reverse the entire string
        self.reverse(arr, 0, len(arr))

        ##  remove extra space
        arr = self.removeExtraSpace(arr)

        ## reverse words
        i, j = 0, 0
        while j < len(arr):
            while j < len(arr) and arr[j] != " ":
                j += 1
            self.reverse(arr, i, j)
            i = j + 1
            j = i

        return "".join(arr)
