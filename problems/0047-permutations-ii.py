"""
47. Permutations II
Medium

Given a collection of numbers, nums, that might contain duplicates, return all
possible unique permutations in any order.


Example 1:
    Input: nums = [1,1,2]
    Output: [[1,1,2],[1,2,1],[2,1,1]]

Example 2:
    Input: nums = [1,2,3]
    Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]


Constraints:
    * 1 <= nums.length <= 8
    * -10 <= nums[i] <= 10

"""

from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def compute(ind):
            if ind >= len(nums):
                return [[]]

            perms = compute(ind + 1)
            new_out = []
            hset = set()
            for perm in perms:
                for i in range(len(perm) + 1):
                    new_p = perm.copy()
                    new_p.insert(i, nums[ind])
                    key = ".".join(map(str, new_p))
                    if key not in hset:
                        hset.add(key)
                        new_out.append(new_p)

            return new_out

        return compute(0)
