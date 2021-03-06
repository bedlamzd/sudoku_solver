CANDIDATES = {1, 2, 3, 4, 5, 6, 7, 8, 9}  # set of possible values
GRID_SIDE_LENGTH = 9  # side length


def test_grid() -> list:
    """
    generates test non-sudoku grid
    | 1 2 3 | 4 5 6 | 7 8 9 |
    | 2 3 4 | 5 6 7 | 8 9 0 |
    | 3 4 5 | 6 7 8 | 9 0 1 |
    - - - - - - - - - - - - -
    :return: 9x9 matrix
    """
    row = [i for i in range(GRID_SIDE_LENGTH)]
    grid = [row[i:GRID_SIDE_LENGTH] + row[:i] for i in range(GRID_SIDE_LENGTH)]
    return grid


def print_grid(grid):
    """
    prints sudoku grid in a formatted way
    :param list grid: sudoku grid
    :return: None
    """
    print('- ' * 13)
    for i, row in enumerate(grid):
        print('|', end=' ')
        for j, cell in enumerate(row):
            print(cell, end=' ')
            if (j + 1) % 3 == 0: print('|', end=' ')
        print()
        if (i + 1) % 3 == 0: print('- ' * 13)
    print()


def possible_in_row(grid, row, col) -> set:
    return CANDIDATES - set(grid[row][:col] + grid[row][col + 1:])


def possible_in_col(grid, row, col) -> set:
    s = set()
    for i in range(GRID_SIDE_LENGTH):
        if i == row:
            continue
        s.add(grid[i][col])
    return CANDIDATES - s


def possible_in_sqr(grid, row, col) -> set:
    first = [0, 1, 2]  # rows/columns of cells which belong to rows/columns of squares
    second = [3, 4, 5]
    third = [6, 7, 8]
    inc = [first, second, third]
    rows, cols = 0, 0
    for i in inc:
        if row in i:
            rows = i
        if col in i:
            cols = i
    s = set()
    for i in rows:
        for j in cols:
            if [i, j] == [row, col]:
                continue
            s.add(grid[i][j])
    return CANDIDATES - s


def possible_entries(grid, row, col) -> set:
    """
    checks for all possible values in the grid[row][col] cell
    :param list grid: sudoku grid
    :param int row: row index
    :param int col: column index
    :return: set of possible values in the cell
    """
    in_row = possible_in_row(grid, row, col)
    in_col = possible_in_col(grid, row, col)
    in_sqr = possible_in_sqr(grid, row, col)
    possible = in_row & in_col & in_sqr
    return possible


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


def valid_solution(grid) -> bool:
    """
    checks if sudoku is properly solved
    i.e. no empty cells and no mistakes
    :param list grid: sudoku grid
    :return: True/False
    """
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if not check(grid, i, j, cell) or cell == 0:
                return False
    return True


def ravel(idx) -> int:
    """
    converts coordinate index (i, j) into flat index for sudoku grid
    :param tuple idx: (row, col) tuple
    :return: flat index
    """
    idx = GRID_SIDE_LENGTH * idx[0] + idx[1]
    return idx


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


def find_zero_cell(grid) -> tuple:
    """
    find first zero cell in a grid
    :param list grid: sudoku grid
    :return: indices (i, j) or (None, None) if no zero cell
    """
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell == 0:
                return i, j
    return None, None
