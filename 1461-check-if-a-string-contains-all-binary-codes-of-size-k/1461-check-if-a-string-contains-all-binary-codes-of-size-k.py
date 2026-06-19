class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        num_set = set()
        
        for i in range(len(s) - k + 1):
            num = int(s[i:i+k], 2)
            num_set.add(num)
        
        print(num_set)
        for i in range(2**k):
            if i not in num_set:
                return False

        return True