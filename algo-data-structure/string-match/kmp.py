from typing import List


def generate_next_from_PTM(pattern: str) -> List[int]:
    m = len(pattern)
    next_arr = [-1 for _ in range(m+1)]

    i = 0
    j = -1
    while i < m:
        if j == -1 or pattern[i] == pattern[j]:
            i += 1
            j += 1
            next_arr[i] = j
        else:
            j = next_arr[j]
    return next_arr


def kmp(main: str, pattern: str) -> int:
    n = len(main)
    m = len(pattern)
    next_arr = generate_next_from_PTM(pattern)
    print(next_arr)

    i = 0
    j = 0
    while i < n and j < m:
        if j == -1 or main[i] == pattern[j]:
            # check the next character in the main string
            i += 1
            j += 1
        else:
            # Thanks to moving one space back in PTM
            # If pattern[j] is the bad character, (main[i] != pattern[j])
            # We check next_arr[j] instead of PTM[j-1], which are the same.
            j = next_arr[j]
    
    if j == m:
        return i - j
    else:
        return -1


if __name__ == "__main__":
    main = "ababababca"
    pattern = "abababca"
    res = kmp(main, pattern)
    print(res)
