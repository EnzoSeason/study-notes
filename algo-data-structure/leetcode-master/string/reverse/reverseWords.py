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

    def reverseWords_ON(self, s: str) -> str:
        """
        1. store words in a list
        2. reverse words

        Time complexity: O(N)
        Space complexity: O(N)
        """
        arr = list(s)
        i = 0
        words = []

        while i < len(arr):
            if arr[i] != " ":
                j = i
                while j < len(arr) and arr[j] != " ":
                    j += 1
                words.append("".join(arr[i:j]))
                i = j
            else:
                i += 1

        self.reverse(words, 0, len(words))
        return " ".join(words)

    def removeExtraSpace(self, arr) -> List[str]:
        slow, fast = 0, 0
        #  remove the spaces at the head.
        while fast < len(arr) and arr[fast] == " ":
            fast += 1

        while fast < len(arr):
            if fast > 0 and arr[fast - 1] == arr[fast] == " ":
                # remove the space between the words
                fast += 1
                continue
            arr[slow] = arr[fast]
            slow += 1
            fast += 1
        # remove the extra spaces at the tail
        return arr[0 : slow - 1] if slow > 0 and arr[slow - 1] == " " else arr[0:slow]

    def reverseWords_O1(self, s: str) -> str:
        """
        1. reverse the entire string
        2. remove the extra space.
        3. reverse each word

        Time complexity: O(N)
        Space complexity: O(1)
        """

        arr = list(s)
        # reverse string
        self.reverse(arr, 0, len(arr))

        # remove the extra space
        arr = self.removeExtraSpace(arr)

        # reverse words
        i = 0
        while i < len(arr):
            # reverse the word, arr[i:j]
            j = i
            while j < len(arr) and arr[j] != " ":
                j += 1
            self.reverse(arr, i, j)
            i = j + 1

        return "".join(arr)