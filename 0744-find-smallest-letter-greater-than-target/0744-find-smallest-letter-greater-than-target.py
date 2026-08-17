class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        start = 0
        end = len(letters) - 1

        while start < end:
            mid = start + (end - start) // 2

            if ord(letters[mid]) > ord(target):
                end = mid
            else:
                start = mid + 1
        
        if start == len(letters) - 1 and ord(letters[start]) <= ord(target):
            return letters[0]
        
        return letters[start]