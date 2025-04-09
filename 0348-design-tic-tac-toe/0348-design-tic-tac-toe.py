class TicTacToe:

    def __init__(self, n: int):
        self.board = [[-2 for i in range(n)] for i in range(n)]

    def move(self, row: int, col: int, player: int) -> int:
        self.board[row][col] = player

        winner = 0
        for i in range(len(self.board)):
            if sum(self.board[i]) == 6:
                winner = 2
            elif sum(self.board[i]) == 3:
                winner = 1
        
        for i in range(len(self.board)):
            if sum([r[i] for r in self.board]) == 6:
                winner = 2
            elif sum([r[i] for r in self.board]) == 3:
               
                winner = 1
        
        total = 0
        for i in range(len(self.board)):
            total += self.board[i][i]
        
        if total == 6:
            winner = 2
        elif total == 3:
            winner = 1

        total = 0
        n = len(self.board) - 1
        for i in range(len(self.board)):
            total += self.board[i][n - i]
        
        if total == 6:
            winner = 2
        elif total == 3:
            winner = 1
        
        return winner

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)