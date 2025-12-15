class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        def traverse(p1: int, p2: int, cache:[]) -> int:
            if p1 >= len(text1) or p2 >= len(text2):
                return 0

            if cache[p1][p2] != -1:
                return cache[p1][p2]

            if text1[p1] == text2[p2]:
                cache[p1][p2] = 1 + traverse(p1 + 1, p2 + 1, cache)

            else:
                cache[p1][p2] = max(traverse(p1 + 1, p2, cache), traverse(p1, p2 + 1, cache))

            return cache[p1][p2]

        cache = [[-1 for i in range(len(text2))] for i in range(len(text1))]
        return traverse(0, 0, cache)
        """

        cache = [[0 for i in range(len(text2) + 1)] for i in range(len(text1) + 1)]

        for i in range(len(text1)):
            for j in range(len(text2)):
                if text1[i] == text2[j]:
                    cache[i + 1][j + 1] = 1 + cache[i][j]
                else:
                    cache[i + 1][j + 1] = max(cache[i][j + 1], cache[i + 1][j])

        return cache[-1][-1]
