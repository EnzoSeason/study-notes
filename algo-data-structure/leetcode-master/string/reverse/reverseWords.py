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

    def reverseWords_O1(self, s: str) -> str:
        """
        1. reverse the entire string
        2. reverse each word and remove extra spaces
        3. remove all the spaces at the tail

        Time complexity: O(N)
        Space complexity: O(1)
        """

        arr = list(s)
        # reverse string
        self.reverse(arr, 0, len(arr))

        # reverse words
        i = 0
        while i < len(arr):
            if arr[i] == " ":
                # remove the space before the word
                arr.pop(i)
            else:
                # reverse the word, arr[i:j]
                j = i
                while j < len(arr) and arr[j] != " ":
                    j += 1
                self.reverse(arr, i, j)
                # arr[j] is the space right after the word.
                # So the next character to check is arr[j + 1]
                i = j + 1
        # remove the spaces at the tail
        while arr[-1] == " ":
            arr.pop()

        return "".join(arr)