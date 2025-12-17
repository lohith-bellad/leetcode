"""
384. Shuffle an Array
Medium

Given an integer array nums, design an algorithm to randomly shuffle the array.
All permutations of the array should be equally likely as a result of the
shuffling.

Implement the Solution class:
    * Solution(int[] nums) Initializes the object with the integer array nums.
    * int[] reset() Resets the array to its original configuration and returns it.
    * int[] shuffle() Returns a random shuffling of the array.


Example 1:
    Input:
        ["Solution", "shuffle", "reset", "shuffle"]
        [[[1, 2, 3]], [], [], []]
    Output:
        [null, [3, 1, 2], [1, 2, 3], [1, 3, 2]]
    Explanation:
        Solution solution = new Solution([1, 2, 3]);
        solution.shuffle();    // Shuffle the array [1,2,3] and return its result.
                               // Any permutation of [1,2,3] must be equally likely
                               // to be returned. Example: return [3, 1, 2]
        solution.reset();      // Resets the array back to its original configuration
                               // [1,2,3]. Return [1, 2, 3]
        solution.shuffle();    // Returns the random shuffling of array [1,2,3].
                               // Example: return [1, 3, 2]


Constraints:
    * 1 <= nums.length <= 50
    * -10^6 <= nums[i] <= 10^6
    * All the elements of nums are unique.
    * At most 10^4 calls in total will be made to reset and shuffle.

"""

from typing import List


class Solution:
    def __init__(self, nums: List[int]):
        self.nums = nums

    def reset(self) -> List[int]:
        return self.nums

    def shuffle(self) -> List[int]:
        output = [self.nums[i] for i in range(len(self.nums))]

        for i in range(len(output)):
            rand_ind = random.randint(i, len(output) - 1)
            output[rand_ind], output[i] = output[i], output[rand_ind]

        return output


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
