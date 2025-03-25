class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False

        maga_table = {}

        for m in magazine:
            maga_table[m] = maga_table.get(m, 0) + 1
        
        for r in ransomNote:
            if r not in maga_table:
                return False
            maga_table[r] -= 1
            if maga_table[r] == 0:
                del maga_table[r]
        
        return True