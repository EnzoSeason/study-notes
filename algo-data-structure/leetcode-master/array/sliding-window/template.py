def slideWindow(arr: list, targets: list, limit: int) -> list:
    # dict_t records the number of each elements in the targets
    dict_t = {}
    for t in targets:
        dict_t[t] = dict_t.get(t, 0) + 1
    ## window records the number of each elements in the sliding window
    window = {}
    ## res = (max_window_length, start_idx, end_idx)
    res = (-1, 0, 0)
    
    l, r = 0, 0
    while r < len(arr):
        ## inscrease the window
        window[arr[r]] = window.get(arr[r], 0) + 1

        while len(window) > limit:
            ## reduce the size of the window
            window[arr[l]] -= 1
            if window[arr[l]] == 0:
                window.pop(arr[l])
            l += 1
        
        # update the res
        if r - l + 1 > res[0]:
            res[0] = r - l + 1
            res[1] = l
            res[2] = r

        r += 1
    
    return arr[res[1]: res[2]]
