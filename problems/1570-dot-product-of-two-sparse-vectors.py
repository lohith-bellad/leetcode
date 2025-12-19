"""
1570. Dot Product of Two Sparse Vectors
Medium

Given two sparse vectors, compute their dot product.

Implement class SparseVector:
    * SparseVector(nums) Initializes the object with the vector nums
    * dotProduct(vec) Compute the dot product between the instance of
      SparseVector and vec

A sparse vector is a vector that has mostly zero values, you should store the
sparse vector efficiently and compute the dot product between two SparseVector.

Follow up: What if only one of the vectors is sparse?


Example 1:
    Input: nums1 = [1,0,0,2,3], nums2 = [0,3,0,4,0]
    Output: 8
    Explanation: v1 = SparseVector(nums1), v2 = SparseVector(nums2)
        v1.dotProduct(v2) = 1*0 + 0*3 + 0*0 + 2*4 + 3*0 = 8

Example 2:
    Input: nums1 = [0,1,0,0,0], nums2 = [0,0,0,0,2]
    Output: 0
    Explanation: v1 = SparseVector(nums1), v2 = SparseVector(nums2)
        v1.dotProduct(v2) = 0*0 + 1*0 + 0*0 + 0*0 + 0*2 = 0

Example 3:
    Input: nums1 = [0,1,0,0,2,0,0], nums2 = [1,0,0,0,3,0,4]
    Output: 6


Constraints:
    * n == nums1.length == nums2.length
    * 1 <= n <= 10^5
    * 0 <= nums1[i], nums2[i] <= 100

"""

from typing import List


def binary_search(nums, key):
    start = 0
    end = len(nums) - 1

    while start <= end:
        mid = start + (end - start) // 2

        if nums[mid][0] == key:
            return mid

        if nums[mid][0] > key:
            end = mid - 1
        else:
            start = mid + 1

    return -1


class SparseVector:
    def __init__(self, nums: List[int]):
        self.indices = []

        for i in range(len(nums)):
            if nums[i]:
                self.indices.append((i, nums[i]))

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: "SparseVector") -> int:
        indices1 = self.indices
        indices2 = vec.indices
        product = 0

        if len(indices1) > len(indices2):
            indices1, indices2 = indices2, indices1

        # indices1 will be shorter one
        for i, val in indices1:
            sec_ind = binary_search(indices2, i)
            if sec_ind > -1:
                product += val * indices2[sec_ind][1]

        return product


# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)
