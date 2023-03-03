"""
Input: board = [["5","3",".",".","7",".",".",".","."]
                ["6",".",".","1","9","5",".",".","."]
                [".","9","8",".",".",".",".","6","."]
                ["8",".",".",".","6",".",".",".","3"]
                ["4",".",".","8",".","3",".",".","1"]
                ["7",".",".",".","2",".",".",".","6"]
                [".","6",".",".",".",".","2","8","."]
                [".",".",".","4","1","9",".",".","5"]
                [".",".",".",".","8",".",".","7","9"]]
Output: [["5","3","4","6","7","8","9","1","2"]
         ["6","7","2","1","9","5","3","4","8"]
         ["1","9","8","3","4","2","5","6","7"]
         ["8","5","9","7","6","1","4","2","3"]
         ["4","2","6","8","5","3","7","9","1"]
         ["7","1","3","9","2","4","8","5","6"]
         ["9","6","1","5","3","7","2","8","4"]
         ["2","8","7","4","1","9","6","3","5"]
         ["3","4","5","2","8","6","1","7","9"]]
Explanation: The input board is shown above and the output is the solved puzzle.

Note:

- The given board contain only digits 1-9 and the character '.'.
- You may assume that the given Sudoku puzzle will have a single unique solution.
- The given board size is always 9x9.

---

We can use a backtracking approach to solve the Sudoku puzzle. We start by iterating through each cell of the board. If we encounter an empty cell, we try all the possible digits that can be placed in that cell. If a digit is valid, we place it in the cell and move on to the next cell. If we reach the end of the board, we have found a solution. If we encounter an invalid digit for a cell, we backtrack and try a different digit for the previous cell.

Here's the Python code that implements this approach:

"""
from typing import List
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        def is_valid(row: int, col: int, num: str) -> bool:
            # Check row
            for i in range(9):
                if board[row][i] == num:
                    return False
            # Check column
            for i in range(9):
                if board[i][col] == num:
                    return False
            # Check sub-box
            sub_box_row = (row // 3) * 3
            sub_box_col = (col // 3) * 3
            for i in range(3):
                for j in range(3):
                    if board[sub_box_row + i][sub_box_col + j] == num:
                        return False
            return True
        def backtrack() -> bool:
            for row in range(9):
                for col in range(9):
                    # If the cell is empty, try filling it with a number from 1 to 9
                    if board[row][col] == ".":
                        for num in map(str, range(1, 10)):
                            # Check whether the number is valid to be placed in the cell
                            if is_valid(row, col, num):
                                # Place the number in the cell
                                board[row][col] = num
                                # Recursively call the function to continue solving the puzzle
                                if backtrack():
                                    return True
                                # If the recursive call fails, remove the number from the cell and try the next number
                                board[row][col] = "."
                        # If all numbers from 1 to 9 fail to solve the puzzle, backtrack
                        return False
            # If all cells in the board are filled, the puzzle is solved
            return True

        # Call the backtrack function to solve the puzzle
        backtrack()
