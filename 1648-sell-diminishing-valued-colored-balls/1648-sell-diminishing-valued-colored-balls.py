class Solution:
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        inventory.sort(reverse=True)
        inventory.append(0)

        width = 1
        profit = 0

        for i in range(len(inventory) - 1):
            cur_num = inventory[i]
            next_num = inventory[i + 1]

            if cur_num == next_num:
                width += 1
                continue
            
            barHeight = cur_num - next_num
            available = barHeight * width

            if available <= orders:
                profit += width * barHeight * (cur_num + next_num + 1) // 2
                orders -= available
            else:
                q, r = divmod(orders, width)
                profit += r * (cur_num - q)
                profit += width * (cur_num + cur_num - q + 1) * q // 2
                break
            
            width += 1

        return profit % (10**9 + 7)
        
