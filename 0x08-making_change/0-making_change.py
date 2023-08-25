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
    if total <= 0:
        return 0
    
    dp = [float("inf")] * (total + 1)
    dp[0] = 0
    
    for amount in range(1, total + 1):
        for coin_value in coins:
            if coin_value <= amount:
                dp[amount] = min(dp[amount], dp[amount - coin_value] + 1)
    
    if dp[total] != float("inf"):
        return dp[total]
    else:
        eturn -1
