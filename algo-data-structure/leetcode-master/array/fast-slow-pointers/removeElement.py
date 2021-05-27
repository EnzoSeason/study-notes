from typing import List

# https://leetcode.com/problems/remove-element/
class SolutionBrute:
    def removeElement(self, nums: List[int], val: int) -> int:
        i, n = 0, len(nums)

        while i < n:
            if nums[i] == val:
                for j in range(i, n - 1):
                    nums[j] = nums[j + 1]
                n -= 1
            else:
                i += 1

        print(nums[0:n])
        return n


class SolutionSwapEnd:
    def removeElement(self, nums: List[int], val: int) -> int:
        i, n = 0, len(nums)

        while i < n:
            if nums[i] == val:
                nums[i], nums[n - 1] = nums[n - 1], nums[i]
                n -= 1
            else:
                i += 1
        print(nums[0:n])
        return n


class SolutionSlowFast:
    def removeElement(self, nums: List[int], val: int) -> int:
        slow, fast = 0, 0
        while fast < len(nums):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        print(nums[0:slow])
        return slow


if __name__ == "__main__":
    nums = [0, 1, 2, 2, 3, 0, 4, 2]
    val = 2

    sb = SolutionBrute()
    print(sb.removeElement(nums, val))

    se = SolutionSwapEnd()
    print(se.removeElement(nums, val))

    ssf = SolutionSlowFast()
    print(ssf.removeElement(nums, val))