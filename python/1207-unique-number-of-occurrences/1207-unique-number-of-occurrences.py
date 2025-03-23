class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        hashmap = {}
        temp = []

        for num in arr:
            if num in hashmap:
                hashmap[num] += 1
            else:
                hashmap[num] = 1
            
        for key, value in hashmap.items():
            if value in temp:
                return False
            temp.append(value)
        
        return True