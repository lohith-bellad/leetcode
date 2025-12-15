class Solution:
    def validPalindrome(self, s: str) -> bool:
        def traverse(s, start, end, skip) -> bool:
            if start > end:
                return True

            if s[start] == s[end]:
                return traverse(s, start + 1, end - 1, skip)
            else:
                if skip:
                    return traverse(s, start + 1, end, 0) or traverse(
                        s, start, end - 1, 0
                    )
                else:
                    return False

        return traverse(s, 0, len(s) - 1, 1)
