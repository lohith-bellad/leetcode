class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """
        table = [[0 for i in range(len(word1) + 1)] for i in range(len(word2) + 1)]

        for i in range(len(word1) + 1):
            table[0][i] = i
        for i in range(len(word2) + 1):
            table[i][0] = i
        
        for i in range(1, len(word2) + 1):
            for j in range(1, len(word1) + 1):
                if word2[i - 1] == word1[j - 1]:
                    table[i][j] = table[i-1][j-1]
                else:
                    table[i][j] = min([table[i-1][j-1], table[i-1][j], table[i][j-1]]) + 1
        
        return table[len(word2)][len(word1)]
        """
        m = len(word1)
        n = len(word2)

        dp = [[0 for i in range(m + 1)] for i in range(n + 1)]

        for i in range(m + 1):
            dp[0][i] = i

        for i in range(n + 1):
            dp[i][0] = i

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if word2[i - 1] == word1[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])

        return dp[n][m]