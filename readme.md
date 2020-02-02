# Sudoku solver and generator

**naive_solver** - simple implementation for solving sudoku, works only on easy
puzzles. Iterates over sudoku and fills values in where only one possibility is.
Then repeats until there is no such cells or sudoku is solved.

**backtrack_solver** - uses backtrack algorithm to solve puzzles.

**sudoku_generator** - generates random puzzle of certain "difficulty" (different number of clues).\
Generates random complete grid. Then deletes given number of cells consequentially. On each deletion checks
if grid is valid and there is unique solution.\
Uniqueness checked by slightly different backtracking algorithm which can count solutions.
