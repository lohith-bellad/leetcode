class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPali(s: str, start: int, end: int) -> bool:
            while start < end:
                if s[start] != s[end]:
                    return False
                start += 1
                end -= 1
            return True

        def traverse(s, ind, part, output):
            if ind == len(s):
                output.append(part.copy())
                return
            
            for j in range(ind, len(s)):
                if isPali(s, ind, j):
                    part.append(s[ind : j + 1])
                    traverse(s, j + 1, part, output)
                    part.pop()
        
        output = []
        traverse(s, 0, [], output)
        return output