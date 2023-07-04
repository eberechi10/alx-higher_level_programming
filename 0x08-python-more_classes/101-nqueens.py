#!/usr/bin/python3

""" solves the N queens problem."""
import sys

if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

try:
    SIZE = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    sys.exit(1)

if SIZE < 4:
    print("N must be at least 4")
    sys.exit(1)


def solve_n_queens(N: int):
    """sum possible solutions for problem of a given N.

    Args:
        N (int): Dimenstion of chessboard / number of queens.
    """
    def is_safe(board, row, col):
        # Check if is safe to place a queen at a given position
        for e in range(row):
            if board[e] == col or \
                    board[e] - e == col - row or \
                    board[e] + e == col + row:
                return False
        return True

    def solve(board, row):
        if row == N:
            # All queens have been placed, print the solution
            print([[e, board[e]] for e in range(N)])
        else:
            for col in range(N):
                if is_safe(board, row, col):
                    board[row] = col
                    solve(board, row + 1)

    board = [-1] * N
    solve(board, 0)


if __name__ == "__main__":
    solve_n_queens(SIZE)
