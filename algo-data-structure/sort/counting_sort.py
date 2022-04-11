from typing import List


def _accumulate_bincount(nums: List[int]) -> List[int]:
    len_acc_bincounts = max(nums) + 1
    acc_bincounts = [0 for _ in range(len_acc_bincounts)]

    ## bincount
    for num in nums:
        acc_bincounts[num] += 1
    ## accumulate
    for i in range(1, len_acc_bincounts):
        acc_bincounts[i] += acc_bincounts[i - 1]

    return acc_bincounts


def _fill_sorted_nums(nums: List[int], acc_bincounts: List[int]) -> List[int]:
    sorted_nums = [0 for _ in nums]
    ## The order is important.
    ## Sorting from bottom to top makes sort stable.
    i = len(nums) - 1

    while i >= 0:
        acc_count = acc_bincounts[nums[i]]
        sorted_nums[acc_count - 1] = nums[i]

        acc_bincounts[nums[i]] -= 1
        i -= 1

    return sorted_nums


def counting_sort(nums: List[int]) -> List[int]:
    acc_bincounts = _accumulate_bincount(nums)
    sorted_nums = _fill_sorted_nums(nums, acc_bincounts)

    return sorted_nums


if __name__ == "__main__":
    nums = [2, 5, 3, 0, 2, 3, 0, 3]

    sorted_nums = counting_sort(nums)

    print("orignal: ", nums)
    print("sorted: ", sorted_nums)
