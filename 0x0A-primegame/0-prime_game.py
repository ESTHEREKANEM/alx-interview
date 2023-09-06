#!/usr/bin/python3
"""
Maria and Ben are playing a game. Given a set of consecutive integers
starting from 1 up to and including n,
they take turns choosing a prime number from the set
and removing that number and its multiples from the set.
The player that cannot make a move loses the game.
"""


def prime_number(p):
    """
    function to get prime numbers
    """
    for i in range(p):
        if p % 2 == 0:
            return False
        else:
            return True


def isWinner(x, nums):
    """
    x rounds of the game, where n may be different for each round.
    Assuming Maria always goes first and both players play optimally,
    determine who the winner of each game is
    """
    count = 0
    for i in range(1, x):
        count += 1
    for j in nums:
        if prime_number(j):
            continue
    if count % j == 0:
        return 'Maria'
    else:
        return 'Ben'
