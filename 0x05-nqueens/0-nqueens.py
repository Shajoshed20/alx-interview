#!/usr/bin/python3
"""A program that solves the N queens problem."""

import sys


def is_safe(n, q, array):
    if q in array:
        return (False)
    else:
        return all(abs(array[column] - q) != n - column
                   for column in range(n))


def solve_nqueens(board, column, prev):
    safe_position = []
    for array in prev:
        for x in range(column):
            if is_safe(board, x, array):
                safe_position.append(array + [x])
    return safe_position


def print_solution(row, column):
    sol = [[]]
    for queen in range(row):
        sol = solve_nqueens(queen, column, sol)
    return sol


def init_board():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
        if N < 4:
            print("N must be at least 4")
            sys.exit(1)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    return (N)


def main():

    N = init_board()
    sol = print_solution(N, N)
    for array in sol:
        clean = []
        for n, q in enumerate(array):
            clean.append([n, q])
        print(clean)


if __name__ == '__main__':
    main()
