#!/usr/bin/python3
"""
N queens puzzle is the challenge of placing
N non-attacking queens on an N x N chessboard
This program solves the N queens problem.
"""
import sys

def is_valid(board, row, col):
  for i in range(row):
    if board[i][col] == 1:
      return False
  for i in range(row):
    for j in range(col):
      if board[i][j] == 1 and abs(i - row) == abs(j - col):
        return False
  return True

def nqueens(N):
  if not isinstance(N, int) or N < 4:
    print("N must be a number and at least 4")
    sys.exit(1)

  board = [[0] * N for _ in range(N)]
  for row in range(N):
    for col in range(N):
      if is_valid(board, row, col):
        board[row][col] = 1
        if nqueens(N - 1):
          for i in range(N):
            for j in range(N):
              print(board[i][j], end=" ")
          print()
        board[row][col] = 0

if __name__ == "__main__":
  N = int(sys.argv[1])
  nqueens(N)

