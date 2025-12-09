"""
17. Letter Combinations of a Phone Number
Medium

Given a string containing digits from 2-9 inclusive, return all possible letter
combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below.
Note that 1 does not map to any letters.

    2: abc
    3: def
    4: ghi
    5: jkl
    6: mno
    7: pqrs
    8: tuv
    9: wxyz


Example 1:
    Input: digits = "23"
    Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Example 2:
    Input: digits = ""
    Output: []

Example 3:
    Input: digits = "2"
    Output: ["a","b","c"]


Constraints:
    * 0 <= digits.length <= 4
    * digits[i] is a digit in the range ['2', '9'].

"""


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        table = {
            2: "abc",
            3: "def",
            4: "ghi",
            5: "jkl",
            6: "mno",
            7: "pqrs",
            8: "tuv",
            9: "wxyz",
        }

        def dfs(ind, cur_word):
            if len(cur_word) == len(digits):
                self.output.append(cur_word)
                return

            cur_letters = table[int(digits[ind])]
            for i in range(len(cur_letters)):
                dfs(ind + 1, cur_word + cur_letters[i])

        if len(digits) == 0:
            return []

        self.output = []
        dfs(0, "")
        return self.output
