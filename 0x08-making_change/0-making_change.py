#!/usr/bin/python3
"""
Given a pile of coins of different values,
determine the fewest number of coins needed to meet a given amount total
"""


def makeChange(coins, total):
    """
    Given a pile of coins of different values,
    determine the fewest number of coins needed to meet a given amount total
    """
    dp = [float("inf")] * (total + 1)

    dp[0] = 0
    n = len(coins)

    for i in range(1, n + 1):
        for j in range(total + 1):
            if coins[i - 1] <= j:
                dp[j] = min(dp[j], dp[j - coins[i - 1]] + 1)
    if dp[-1] != float("inf"):
        return dp[-1]
    else:
        return -1
