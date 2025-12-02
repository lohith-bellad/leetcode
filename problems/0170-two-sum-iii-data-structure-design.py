"""
170. Two Sum III - Data structure design
Easy

Design a data structure that accepts a stream of integers and checks if it has a pair of
integers that sum up to a particular value.

Implement the TwoSum class:

    * TwoSum() Initializes the TwoSum object, with an empty array initially.
    * void add(int number) Adds number to the data structure.
    * boolean find(int value) Returns true if there exists any pair of numbers whose sum is
      equal to value, otherwise, it returns false.


Example 1:
    Input:
        ["TwoSum", "add", "add", "add", "find", "find"]
        [[], [1], [3], [5], [4], [7]]
    Output:
        [null, null, null, null, true, false]

    Explanation:
        TwoSum twoSum = new TwoSum();
        twoSum.add(1);   // [] --> [1]
        twoSum.add(3);   // [1] --> [1,3]
        twoSum.add(5);   // [1,3] --> [1,3,5]
        twoSum.find(4);  // 1 + 3 = 4, return true
        twoSum.find(7);  // No two integers sum up to 7, return false

Example 2:
    Input:
        ["TwoSum", "add", "add", "add", "find", "find"]
        [[], [3], [1], [2], [3], [6]]
    Output:
        [null, null, null, null, true, false]

    Explanation:
        TwoSum twoSum = new TwoSum();
        twoSum.add(3);   // [] --> [3]
        twoSum.add(1);   // [3] --> [3,1]
        twoSum.add(2);   // [3,1] --> [3,1,2]
        twoSum.find(3);  // 1 + 2 = 3, return true
        twoSum.find(6);  // No two integers sum up to 6, return false


Constraints:
    * -10^5 <= number <= 10^5
    * -2^31 <= value <= 2^31 - 1
    * At most 10^4 calls will be made to add and find.

"""


class TwoSum:
    def __init__(self):
        self.nums = []

    def add(self, number: int) -> None:
        self.nums.append(number)
        self.nums.sort()

    def find(self, value: int) -> bool:
        start = 0
        end = len(self.nums) - 1

        while start < end:
            if self.nums[start] + self.nums[end] == value:
                return True

            if self.nums[start] + self.nums[end] > value:
                end -= 1
            else:
                start += 1

        return False


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)
