class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        """
        table = {}
        output = []

        for i in range(len(s)):
            table[s[i]] = i
        
        end = 0
        while end < len(s):
            start = end
            end = table[s[start]]
            pivot = start + 1

            while end < len(s) and pivot < end:
                if table[s[pivot]] > end:
                    end = table[s[pivot]]
                pivot += 1

            output.append(end - start + 1)
            end += 1

        return output
        """
        hashMap = {}

        for i in range(len(s)):
            if s[i] not in hashMap:
                hashMap[s[i]] = [i]
            elif len(hashMap[s[i]]) == 1:
                hashMap[s[i]].append(i)
            else:
                hashMap[s[i]][1] = i

        windows = []
        for val in hashMap.values():
            if len(val) == 1:
                val.append(val[0])
            windows.append(val)

        windows.sort()
        partition = [windows[0]]

        for i in range(1, len(windows)):
            last_x, last_y = partition[-1]
            x, y = windows[i]

            if x <= last_y:
                partition[-1][1] = max(y, last_y)
            else:
                partition.append([x, y])
        
        output = []
        for part in partition:
            output.append(part[1] - part[0] + 1)
        
        return output