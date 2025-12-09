"""
46. Permutations
Medium

Given an array nums of distinct integers, return all the possible permutations.
You can return the answer in any order.


Example 1:
    Input: nums = [1,2,3]
    Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Example 2:
    Input: nums = [0,1]
    Output: [[0,1],[1,0]]

Example 3:
    Input: nums = [1]
    Output: [[1]]


Constraints:
    * 1 <= nums.length <= 6
    * -10 <= nums[i] <= 10
    * All the integers of nums are unique

"""

from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(ind):
            if ind >= len(nums):
                return [[]]

            new_out = []
            perms = dfs(ind + 1)
            for perm in perms:
                for i in range(len(perm) + 1):
                    new_perm = perm.copy()
                    new_perm.insert(i, nums[ind])
                    new_out.append(new_perm)

            return new_out

        return dfs(0)
