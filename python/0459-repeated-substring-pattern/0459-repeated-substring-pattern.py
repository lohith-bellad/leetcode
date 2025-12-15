class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        new_string = s + s
        new_string = new_string[1 : len(new_string) - 1]
        if s in new_string:
            return True
        else:
            return False
