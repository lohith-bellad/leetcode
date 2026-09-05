class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        def dfs(ind: int) -> bool:
            if ind in cache:
                return cache[ind]

            for i in range(1, len(s) - ind + 1):
                if s[ind: ind + i] in wordDict:
                    if dfs(ind + i):
                        cache[ind] = True
                        return True

            cache[ind] = False
            return False

        cache = {len(s): True}
        return dfs(0)
        """
        words = set(wordDict)

        def dfs(ind):
            if ind == len(s):
                return True

            if ind in cache:
                return cache[ind]
            
            for offset in range(1, len(s) - ind + 1):
                if s[ind : ind + offset] in words:
                    if dfs(ind + offset):
                        cache[ind] = True
                        return True

            cache[ind] = False
            return False

        cache = {}
        return dfs(0)