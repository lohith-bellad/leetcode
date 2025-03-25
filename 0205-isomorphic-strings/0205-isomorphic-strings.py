class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_t_table = {}
        t_s_table = {}

        for s1, t1 in zip(s, t):
            if s1 not in s_t_table and t1 not in t_s_table:
                s_t_table[s1] = t1
                t_s_table[t1] = s1
            elif s_t_table.get(s1) != t1 or t_s_table.get(t1) != s1:
                return False
        
        return True
