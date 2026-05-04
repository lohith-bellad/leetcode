class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left = 0
        max_fruits = 0
        ctable = {}

        for right in range(len(fruits)):
            f = fruits[right]
            ctable[f] = ctable.get(f, 0) + 1

            while len(ctable) > 2:
                ctable[fruits[left]] -= 1
                if not ctable[fruits[left]]:
                    del ctable[fruits[left]]
                left += 1
            
            max_fruits = max(max_fruits, right - left + 1)
        
        return max_fruits