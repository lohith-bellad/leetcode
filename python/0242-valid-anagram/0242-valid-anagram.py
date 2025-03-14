class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        hash_map_s = {}
        hash_map_t = {}

        for c in s:
            if c not in hash_map_s:
                hash_map_s[c] = 0
            hash_map_s[c] += 1
        
        for c in t:
            if c not in hash_map_t:
                hash_map_t[c] = 0
            hash_map_t[c] += 1
        
        return hash_map_s == hash_map_t



