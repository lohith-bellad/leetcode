"""
408. Valid Word Abbreviation
Easy

A string can be abbreviated by replacing any number of non-adjacent, non-empty substrings
with their lengths. The lengths should not have leading zeros.

For example:
    * "substitution" can be abbreviated as "s10n" ("s ubstitutio n")
    * "substitution" can be abbreviated as "sub4u4" ("sub stit u tion")

The following are NOT valid abbreviations:
    * "s55n" ("s ubsti tutio n", the replaced substrings are adjacent)
    * "s010n" (has leading zeros)
    * "s0ubstitution" (replaces an empty substring)

Given a string word and an abbreviation abbr, return whether the string matches the given
abbreviation.


Example 1:
    Input: word = "internationalization", abbr = "i12iz4n"
    Output: true
    Explanation: "i12iz4n" can be formed by replacing "nternational" (12 characters)
                 and "atio" (4 characters) in "internationalization"

Example 2:
    Input: word = "apple", abbr = "a2e"
    Output: false
    Explanation: "a2e" is not a valid abbreviation of "apple"


Constraints:
    * 1 <= word.length <= 20
    * word consists of only lowercase English letters
    * 1 <= abbr.length <= 10
    * abbr consists of lowercase English letters and digits
    * All the integers in abbr will fit in a 32-bit integer

"""


class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        word_ind = 0
        abbr_ind = 0

        while word_ind < len(word) and abbr_ind < len(abbr):
            skip = 0

            if abbr[abbr_ind] == "0":
                return False

            while abbr_ind < len(abbr) and abbr[abbr_ind].isdigit():
                skip = skip * 10 + int(abbr[abbr_ind])
                abbr_ind += 1

            if skip > 0:
                word_ind += skip
            else:
                if word[word_ind] != abbr[abbr_ind]:
                    return False

                word_ind += 1
                abbr_ind += 1

        return word_ind == len(word) and abbr_ind == len(abbr)
