class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set1 = set()
        set2 = set()
        out1 = []
        out2 = []

        for n in nums1:
            set1.add(n)

        for n in nums2:
            set2.add(n)

        for n in set1:
            if n not in set2:
                out1.append(n)

        for n in set2:
            if n not in set1:
                out2.append(n)

        return [out1, out2]
