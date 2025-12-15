class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s_list = s.split(" ")
        if len(s_list) != len(pattern):
            return False

        ps_table = {}
        sp_table = {}

        for c, word in zip(pattern, s_list):
            if (c not in ps_table) and (word not in sp_table):
                ps_table[c] = word
                sp_table[word] = c

            elif (ps_table.get(c) != word) or (sp_table.get(word) != c):
                print(ps_table.get(c))
                return False

        return True
