from typing import List


def binarySearch(asc_array: List[int], target: int) -> bool:
    """
    Find an element in an asc sorted array.
    """

    left, right = 0, len(asc_array) - 1
    while left <= right: #  Attention: "<=" is used
        mid = left + (right - left) // 2 #  "//" is equivalent to floor() 
        if asc_array[mid] == target:
            return True
        elif asc_array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return False