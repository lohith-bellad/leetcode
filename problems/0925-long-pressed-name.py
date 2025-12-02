"""
925. Long Pressed Name
Easy

Your friend is typing his name into a keyboard. Sometimes, when typing a character c, the
key might get long pressed, and the character will be typed 1 or more times.

You examine the typed characters of the keyboard. Return True if it is possible that it
was your friends name, with some characters (possibly none) being long pressed.


Example 1:
    Input: name = "alex", typed = "aaleex"
    Output: true
    Explanation: 'a' and 'e' in 'alex' were long pressed.

Example 2:
    Input: name = "saeed", typed = "ssaaedd"
    Output: false
    Explanation: 'e' must have been pressed twice, but it wasn't in the typed output.

Example 3:
    Input: name = "leelee", typed = "lleeelee"
    Output: true

Example 4:
    Input: name = "laiden", typed = "laiden"
    Output: true
    Explanation: It's not necessary to long press any character.


Constraints:
    * 1 <= name.length, typed.length <= 1000
    * name and typed consist of only lowercase English letters.

"""


class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        p1 = 1
        p2 = 1

        if name[0] != typed[0]:
            return False

        while p1 < len(name) and p2 < len(typed):
            if name[p1] == typed[p2]:
                p1 += 1
                p2 += 1
            else:
                while p2 < len(typed):
                    if typed[p2] == name[p1 - 1]:
                        p2 += 1
                    elif typed[p2] == name[p1]:
                        break
                    else:
                        return False

        while p2 < len(typed) and typed[p2] == typed[p2 - 1]:
            p2 += 1

        return p1 == len(name) and p2 == len(typed)
