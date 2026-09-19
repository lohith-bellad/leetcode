class Solution:
    def alienOrder(self, words: List[str]) -> str:
        """
        def dfs(c, cpath):
            if c in cpath:
                return False

            if c in visited:
                return True

            cpath.add(c)
            for n in adj_map[c]:
                if not dfs(n, cpath):
                    return False

            cpath.remove(c)
            visited.add(c)
            output.append(c)
            return True
            
        adj_map = {}
        all_chars = set()
        output = []
        visited = set()

        for word in words:
            for c in word:
                all_chars.add(c)

        for ch in list(all_chars):
            adj_map[ch] = []

        for i in range(len(words) - 1):
            w1 = words[i]
            w2 = words[i + 1]

            mismatch = False
            for j in range(min(len(w1), len(w2))):
                if w1[j] != w2[j]:
                    adj_map[w2[j]].append(w1[j])
                    mismatch = True
                    break

            if not mismatch:
                if len(w1) > len(w2):
                    return ""

        print(adj_map)
        for ch in list(all_chars):
            if not dfs(ch, set()):
                return ""

        return "".join(output)
        """
        def dfs(c, path):
            if c in path:
                return False

            if c in visited:
                return True

            path.add(c)
            for nxt in adj_mapping[c]:
                if not dfs(nxt, path):
                    return False
            path.remove(c)
            output.append(c)
            visited.add(c)
            return True

        adj_mapping = defaultdict(list)
        all_chars = set()

        for w in words:
            for c in w:
                all_chars.add(c)

        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i + 1]

            mismatch = False
            for j in range(min(len(word1), len(word2))):
                if word1[j] != word2[j]:
                    adj_mapping[word2[j]].append(word1[j])
                    mismatch = True
                    break

            if not mismatch:
                if len(word1) > len(word2):
                    return ""

        output = []
        visited = set()
        for c in all_chars:
            if not dfs(c, set()):
                return ""

        return "".join(output)