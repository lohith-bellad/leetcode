class SparseVector:
    def __init__(self, nums: List[int]):
        self.indices = {}
        self.nums = nums
        for i, n in enumerate(nums):
            if n > 0:
                self.indices[i] = 1
        

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        res = 0
        for k in self.indices.keys():
            if k in vec.indices:
                res += self.nums[k] * vec.nums[k]
        
        return res

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)