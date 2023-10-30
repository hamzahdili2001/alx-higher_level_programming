#!/usr/bin/python3
"""Solves the N-queens puzzle"""

import sys


def initialize_board(n):
    """Initialize chessboard with empty spaces."""
    board = [[' ' for _ in range(n)] for _ in range(n)]
    return board


def deepcopy_board(board):
    """Return a deepcopy of a chessboard."""
    return [row.copy() for row in board]


def get_solution(board):
    """Return the list of lists representation of a solved chessboard."""
    solution = []
    for r in range(len(board)):
        for c in range(len(board)):
            if board[r][c] == "Q":
                solution.append([r, c])
                break
    return solution


def mark_non_attacking_positions(board, row, col):
    """Mark spots on a chessboard as non-attacking positions.
    """
    n = len(board)
    # Mark all forward spots
    for c in range(col + 1, n):
        board[row][c] = "x"
    # Mark all backward spots
    for c in range(col - 1, -1, -1):
        board[row][c] = "x"
    # Mark all spots below
    for r in range(row + 1, n):
        board[r][col] = "x"
    # Mark all spots above
    for r in range(row - 1, -1, -1):
        board[r][col] = "x"
    # Mark all spots diagonally down to the right
    r, c = row + 1, col + 1
    while r < n and c < n:
        board[r][c] = "x"
        r += 1
        c += 1
    # Mark all spots diagonally up to the left
    r, c = row - 1, col - 1
    while r >= 0 and c >= 0:
        board[r][c] = "x"
        r -= 1
        c -= 1
    # Mark all spots diagonally up to the right
    r, c = row - 1, col + 1
    while r >= 0 and c < n:
        board[r][c] = "x"
        r -= 1
        c += 1
    # Mark all spots diagonally down to the left
    r, c = row + 1, col - 1
    while r < n and c >= 0:
        board[r][c] = "x"
        r += 1
        c -= 1


def solve_n_queens(board, row, queens, solutions):
    """Recursively solve an N-queens puzzle.
    """
    n = len(board)
    if queens == n:
        solutions.append(get_solution(board))
        return solutions

    for col in range(n):
        if board[row][col] == ' ':
            tmp_board = deepcopy_board(board)
            tmp_board[row][col] = 'Q'
            mark_non_attacking_positions(tmp_board, row, col)
            solutions = solve_n_queens(
                    tmp_board, row + 1, queens + 1, solutions
                    )

    return solutions


def print_solutions(solutions):
    """Print the solutions in the required format."""
    for solution in solutions:
        print([[i, j] for i, j in solution])


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if not sys.argv[1].isdigit():
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    board_size = int(sys.argv[1])
    board = initialize_board(board_size)
    solutions = solve_n_queens(board, 0, 0, [])
    print_solutions(solutions)
