class Trie:
    def __init__(self):
        self.branches = [None for i in range(26)]
        self.end = False

    def insert(self, word: str) -> None:
        cur_node = self
        for c in word:
            ind = ord(c) - ord('a')
            if not cur_node.branches[ind]:
                cur_node.branches[ind] = Trie()
            cur_node = cur_node.branches[ind]
        cur_node.end = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def dfs(r, c, cur_word, node):
            ch = board[r][c]
            ind = ord(ch) - ord('a')
            
            if not node.branches[ind]:
                return
    
            node = node.branches[ind]
            cur_word += ch
    
            if node.end:
                output.append(cur_word)
                node.end = False   # avoid duplicates
            
            visited.add((r, c))
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < row_max and 0 <= nc < col_max and (nr, nc) not in visited:
                    dfs(nr, nc, cur_word, node)
            visited.remove((r, c))   # backtrack

        root = Trie()

        for word in words:
            root.insert(word)
        
        row_max = len(board)
        col_max = len(board[0])
        dirs = [[0, -1], [0, 1], [-1, 0], [1, 0]]

        output = []
        visited = set()
        for row in range(row_max):
            for col in range(col_max):
                dfs(row, col, "", root)

        return output