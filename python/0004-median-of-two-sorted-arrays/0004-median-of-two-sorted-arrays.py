class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        len1 = len(nums1)
        len2 = len(nums2)
        self.p1 = 0
        self.p2 = 0

        def get_min() -> int:
            if self.p1 < len1 and self.p2 < len2:
                if nums1[self.p1] < nums2[self.p2]:
                    out = nums1[self.p1]
                    self.p1 += 1
                else:
                    out = nums2[self.p2]
                    self.p2 += 1
            elif self.p1 < len1:
                out = nums1[self.p1]
                self.p1 += 1
            else:
                out = nums2[self.p2]
                self.p2 += 1

            return out

        if (len1 + len2) % 2 == 0:
            for i in range((len1 + len2) // 2 - 1):
                v = get_min()
            out = (get_min() + get_min()) / 2
        else:
            for i in range((len1 + len2) // 2):
                v = get_min()
            out = get_min()

        return out
