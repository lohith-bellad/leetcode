class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def traverse(nums: List[int], ind: int, cur_subset: [], output: []):
            if ind == len(nums):
                output.append(cur_subset.copy())
                return

            cur_subset.append(nums[ind])
            traverse(nums, ind + 1, cur_subset, output)
            cur_subset.pop()

            traverse(nums, ind + 1, cur_subset, output)
            return

        cur_subset = []
        output = []
        traverse(nums, 0, cur_subset, output)
        return output
