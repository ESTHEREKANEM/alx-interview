#!/usr/bin/python3
"""
N queens puzzle is the challenge of placing
N non-attacking queens on an N x N chessboard
This program solves the N queens problem.
"""

import sys


def is_safe(chessboard, row, col):
    """Check if the board is valid for the given row and column"""
    for i in range(row):
        if chessboard[i] == col or abs(chessboard[i] - col) == abs(i - row):
            return False
    return True


def solve_nqueens(chessboard, row):
    """Solves the N queens problem"""
    n = len(chessboard)
    if row == n:
        return [tuple((i, chessboard[i])) for i in range(n)]
    solutions = []
    for col in range(n):
        if is_safe(chessboard, row, col):
            chessboard[row] = col
            solutions.extend(solve_nqueens(chessboard, row + 1))
    return solutions


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solve_nqueens([0] * n, 0)
