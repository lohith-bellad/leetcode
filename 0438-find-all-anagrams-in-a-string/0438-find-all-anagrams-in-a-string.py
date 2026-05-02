class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        """
        phash = {}
        psize = 0
        shash = {}
        output = []

        if len(p) > len(s):
            return output
            
        for c in p:
            if c not in phash:
                phash[c] = 0
            phash[c] += 1
            psize += 1
        
        for i in range(psize):
            if s[i] not in shash:
                shash[s[i]] = 0
            shash[s[i]] += 1
        
        if phash == shash:
            output.append(0)
        
        start = 0
        end = psize

        while end < len(s):
            shash[s[start]] -= 1
            if shash[s[start]] == 0:
                del shash[s[start]]
            
            if s[end] not in shash:
                shash[s[end]] = 0
            shash[s[end]] += 1

            start += 1
            end += 1

            if shash == phash:
                output.append(start)
            
        return output
        """
        if len(p) > len(s):
            return []
            
        ptable = {}
        stable = {}
        k = len(p)
        output = []

        for c in p:
            ptable[c] = ptable.get(c, 0) + 1
        
        for i in range(k):
            stable[s[i]] = stable.get(s[i], 0) + 1
        
        if ptable == stable:
            output.append(0)

        for right in range(k, len(s)):
            stable[s[right - k]] -= 1
            if not stable[s[right - k]]:
                del stable[s[right -k]]
            
            stable[s[right]] = stable.get(s[right], 0) + 1

            if ptable == stable:
                output.append(right - k + 1)
        
        return output

