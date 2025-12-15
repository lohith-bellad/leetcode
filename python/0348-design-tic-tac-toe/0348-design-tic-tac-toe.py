class TicTacToe:
    def __init__(self, n: int):
        self.board = [[0 for i in range(n)] for i in range(n)]
        self.n = n

    def move(self, row: int, col: int, player: int) -> int:
        self.board[row][col] = player

        for i in range(self.n):
            if self.board[row][i] != player:
                break
            if i == self.n - 1:
                return player

        for i in range(self.n):
            if self.board[i][col] != player:
                break
            if i == self.n - 1:
                return player

        for i in range(self.n):
            if self.board[i][i] != player:
                break
            if i == self.n - 1:
                return player

        for i in range(self.n):
            if self.board[i][self.n - 1 - i] != player:
                break
            if i == self.n - 1:
                return player

        return 0


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
