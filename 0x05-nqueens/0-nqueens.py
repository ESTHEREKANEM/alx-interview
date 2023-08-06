#!/usr/bin/python3
"""
N queens puzzle is the challenge of placing
N non-attacking queens on an N x N chessboard
This program solves the N queens problem.
"""

import sys


def is_board_ok(chessboard: list, row: int, col: int):
    """check if the board is valid for the given row and column"""
    for i in range(row):
        if chessboard[i] == col:
            return False
        if abs(chessboard[i] - col) == abs(i - row):
            return False
    return True


def n_queens(chessboard: list, row: int):
    """solves the N queens problem"""
    n = len(chessboard)
    if row == n:
        result = []
        for i in range(n):
            result.append([i, chessboard[i]])
        print(result)
    else:
        for col in range(n):
            if is_board_ok(chessboard, row, col):
                chessboard[row] = col
                n_queens(chessboard, row + 1)


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

    n_queens([0] * n, 0)
