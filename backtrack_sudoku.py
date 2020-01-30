from sudoku_tools import possible_entries, print_grid

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


sudoku_grid = [[5, 0, 0, 0, 0, 0, 7, 0, 9],
               [0, 4, 0, 9, 2, 0, 0, 6, 0],
               [7, 6, 0, 0, 0, 0, 0, 3, 0],
               [0, 0, 6, 0, 1, 5, 0, 0, 0],
               [0, 8, 1, 0, 7, 0, 4, 0, 0],
               [9, 0, 0, 6, 0, 0, 0, 0, 8],
               [0, 0, 4, 2, 6, 0, 0, 0, 1],
               [0, 0, 0, 7, 0, 4, 2, 0, 0],
               [0, 9, 0, 0, 0, 1, 0, 0, 0]]

given = given_idc(sudoku_grid)  # list of indices of given values
visited = []  # list of indices of visited cells
flat_idx = 0  # flattened array index of a current cell
steps = 0  # how many steps is done
value = 0  # value to write in cell

while flat_idx < GRID_SIDE_LENGTH ** 2:
    row, col = unravel(flat_idx)
    if sudoku_grid[row][col] != 0 and flat_idx in given:  # skip if a given cell
        steps += 1
        flat_idx += 1
        continue
    for value in range(value, 10):
        steps += 1
        if check(sudoku_grid, row, col, value):
            sudoku_grid[row][col] = value
            visited.append(flat_idx)
            value = 0
            flat_idx += 1
            break
    else:
        steps += 1
        sudoku_grid[row][col] = 0
        flat_idx = visited.pop()
        row, col = unravel(flat_idx)
        value = sudoku_grid[row][col] + 1

print(f'Steps done: {steps:5}')
print_grid(sudoku_grid)
