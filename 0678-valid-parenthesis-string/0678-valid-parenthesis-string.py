class Solution:
    def checkValidString(self, s: str) -> bool:
        """
        def traverse(ind: int, waiting: int) -> bool:
            if ind == len(s):
                return waiting == 0
            
            if waiting < 0:
                return False

            if (ind, waiting) in cache:
                return cache[(ind, waiting)]

            if s[ind] == "(":
                res = traverse(ind + 1, waiting + 1)
            elif s[ind] == ")":
                res = traverse(ind + 1, waiting - 1)
            else:
                res = (traverse(ind + 1, waiting + 1) or 
                        traverse(ind + 1, waiting) or 
                        traverse(ind + 1, waiting - 1))

            cache[(ind, waiting)] = res
            return res
        
        cache = {}
        res = traverse(0, 0)
        return res
        
        def dfs(ind, balance):
            if balance < 0:
                return False

            if ind >= len(s):
                return balance == 0

            if (ind, balance) in cache:
                return cache[(ind, balance)]

            if s[ind] == "(":
                cache[(ind, balance)] = dfs(ind + 1, balance + 1)

            if s[ind] == ")":
                cache[(ind, balance)] = dfs(ind + 1, balance - 1)

            if s[ind] == "*":
                consider_open = dfs(ind + 1, balance + 1)
                consider_close = dfs(ind + 1, balance - 1)
                consider_star = dfs(ind + 1, balance)

                cache[(ind, balance)] = consider_open or consider_close or consider_star

            return cache[(ind, balance)]

        cache = {}
        return dfs(0, 0)
        """
        def dfs(ind, opened, closed):
            if ind >= len(s):
                if opened == closed:
                    return True
                return False
            
            if closed > opened:
                return False
            
            if (ind, opened, closed) in cache:
                return cache[(ind, opened, closed)]
            
            if s[ind] == "(":
                cache[(ind, opened, closed)] = dfs(ind + 1, opened + 1, closed)
            
            if s[ind] == ")":
                cache[(ind, opened, closed)] = dfs(ind + 1, opened, closed + 1)
            
            if s[ind] == "*":
                cache[(ind, opened, closed)] = (dfs(ind + 1, opened + 1, closed) or
                        dfs(ind + 1, opened, closed + 1) or
                        dfs(ind + 1, opened, closed))
            
            return cache[(ind, opened, closed)]
        
        cache = {}
        return dfs(0, 0, 0)

        

