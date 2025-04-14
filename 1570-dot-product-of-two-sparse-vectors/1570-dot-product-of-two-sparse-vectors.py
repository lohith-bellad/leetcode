class SparseVector:
    def __init__(self, nums: []):
        self.nums_map = {}
        for i, val in enumerate(nums):
            if val != 0:
                self.nums_map[i] = val

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, sv: 'SparseVector') -> int:
        res = 0

        for key, val in self.nums_map.items():
            if key in sv.nums_map:
                res += val * sv.nums_map[key]
        
        return res

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)