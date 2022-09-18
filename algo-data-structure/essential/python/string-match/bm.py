from typing import List


def generateBC(pattern: str) -> dict:
    """
    For Bad Character Rule

    generate a hash map which
    saves the lastest postion of each character in the pattern
    """
    hash_map = {}
    for i, c in enumerate(pattern):
        hash_map[c] = i
    return hash_map


def generateGS(pattern: str) -> tuple:
    """
    For Good Suffix Rule

    generate 2 array: k means the lenght of the suffix
    - suffix_latest_appearAt[k] = -1

       the latest matched part index of pattern[m-k:m]

       (Part index is the index of the first element in the part.)

    - prefix_is_matched[k] = False

       If pattern[m-k:m] matches pattern[0:k+1]
    """
    m = len(pattern)
    suffix_latest_appearAt = [-1 for _ in range(m)]
    prefix_is_matched = [False for _ in range(m)]

    for i in range(m - 1):
        j = i
        k = 0
        # traverse the prefix and the suffix of the pattern
        while j >= 0 and pattern[j] == pattern[m - 1 - k]:
            j -= 1
            k += 1
            suffix_latest_appearAt[k] = j + 1
        if j == -1:
            prefix_is_matched[k] = True

    return suffix_latest_appearAt, prefix_is_matched


def makeGoodSuffixMove(
    j: int, m: int, suffix_latest_appearAt: List[int], prefix_is_matched: List[bool]
) -> int:
    """
    - j: current traversing index in the pattern
    - m: the lenght of the pattern
    """
    #  The lenght of the suffix
    k = m - 1 - j
    # case 1: The good suffix exists in the pattern
    if suffix_latest_appearAt[k] != -1:
        return j - suffix_latest_appearAt[k] + 1
    # case 2: The suffix of good suffix matches the prefix of pattern
    # j+1 is included in the case 1, so we start at j+2
    for r in range(j + 2, m):
        if prefix_is_matched[m - r]:
            return r
    # case 3: no match between the good suffix and the prefix of pattern
    return m


def bm(main: str, pattern: str) -> int:
    n = len(main)
    m = len(pattern)
    # prepare for bad character rule
    pattern_map = generateBC(pattern)
    # prepare for good suffix rule
    suffix_latest_appearAt, prefix_is_matched = generateGS(pattern)
    i = 0
    while i <= n - m:
        j = m - 1
        while j >= 0:
            if main[i + j] != pattern[j]:
                break
            j -= 1
        if j < 0:  # Pattern is found in main
            return i
        bad_character_move = (
            j - pattern_map[main[i + j]] if main[i + j] in pattern_map else j + 1
        )
        good_suffix_move = 0
        if j < m - 1:
            good_suffix_move = makeGoodSuffixMove(
                j, m, suffix_latest_appearAt, prefix_is_matched
            )

        i += max(bad_character_move, good_suffix_move)

    return -1


if __name__ == "__main__":
    main = "aabababc"
    pattern = "abc"
    res = bm(main, pattern)
    print(res)
