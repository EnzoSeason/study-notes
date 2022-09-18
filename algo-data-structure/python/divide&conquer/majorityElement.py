from typing import List


def majorityElement_re_helper(nums: List[int], l: int, r: int) -> int:
    if l == r:
        return nums[l]

    m = l + (r - l) // 2
    l_maj = majorityElement_re_helper(nums, l, m)
    r_maj = majorityElement_re_helper(nums, m + 1, r)

    if l_maj == r_maj:
        return l_maj

    return (
        l_maj if nums[l : r + 1].count(l_maj) > nums[l : r + 1].count(r_maj) else r_maj
    )


def majorityElement_re(nums: List[int]) -> int:
    return majorityElement_re_helper(nums, 0, len(nums) - 1)


def majorityElement_sort(nums: List[int]) -> int:
    nums.sort()
    return nums[len(nums) // 2]


def majorityElement_hash(nums: List[int]) -> int:
    hash_map = {}
    for num in nums:
        if num in hash_map:
            hash_map[num] += 1
            if hash_map[num] > len(nums) // 2:
                return num
        else:
            hash_map[num] = 1
    return None


if __name__ == "__main__":
    arr = [2, 2, 1, 1, 1, 2, 2]
    maj = majorityElement_hash(arr)
    print(maj)