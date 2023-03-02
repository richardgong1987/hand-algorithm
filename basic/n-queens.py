class NQueens:
    def __init__(self, n):
        self.n = n
        self.board = [-1] * n
        self.solutions = []

    def is_valid(self, row, col):
        for i in range(row):
            if self.board[i] == col or \
                    self.board[i] - i == col - row or \
                    self.board[i] + i == col + row:
                return False
        return True

    def solve(self, row=0):
        if row == self.n:
            self.solutions.append(self.board[:])
            return
        for col in range(self.n):
            if self.is_valid(row, col):
                self.board[row] = col
                self.solve(row + 1)
        self.board[row] = -1

    def print_solutions(self):
        for solution in self.solutions:
            for row in range(self.n):
                line = ""
                for col in range(self.n):
                    if solution[row] == col:
                        line += "Q "
                    else:
                        line += ". "
                print(line)
            print('---------------------')


n = 4
solver = NQueens(n)
solver.solve()
solver.print_solutions()
