def bf(main_str: str, pattern: str) -> int:
    n = len(main_str)
    m = len(pattern)
    for idx_main in range(n - m + 1):
        count = 0
        for idx_sub in range(m):
            if pattern[idx_sub].lower() != main_str[idx_main+idx_sub].lower():
                break
            count += 1
        if count == m:
            return idx_main
    return -1

if __name__ == "__main__":
    main = "aababc"
    sub = "abc"
    res = bf(main, sub)
    print(res)