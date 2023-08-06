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
  solutions = []
  for row in range(N):
    for col in range(N):
      if is_valid(board, row, col):
        board[row][col] = 1
        if nqueens(N - 1):
          solutions.append(board)
        board[row][col] = 0
  return solutions

def parse_args():
  args = sys.argv[1:]
  if len(args) != 1:
    print("Usage: nqueens N")
    sys.exit(1)
  N = int(args[0])
  return N

def main():
  N = parse_args()
  solutions = nqueens(N)
  for solution in solutions:
    for row in solution:
      print(*row, end=" ")
    print()

if __name__ == "__main__":
  main()
