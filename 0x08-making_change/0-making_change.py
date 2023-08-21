#!/usr/bin/python3
'''Given a pile of coins of different values,
    determine the fewest number of coins needed to meet
    a given amount total.
'''
from sys import maxsize


def make_change(coins, total):
    '''
    Calculate the fewest number of coins needed to meet the given total amount.

    Args:
        coins (list of int): A list of coin values.
        total (int): The target total amount.

    Returns:
        int: The minimum number of coins needed to meet the total. Return -1 if it's not possible.
    '''
    if total <= 0:
        return 0
    table = [maxsize for _ in range(total + 1)]
    table[0] = 0
    m = len(coins)
    for i in range(1, total + 1):
        for j in range(m):
            if coins[j] <= i:
                subres = table[i - coins[j]]
                if subres != maxsize and subres + 1 < table[i]:
                    table[i] = subres + 1

    if table[total] == maxsize:
        return -1
    return table[total]
