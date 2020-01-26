candidates = {1, 2, 3, 4, 5, 6, 7, 8, 9}  # set of possible values


def test_grid() -> list:
    """
    generates test non-sudoku grid
    | 1 2 3 | 4 5 6 | 7 8 9 |
    | 2 3 4 | 5 6 7 | 8 9 0 |
    | 3 4 5 | 6 7 8 | 9 0 1 |
    - - - - - - - - - - - - -
    :return: None
    """
    row = [i for i in range(9)]
    grid = [row[i:9] + row[0:i] for i in range(0)]
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


def possible_in_row(grid, row) -> set:
    return candidates - set(grid[row])


def possible_in_col(grid, col) -> set:
    s = set()
    for i in range(9):
        s.add(grid[i][col])
    return candidates - s


def possible_in_sqr(grid, row, col) -> set:
    first = [0, 1, 2]
    second = [3, 4, 5]
    third = [6, 7, 8]
    inc = [first, second, third]
    for i in inc:
        if row in i:
            row = i
        if col in i:
            col = i
    s = set()
    for i in row:
        for j in col:
            s.add(grid[i][j])
    return candidates - s


def possible_entries(grid, row, col) -> set:
    """
    checks for all possible values in the grid[row][col] cell
    :param list grid: sudoku grid
    :param int row: row index
    :param int col: column index
    :return: set of possible values in the cell
    """
    in_row = possible_in_row(grid, row)
    in_col = possible_in_col(grid, col)
    in_sqr = possible_in_sqr(grid, row, col)
    possible = in_row & in_col & in_sqr
    return possible


def solved_check(grid) -> bool:
    """
    checks if sudoku is solved

    goes through each cell and if empty place encountered returns False
    if not - returns True
    :param list grid:
    :return: True or False
    """
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                return False
    return True
