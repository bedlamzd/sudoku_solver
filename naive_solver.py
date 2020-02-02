from copy import deepcopy
from sudoku_tools import possible_entries, print_grid, GRID_SIDE_LENGTH, valid_solution


def naive_solver(grid) -> tuple:
    """
    goes through the grid and in each empty cell check for possible values
    if there is only one possible value then places it in the cell
    :param list grid: sudoku grid
    :return: new grid with filled in values
    """

    def _naive_solver(grid):
        new_grid = deepcopy(grid)
        for row in range(GRID_SIDE_LENGTH):
            for col in range(GRID_SIDE_LENGTH):
                entrie = new_grid[row][col]
                if entrie != 0: continue
                entries = possible_entries(new_grid, row, col)
                if len(entries) == 1: new_grid[row][col] = list(entries)[0]
        return new_grid

    grid_copy = deepcopy(grid)
    iterations = 0
    while True:
        iterations += 1
        new_grid = _naive_solver(grid_copy)
        if new_grid == grid_copy:
            break
        else:
            grid_copy = new_grid
    return valid_solution(grid_copy), grid_copy, iterations


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

    solved, new_grid, iterations = naive_solver(sudoku_grid)
    print('Sudoku solved') if solved else print('Solver stuck')

    print(f'Iterations done: {iterations:4d}')
    print_grid(new_grid)
