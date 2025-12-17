"""
946. Validate Stack Sequences
Medium

Given two integer arrays pushed and popped each with distinct values, return
true if this could have been the result of a sequence of push and pop operations
on an initially empty stack, or false otherwise.


Example 1:
    Input: pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
    Output: true
    Explanation: We might do the following sequence:
        push(1), push(2), push(3), push(4),
        pop() -> 4,
        push(5),
        pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1

Example 2:
    Input: pushed = [1,2,3,4,5], popped = [4,3,5,1,2]
    Output: false
    Explanation: 1 cannot be popped before 2.


Constraints:
    * 1 <= pushed.length <= 1000
    * 0 <= pushed[i] <= 1000
    * All the elements of pushed are unique.
    * popped.length == pushed.length
    * popped is a permutation of pushed.

"""

from typing import List


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        my_stack = []
        i = 0
        j = 0

        while (i < len(pushed) or my_stack) and j < len(popped):
            if i < len(pushed):
                if pushed[i] != popped[j]:
                    if my_stack and my_stack[-1] == popped[j]:
                        my_stack.pop()
                        j += 1
                    else:
                        my_stack.append(pushed[i])
                        i += 1
                else:
                    i += 1
                    j += 1
            else:
                if my_stack and popped[j] != my_stack.pop():
                    return False
                j += 1

        if not my_stack and i == len(pushed) and j == len(popped):
            return True

        return False
