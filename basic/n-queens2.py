

def solve_n_queens(n):
    def is_valid(board, row, col):
        # check row and column
        for i in range(n):
            if board[row][i] == 1 or board[i][col] == 1:
                return False
        # check diagonals
        for i in range(n):
            for j in range(n):
                if (i + j == row + col) or (i - j == row - col):
                    if board[i][j] == 1:
                        return False
        return True

    def backtrack(board, row):
        if row == n:
            # found a solution
            solutions.append([row[:] for row in board])
            return
        for col in range(n):
            if is_valid(board, row, col):
                board[row][col] = 1
                backtrack(board, row + 1)
                board[row][col] = 0

    solutions = []
    board = [[0] * n for i in range(n)]
    backtrack(board, 0)
    return solutions


print(solve_n_queens(4))
