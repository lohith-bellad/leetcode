"""
383. Ransom Note
Easy

Given two strings ransomNote and magazine, return true if ransomNote can be constructed
by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.


Example 1:
    Input: ransomNote = "a", magazine = "b"
    Output: false

Example 2:
    Input: ransomNote = "aa", magazine = "ab"
    Output: false

Example 3:
    Input: ransomNote = "aa", magazine = "aab"
    Output: true


Constraints:
    * 1 <= ransomNote.length, magazine.length <= 10^5
    * ransomNote and magazine consist of lowercase English letters.

"""


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        rTable = {}
        mTable = {}

        for c in ransomNote:
            rTable[c] = rTable.get(c, 0) + 1

        for c in magazine:
            mTable[c] = mTable.get(c, 0) + 1

        for key, value in rTable.items():
            if mTable.get(key, 0) < value:
                return False

        return True
