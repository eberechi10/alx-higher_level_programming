#!/usr/bin/python3

"""a program to resolve the N-Queen puzzle"""

import sys


def init_board(n):

    """Initialize sized chessboard"""
    node = []
    [node.append([]) for e in range(n)]
    [row.append(' ') for e in range(n) for row in node]
    return (node)


def node_copy(node):

    """copy of a chessboard."""
    if isinstance(node, list):
        return list(map(node_copy, node))
    return (node)


def get_solved(node):

    """representation of a solved chessboard."""
    solved = []
    for p in range(len(node)):
        for c in range(len(node)):
            if node[p][c] == "Q":
                solved.append([p, c])
                break
    return (solved)


def xout(node, row, col):

    """spots on a chessboard.
    spots where non-attacking queens can't
    be played out.
    Args:
        node: working chessboard.
        row: row last played.
        col: column last played.
    """

    for c in range(col + 1, len(node)):
        node[row][c] = "x"
    for c in range(col - 1, -1, -1):
        node[row][c] = "x"
    for p in range(row + 1, len(node)):
        node[p][col] = "x"
    for p in range(row - 1, -1, -1):
        node[p][col] = "x"
    c = col + 1
    for p in range(row + 1, len(node)):
        if c >= len(node):
            break
        node[p][c] = "x"
        c += 1
    c = col - 1
    for p in range(row - 1, -1, -1):
        if c < 0:
            break
        board[p][c]
        c -= 1
    c = col + 1
    for p in range(row - 1, -1, -1):
        if c >= len(node):
            break
        node[p][c] = "x"
        c += 1
    c = col - 1
    for p in range(row + 1, len(node)):
        if c < 0:
            break
        node[p][c] = "x"
        c -= 1


def recur_solved(node, row, queens, solved):

    """solve N-queens puzzle.
    Args:
        node: working chessboard.
        row: current row.
        queens: current placed queens.
        solved: lists of solve.
    """
    if queens == len(node):
        solved.append(get_solved(node))
        return (solved)

    for c in range(len(node)):
        if node[row][c] == " ":
            elm_node = node_copy(node)
            elm_node[row][c] = "Q"
            xout(elm_node, row, c)
            solved = recur_solved(elm_node, row + 1, queens + 1, solved)

    return (solved)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit() is False:
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    node = init_node(int(sys.argv[1]))
    solved = recur_solved(node, 0, 0, [])
    for pt in solved:
        print(pt)
