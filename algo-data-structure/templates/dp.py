from typing import Any


def dp(data: list) -> Any:
    #  1. init dp
    n = len(data)
    dp = [-1] * (n + 1)

    #  2. init the initial state
    dp[0] = 0

    #  3. get dp[i] from dp[0:i]
    for i in range(1, n + 1):
        dp[i] = f([dp[j] for j in range(i)])

    #  4. return the final state
    return dp[n]

def f(prev_dp: list) -> Any:
    return