class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        """
        def dfs(ind: int, sentence: str):
            if ind >= len(s):
                self.output.append(" ".join(sentence.copy()))
                return
            
            for i in range(len(s) - ind):
                search_word = s[ind: ind + i + 1]
                if search_word in wordDict:
                    sentence.append(search_word)
                    dfs(ind + i + 1, sentence)
                    sentence.pop()
            return

        self.output = []
        dfs(0, [])

        return self.output
        """
        words = set(wordDict)
        output = []

        def dfs(ind, path):
            if ind == len(s):
                output.append(" ".join(path))
                return

            for offset in range(1, len(s) - ind + 1):
                cur_word = s[ind: ind + offset]
                if cur_word in words:
                    path.append(cur_word)
                    dfs(ind + offset, path)
                    path.pop()

            return

        dfs(0, [])
        return output