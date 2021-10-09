from typing import List


def generate_next_from_PTM(pattern: str) -> List[int]:
    next_arr = [-1 for _ in range(len(pattern) + 1)]

    #  use fast-slow pointers
    i, j = 0, -1
    while i < len(pattern):
        while j >= 0 and pattern[i] != pattern[j]:
            j = next_arr[j]
        j += 1
        i += 1
        next_arr[i] = j

    return next_arr


def kmp(main: str, pattern: str) -> int:
    next_arr = generate_next_from_PTM(pattern)

    i, j = 0, 0
    while i < len(main) and j < len(pattern):
        while j >= 0 and main[i] != pattern[j]:
            j = next_arr[j]
        i += 1
        j += 1

    return i - j if j == len(pattern) else -1


if __name__ == "__main__":
    main = "ababababca"
    pattern = "abababca"
    res = kmp(main, pattern)
    print(res)
