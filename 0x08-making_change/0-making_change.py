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
    Total = [float("inf")] * (total + 1)

    Total[0] = 0
    n = len(coins)

    for i in range(1, n + 1):
        for j in range(total + 1):
            if coins[i - 1] <= j:
                Total[j] = min(Total[j], Total[j - coins[i - 1]] + 1)
    if Total[-1] != float("inf"):
        return Total[-1]
    else:
        return -1
