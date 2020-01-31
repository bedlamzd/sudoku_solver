from sudoku_tools import possible_entries, print_grid
from copy import deepcopy

GRID_SIDE_LENGTH = 9  # side length


def check(grid, row, col, value) -> bool:
    """
    check if value is possible at grid[row][col] cell
    :param list grid: sudoku grid
    :param int row: cell row
    :param int col: cell column
    :param int value: value to check
    :return: True if value is possible, False otherwise
    """
    return True if value in possible_entries(grid, row, col) else False


def unravel(idx) -> tuple:
    """
    converts flat index into (row, column) tuple for sudoku grid
    :param int idx:
    :return: (row, column)
    """
    i = idx // GRID_SIDE_LENGTH
    j = idx % GRID_SIDE_LENGTH
    return i, j


def given_idc(grid) -> list:
    """
    find flat indices of cells with given values
    :param list grid: sudoku grid
    :return: list of indices
    """
    idc = []
    idx = 0
    for row in grid:
        for cell in row:
            if cell != 0:
                idc.append(idx)
            idx += 1
    return idc


def find_zero_cell(grid):
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell == 0:
                return i, j
    return None, None


def backtrack_solve(grid, *, calls=0):
    calls += 1
    new_grid = deepcopy(grid) # copy grid to avoid changes in the original
    i, j = find_zero_cell(new_grid)
    if i is None: return True, new_grid, calls  # if no zero cells then sudoku is solved
    for value in possible_entries(new_grid, i, j):
        new_grid[i][j] = value
        solved, new_grid, calls = backtrack_solve(new_grid, calls=calls)
        if not solved:
            new_grid[i][j] = 0
        else:
            return True, new_grid, calls
    return False, new_grid, calls  # if no value fit, then backtrack


sudoku_grid = [[5, 0, 0, 0, 0, 0, 7, 0, 9],
               [0, 4, 0, 9, 2, 0, 0, 6, 0],
               [7, 6, 0, 0, 0, 0, 0, 3, 0],
               [0, 0, 6, 0, 1, 5, 0, 0, 0],
               [0, 8, 1, 0, 7, 0, 4, 0, 0],
               [9, 0, 0, 6, 0, 0, 0, 0, 8],
               [0, 0, 4, 2, 6, 0, 0, 0, 1],
               [0, 0, 0, 7, 0, 4, 2, 0, 0],
               [0, 9, 0, 0, 0, 1, 0, 0, 0]]

_, solved_grid, calls = backtrack_solve(sudoku_grid)

print(f'Steps done: {calls:5}')
print_grid(solved_grid)
