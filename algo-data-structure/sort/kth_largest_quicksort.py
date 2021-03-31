def _partition(arr, start, end):
    pivot_idx = start

    for i in range(start, end - 1):
        if arr[i] > arr[end - 1]:
            arr[i], arr[pivot_idx] = arr[pivot_idx], arr[i]
            pivot_idx += 1
        
    arr[end - 1], arr[pivot_idx] = arr[pivot_idx], arr[end - 1]
    
    return pivot_idx

def _worker(nums, start, end, k):
    print(start, end, k)
    if start == 0 and end - 1 == 0:
        if k == 1: return nums[start]
        else: return
    
    pivot_idx = _partition(nums, start, end)
    print('k = ', k)
    print('nums[{}] == {}'.format(pivot_idx, nums[pivot_idx]))
    print(nums)

    if pivot_idx ==  k - 1: return nums[pivot_idx]

    if pivot_idx > k - 1:
        nums = nums[start:pivot_idx]
        return _worker(nums, 0, len(nums), k)
    else:
        nums = nums[pivot_idx+1: end]
        return _worker(nums,  0, len(nums), k - (pivot_idx - start) - 1)

def kth_largest(nums, k):
    copied_nums = nums.copy()
    n = len(copied_nums)

    if k == 0: return
    if n == 0: return
    
    item = _worker(copied_nums, 0, n, k)

    return [item, copied_nums]

if __name__ == "__main__":
    arr = [3,2,1,5,6,4]
    k = 2
    
    [item, sorted_arr] = kth_largest(arr, k)
    
    print('orignal: ', arr)
    print('k: ', k)
    print('sorted: ', sorted_arr)
    print('item: ', item)