class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        def dp(ind, own_stock, transactions):
            if ind == len(prices) - 1:
                if own_stock and transactions > 0:
                    return prices[ind]
                else:
                    return 0
            
            if (ind, own_stock, transactions) in cache:
                return cache[(ind, own_stock, transactions)]
            
            if own_stock:
                if transactions > 0:
                    sell = prices[ind] + dp(ind + 1, False, transactions - 1)
                else:
                    sell = dp(ind + 1, True, transactions)
                
                no_change = dp(ind + 1, True, transactions)

                res = max(sell, no_change)
            else:
                no_change = dp(ind + 1, False, transactions)
                buy = -prices[ind] + dp(ind + 1, True, transactions)

                res= max(buy, no_change)
            
            cache[(ind, own_stock, transactions)] = res
            return res

        cache = {}
        return dp(0, False, 2)