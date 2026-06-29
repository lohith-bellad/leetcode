class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def traverse(ind, cur_set, output):
            if ind >= len(nums):
                output.append(cur_set.copy())
                return
            
            cur_set.append(nums[ind])
            traverse(ind + 1, cur_set, output)
            cur_set.pop()

            traverse(ind + 1, cur_set, output)
            return

        output = []
        traverse(0, [], output)
        
        return output