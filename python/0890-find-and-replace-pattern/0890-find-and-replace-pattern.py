class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        wp_table = {}
        pw_table = {}
        output = []

        for word in words:
            if len(word) != len(pattern):
                continue
            wp_table.clear()
            pw_table.clear()

            output.append(word)
            for c1, p1 in zip(word, pattern):
                if c1 not in wp_table and p1 not in pw_table:
                    wp_table[c1] = p1
                    pw_table[p1] = c1

                elif wp_table.get(c1) != p1 or pw_table.get(p1) != c1:
                    output.pop()
                    break

        return output
