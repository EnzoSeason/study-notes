class Solution:
    """
    https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/
    """

    def removeDuplicates_stack(self, s: str) -> str:
        stack = []

        for char in s:
            if len(stack) == 0:
                stack.append(char)
            else:
                el = stack[-1]
                if el != char:
                    stack.append(char)
                else:
                    stack.pop()

        return "".join(stack)

    def removeDuplicates_two_pointers(self, s: str) -> str:
        i, j = 0, 0
        arr = list(s)
        
        while j < len(arr):
            arr[i] = arr[j]
            if i > 0 and arr[i - 1] == arr[i]:
                i -= 2
            i += 1
            j += 1
            
        return "".join(arr[0: i])