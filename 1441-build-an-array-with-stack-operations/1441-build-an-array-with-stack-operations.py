class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        output = []
        s = []
        ind = 0

        for i in range(1, n + 1):
            if ind >= len(target):
                break
            if target[ind] == i:
                while s and (ind == 0 or s[-1] != target[ind - 1]):
                    s.pop()
                    output.append("Pop")
                s.append(i)
                output.append("Push")
                ind += 1
            else:
                output.append("Push")
                s.append(i)
        
        return output