class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        hash1 = {}
        hash2 = {}
        set1 = set()
        set2 = set()

        for c in word1:
            set1.add(c)
            if c in hash1:
                hash1[c] += 1
            else:
                hash1[c] = 1

        for c in word2:
            set2.add(c)
            if c in hash2:
                hash2[c] += 1
            else:
                hash2[c] = 1

        count1 = sorted(hash1.values())
        count2 = sorted(hash2.values())

        if set1 == set2 and count1 == count2:
            return True

        return False
