#!/usr/bin/python3

"""module that resolves the N-Queen puzzle"""


def isSafe(board, nqueen):

    """determines if the queens can or can't kill each other

    Args:
        board: queens positions
        nqueen: queen number

    Returns:
        True: can't kill each other
        False: queens can kill

    """

    for e in range(nqueen):

        if board[e] == board[nqueen]:
            return False

        if abs(board[e] - board[nqueen]) == abs(e - nqueen):
            return False

    return True


def solution(m_queen, nqueen):

    """ list with the Queens positions

    Args:
        board: queens positions
        nqueen: queen number

    """

    sol = []

    for e in range(nqueen):
        sol.append([e, board[e]])

    print(sol)


def recursive_sol(board, nqueen):

    """ a recursive that executes the Backtracking

    Args:
        board: queens positions
        nqueen: queen number

    """

    if nqueen is len(board):
        solution(board, nqueen)
        return

    board[nqueen] = -1

    while((board[nqueen] < len(board) - 1)):

        board[nqueen] += 1

        if isSafe(board, nqueen) is True:

            if nqueen is not len(board):
                recursive_sol(board, nqueen + 1)


def sol_NQueen(size):

    """ initialized the Backtracking

    Args:
        size: chessboard size

    """

    board = [-1 for e in range(size)]

    recursive_sol(board, 0)


if __name__ == '__main__':

    import sys

    if len(sys.argv) == 1 or len(sys.argv) > 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        size = int(sys.argv[1])
    except ValueError:  # Catch the specific ValueError if conversion fails
        print("N must be a number")
        sys.exit(1)

    if size < 4:
        print("N must be at least 4")
        sys.exit(1)

    sol_NQueen(size)
