def hash(val: str) -> int:
    """
    1. Map a-z into their acsii value 
    2. Tranform the value to reversed decimal
    """
    res = 0
    pos = 0
    for i in range(len(val)):
        c = val[i].lower()
        res += ord(c) * (26**pos)
        pos += 1
    return res

def compare(main_str: str, sub_str: str) -> bool:
    n = len(main_str)
    m = len(sub_str)

    if n != m:
        return False

    for i in range(n):
        if main_str[i] != sub_str[i]:
            return False

    return True


def rf(main_str: str, pattern: str) -> int:
    n = len(main_str)
    m = len(pattern)
    pattern_hash = hash(pattern)
    for idx_main in range(n - m + 1):
        sub_str = main_str[idx_main: idx_main + m]
        sub_hash = hash(sub_str)
        if sub_hash == pattern_hash and compare(sub_str, pattern):
            return idx_main
    return -1


if __name__ == "__main__":
    main = "aabababc"
    sub = "abc"
    res = rf(main, sub)
    print(res)
