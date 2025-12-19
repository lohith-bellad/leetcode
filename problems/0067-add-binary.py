"""
67. Add Binary
Easy

Given two binary strings a and b, return their sum as a binary string.


Example 1:
    Input: a = "11", b = "1"
    Output: "100"

Example 2:
    Input: a = "1010", b = "1011"
    Output: "10101"


Constraints:
    * 1 <= a.length, b.length <= 10^4
    * a and b consist only of '0' or '1' characters.
    * Each string does not contain leading zeros except for the zero itself.

"""


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        p1 = len(a) - 1
        p2 = len(b) - 1
        output = ""

        sum = 0
        carry = 0
        while p1 >= 0 or p2 >= 0:
            b1 = 0
            b2 = 0

            if p1 >= 0:
                b1 = int(a[p1])
                p1 -= 1
            if p2 >= 0:
                b2 = int(b[p2])
                p2 -= 1

            sum = (b1 + b2 + carry) % 2
            carry = (b1 + b2 + carry) // 2

            output += str(sum)

        if carry:
            output += "1"

        return output[::-1]
