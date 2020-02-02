from sudoku_tools import GRID_SIDE_LENGTH, possible_entries, print_grid, given_idc, unravel, find_zero_cell, \
    valid_solution
from copy import deepcopy
import random


def random_full(*, calls=0) -> tuple:
    """
    generate random proper complete sudoku
    :return: sudoku grid and number of calls
    """
    calls += 1
    grid = [[0 for _ in range(GRID_SIDE_LENGTH)] for _ in range(GRID_SIDE_LENGTH)]
    for i, row in enumerate(grid):
        for j, _ in enumerate(row):
            try:
                grid[i][j] = random.choice(tuple(possible_entries(grid, i, j)))
            except IndexError:
                return random_full(calls=calls)
    return grid, calls


def find_random_nonzero(grid, exclude=None) -> tuple:
    """
    find index of random non empty cell in grid
    :param list grid: sudoku grid
    :param list exclude: (i, j) indices to exlude from search
    :return: (i, j) indices of a cell
    """
    given = [unravel(idx) for idx in given_idc(grid)]
    if exclude:
        for idx in exclude:
            if idx in given:
                given.remove(idx)
    i, j = random.choice(given)
    return i, j


def delete_random(grid, exclude=None) -> list:
    """
    return new grid with random non empty cell deleted
    :param list grid: sudoku grid
    :return: new sudoku grid
    """
    new_grid = deepcopy(grid)
    i, j = find_random_nonzero(new_grid, exclude=exclude)
    new_grid[i][j] = 0
    return new_grid


def count_solutions(grid, *, calls=0, solutions=0, grids=None, only_uniqueness=False):
    """
    Finds solutions to a sudoku puzzle

    based on backtracking algorithm where all the possibilities except invalid are checked
    :param list grid: sudoku grid to find solutions to
    :param int calls: number of times function have been called
    :param int solutions: number of solutions to a puzzle
    :param list grids: list of possible solutions
    :return: solutions, calls, grids
    """
    calls += 1
    if not grids: grids = []
    grid_copy = deepcopy(grid)  # copy grid to avoid changes in the original
    i, j = find_zero_cell(grid_copy)
    if i is None:
        grids.append(grid_copy)
        return solutions + 1, calls, grids  # if no zero cells then sudoku is solved
    values = possible_entries(grid_copy, i, j)
    for value in values:
        grid_copy[i][j] = value
        solutions, calls, grids = count_solutions(grid_copy, calls=calls, solutions=solutions, grids=grids,
                                                  only_uniqueness=only_uniqueness)
        if only_uniqueness:
            if solutions > 1:
                return solutions, calls, grids
    return solutions, calls, grids  # if no value fit, then backtrack


if __name__ == '__main__':
    difficulties = {'easy': 40, 'medium': 30, 'hard': 20}  # number of clues for puzzle
    difficulty = 'Medium'

    answer, iterations = random_full()
    while not valid_solution(answer):
        answer, iterations = random_full()

    print(f'Full sudoku generated.\n'
          f'Iterations required: {iterations:5}')
    print_grid(answer)

    puzzle = deepcopy(answer)
    clues = difficulties[difficulty.lower()]  # minimal number of clues for puzzle
    given = given_idc(puzzle)  # number of clues in puzzle
    exclude = []  # indices of cells to exclude from deletion
    iterations = 0

    while len(given) > clues and len(given) > len(exclude):  # delete cells until certain number of clues
        i, j = find_random_nonzero(puzzle, exclude=exclude)
        grid = deepcopy(puzzle)
        grid[i][j] = 0
        solutions, calls, puzzle_solution = count_solutions(grid, only_uniqueness=True)
        iterations += calls
        if solutions != 1:
            exclude.append((i, j))
        else:
            exclude = []
            puzzle = grid
            given = given_idc(puzzle)

    print(f'Puzzle generated.\n'
          f'Recursions done: {iterations: 5}\n'
          f'Number of clues: {len(given_idc(puzzle)):2}\n'
          f'Difficulty: {difficulty}')
    print_grid(puzzle)
