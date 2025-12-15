class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_map = {}
        s2_map = {}

        for c in s1:
            s1_map[c] = s1_map.get(c, 0) + 1

        for i in range(len(s1)):
            s2_map[s2[i]] = s2_map.get(s2[i], 0) + 1

        if s2_map == s1_map:
            return True

        start = 0
        end = len(s1)

        while end < len(s2):
            s2_map[s2[start]] -= 1
            if s2_map[s2[start]] == 0:
                del s2_map[s2[start]]

            s2_map[s2[end]] = s2_map.get(s2[end], 0) + 1

            if s2_map == s1_map:
                return True

            end += 1
            start += 1

        return False
