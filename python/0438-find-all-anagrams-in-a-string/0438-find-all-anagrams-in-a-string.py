class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
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
