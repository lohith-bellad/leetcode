"""
394. Decode String
Medium

Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the
square brackets is being repeated exactly k times. Note that k is guaranteed to
be a positive integer.

You may assume that the input string is always valid; there are no extra white
spaces, square brackets are well-formed, etc. Furthermore, you may assume that
the original data does not contain any digits and that digits are only for
those repeat numbers, k. For example, there will not be input like 3a or 2[4].

The test cases are generated so that the length of the output will never exceed
10^5.


Example 1:
    Input: s = "3[a]2[bc]"
    Output: "aaabcbc"

Example 2:
    Input: s = "3[a2[c]]"
    Output: "accaccacc"

Example 3:
    Input: s = "2[abc]3[cd]ef"
    Output: "abcabccdcdcdef"


Constraints:
    * 1 <= s.length <= 30
    * s consists of lowercase English letters, digits, and square brackets '[]'.
    * s is guaranteed to be a valid input.
    * All the integers in s are in the range [1, 300].

"""


class Solution:
    def decodeString(self, s: str) -> str:
        num_stack = []
        word_stack = []

        i = 0
        while i < len(s):
            num = 0
            while i < len(s) and s[i].isdigit():
                num = (num * 10) + int(s[i])
                i += 1

            if num > 0:
                num_stack.append(num)
                continue

            if s[i] == "[" or s[i].isalpha():
                word_stack.append(s[i])

            elif s[i] == "]":
                cur_word = ""

                while word_stack and word_stack[-1] != "[":
                    cur_word += word_stack.pop()[::-1]

                # pop "["
                word_stack.pop()
                count = num_stack.pop()

                cur_word = cur_word[::-1]
                new_word = cur_word * count

                word_stack.append(new_word)

            i += 1

        return "".join(word_stack)
