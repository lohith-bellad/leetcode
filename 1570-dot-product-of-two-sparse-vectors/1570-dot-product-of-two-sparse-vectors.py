class SparseVector:
    def __init__(self, nums: List[int]):
        self.indices = []
        self.nums = nums
        for i, n in enumerate(nums):
            if n > 0:
                self.indices.append(i)
        

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        res = 0
        ind = list(set(self.indices) & set(vec.indices))
        for i in ind:
            res += self.nums[i] * vec.nums[i]
        
        return res

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)