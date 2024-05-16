#!/usr/bin/python3
"""
This module solves the N queens problem. It uses backtracking algorithm to
place N non-attacking queens on an N×N chessboard
"""
import sys


def is_safe(board, row, column):
    """
    Check if it's safe to place a queen at the given row and column.
    """
    for i in range(row):
        if board[i] == col or \
           board[i] - i == column - row or \
           board[i] + i == column + row:
            return False
    return True


def solve_nqueens(n, row, board, solutions):
    """
    Solve the N-Queens problem using backtracking.
    """
    if row == n:
        solutions.append([[i, board[i]] for i in range(n)])
        return
    for col in range(n):
        if is_safe(board, row, col):
            board[row] = col
            solve_nqueens(n, row + 1, board, solutions)


def nqueens(N):
    """
    Validate the input, initialize the board, and solve the N-Queens problem.
    """
    if not N.isdigit():
        print("N must be a number")
        sys.exit(1)
    N = int(N)
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = []
    board = [-1] * N
    solve_nqueens(N, 0, board, solutions)

    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    """
    Entry point of the program. Validates the command-line arguments and
    calls nqueens function.
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    nqueens(sys.argv[1])
