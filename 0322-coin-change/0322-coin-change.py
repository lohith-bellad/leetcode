class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        def traverse(cur_amt: int):
            if cur_amt in cache:
                return cache[cur_amt]
            
            if cur_amt == 0:
                return 0
            
            cache[cur_amt] = float('inf')
            for coin in coins:
                if cur_amt >= coin:
                    cache[cur_amt] = min(cache[cur_amt], traverse(cur_amt - coin) + 1)
            
            return cache[cur_amt]

        cache = {}
        output = traverse(amount)

        if output == float(inf):
            return -1
        
        return output