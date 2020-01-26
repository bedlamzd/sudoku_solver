import copy
from sudoku_tools import possible_entries, print_grid, solved_check

sudoku_grid = [[5, 0, 0, 0, 0, 0, 7, 0, 9],
               [0, 4, 0, 9, 2, 0, 0, 6, 0],
               [7, 6, 0, 0, 0, 0, 0, 3, 0],
               [0, 0, 6, 0, 1, 5, 0, 0, 0],
               [0, 8, 1, 0, 7, 0, 4, 0, 0],
               [9, 0, 0, 6, 0, 0, 0, 0, 8],
               [0, 0, 4, 2, 6, 0, 0, 0, 1],
               [0, 0, 0, 7, 0, 4, 2, 0, 0],
               [0, 9, 0, 0, 0, 1, 0, 0, 0]]


def naive_solver(grid) -> list:
    """
    goes through the grid and in each empty cell check for possible values
    if there is only one possible value then places it in the cell
    :param list grid: sudoku grid
    :return: new grid with filled in values
    """
    new_grid = copy.deepcopy(grid)
    for row in range(9):
        for col in range(9):
            entrie = new_grid[row][col]
            if entrie != 0: continue
            entries = possible_entries(new_grid, row, col)
            if len(entries) == 1: new_grid[row][col] = list(entries)[0]
    return new_grid


iterations = 0  # number of iterations through whole grid

while True:
    iterations += 1
    grid = naive_solver(sudoku_grid)
    if grid == sudoku_grid:  # check if solver inserted any new values
        print('Sudoku solved') if solved_check(grid) else print('Solver stuck')
        break
    else:
        sudoku_grid = grid

print(f'Iterations done: {iterations:4d}')
print_grid(grid)
