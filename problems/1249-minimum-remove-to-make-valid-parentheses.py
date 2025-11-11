"""
LeetCode 1249: Minimum Remove to Make Valid Parentheses

Given a string s of '(' , ')' and lowercase English characters.
Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions )
so that the resulting parentheses string is valid and return any valid string.

A valid parentheses string is defined as:
- An empty string or a string containing only lowercase characters
- A concatenation of two valid strings (AB where A and B are valid strings)
- A valid string wrapped in parentheses: (A)

Examples:

Example 1:
    Input: s = "lee(t(c)o)de)"
    Output: "lee(t(c)o)de"
    Explanation: "lee(t(co)de)" would also be accepted.

Example 2:
    Input: s = "a)b(c)d"
    Output: "ab(c)d"

Example 3:
    Input: s = "))(("
    Output: ""
    Explanation: An empty string is also valid.

Example 4:
    Input: s = "(a(b(c)d)"
    Output: "a(b(c)d)"

Constraints:
    - 1 <= s.length <= 10^5
    - s[i] is either '(' , ')', or lowercase English letter
"""


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        output = []
        pstack = []
        ind = 0

        for c in s:
            if c == "(":
                output.append(c)
                pstack.append(ind)
                ind += 1
            elif c == ")":
                if pstack:
                    pstack.pop()
                    output.append(c)
                    ind += 1
            else:
                output.append(c)
                ind += 1

        while pstack:
            output[pstack.pop()] = ""

        return "".join(output)
