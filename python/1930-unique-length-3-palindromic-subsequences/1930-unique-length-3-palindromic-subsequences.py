class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        left_hash = {}
        right_hash = {}
        output = set()

        if len(s) < 3:
            return 0

        left_hash[s[0]] = 1
        for i in range(1, len(s)):
            if s[i] not in right_hash:
                right_hash[s[i]] = 0
            right_hash[s[i]] += 1
        
        idx = 1
        while idx < len(s) - 1:
            if s[idx] in right_hash:
                right_hash[s[idx]] -= 1
                if right_hash[s[idx]] == 0:
                    del right_hash[s[idx]]

            for l in left_hash.keys():
                if l in right_hash:
                    new_s = l + s[idx] + l
                    output.add(new_s)

            if s[idx] in left_hash:
                left_hash[s[idx]] += 1
            else:
                left_hash[s[idx]] = 1
            
            idx += 1
        
        return len(output)