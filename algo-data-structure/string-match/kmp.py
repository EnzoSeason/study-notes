from typing import List


def generate_next_from_PTM(pattern: str) -> List[int]:
    m = len(pattern)
    next_arr = [-1 for _ in range(m+1)]

    # use fast-slow pointers
    i = 0
    j = -1
    while i < m:
        if j == -1 or pattern[i] == pattern[j]:
            # This case means the partial match is found (pattern[i] == pattern[j]),
            # or no partial match is found. (j == -1)
            # In either case, we can add value to next_arr
            
            # Because next_arr is one space back than PTM, 
            # so we need increase i before assigning the value.
            i += 1

            # Because j starts with -1, 
            # so we need increase j before assigning the value.
            j += 1

            next_arr[i] = j
        else:
            # In this case, the partial match is not found,
            # but we don't know whether there is no match.
            # So, we move to the previous match.
            # To do that, we need to move j and hold i.
            j = next_arr[j]
    return next_arr


def kmp(main: str, pattern: str) -> int:
    n = len(main)
    m = len(pattern)
    next_arr = generate_next_from_PTM(pattern)
    print(next_arr)

    # use fast-slow pointers
    i = 0
    j = 0
    while i < n and j < m:
        if j == -1 or main[i] == pattern[j]:
            # check the next character in the main string
            i += 1
            j += 1
        else:
            # Thanks to moving one space back than PTM
            # If pattern[j] is the bad character, (main[i] != pattern[j])
            # We check next_arr[j] instead of PTM[j-1], which are the same.
            j = next_arr[j]
            # This line also implies the slide of pattern.
            # Because the pointer i is not moved, the slide of pattern is i - j 
    
    if j == m:
        return i - j
    else:
        return -1


if __name__ == "__main__":
    main = "ababababca"
    pattern = "abababca"
    res = kmp(main, pattern)
    print(res)
