class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        def traverse(s: str, ind: int) -> [""]:
            if ind == len(s):
                return [""]

            perms = traverse(s, ind + 1)
            temp = []
            for perm in perms:
                if s[ind].isalpha():
                    clower = s[ind].lower()
                    cupper = s[ind].upper()
                    temp.append(clower + perm)
                    temp.append(cupper + perm)
                else:
                    temp.append(s[ind] + perm)
            return temp

        return traverse(s, 0)
