from sudoku_tools import possible_entries, print_grid, find_zero_cell
from copy import deepcopy


def backtrack_solver(grid, *, calls=0):
    calls += 1
    new_grid = deepcopy(grid)  # copy grid to avoid changes in the original
    i, j = find_zero_cell(new_grid)
    if i is None: return True, new_grid, calls  # if no zero cells then sudoku is solved
    for value in possible_entries(new_grid, i, j):
        new_grid[i][j] = value
        solved, new_grid, calls = backtrack_solver(new_grid, calls=calls)
        if not solved:
            new_grid[i][j] = 0
        else:
            return True, new_grid, calls
    return False, new_grid, calls  # if no value fit, then backtrack


if __name__ == '__main__':
    sudoku_grid = [[5, 0, 0, 0, 0, 0, 7, 0, 9],
                   [0, 4, 0, 9, 2, 0, 0, 6, 0],
                   [7, 6, 0, 0, 0, 0, 0, 3, 0],
                   [0, 0, 6, 0, 1, 5, 0, 0, 0],
                   [0, 8, 1, 0, 7, 0, 4, 0, 0],
                   [9, 0, 0, 6, 0, 0, 0, 0, 8],
                   [0, 0, 4, 2, 6, 0, 0, 0, 1],
                   [0, 0, 0, 7, 0, 4, 2, 0, 0],
                   [0, 9, 0, 0, 0, 1, 0, 0, 0]]

    _, solved_grid, calls = backtrack_solver(sudoku_grid)

    print(f'Steps done: {calls:5}')
    print_grid(solved_grid)
