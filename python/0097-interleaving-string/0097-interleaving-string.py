class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        def traverse(p1, p2, p3):
            if p3 == len(s3):
                return True

            if (p1, p2) in mapping:
                return mapping[(p1, p2)]

            if p1 < len(s1) and p2 < len(s2) and s1[p1] == s2[p2] and s1[p1] == s3[p3]:
                res = traverse(p1 + 1, p2, p3 + 1) or traverse(p1, p2 + 1, p3 + 1)
            elif p1 < len(s1) and s1[p1] == s3[p3]:
                res = traverse(p1 + 1, p2, p3 + 1)
            elif p2 < len(s2) and s2[p2] == s3[p3]:
                res = traverse(p1, p2 + 1, p3 + 1)
            else:
                res = False

            mapping[(p1, p2)] = res
            return res

        if len(s1) + len(s2) != len(s3):
            return False

        mapping = {}
        return traverse(0, 0, 0)
