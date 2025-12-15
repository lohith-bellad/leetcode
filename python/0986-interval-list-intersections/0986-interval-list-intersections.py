class Solution:
    def intervalIntersection(
        self, firstList: List[List[int]], secondList: List[List[int]]
    ) -> List[List[int]]:
        i = 0
        j = 0
        output = []
        m = len(firstList)
        n = len(secondList)

        while i < m and j < n:
            x = max(firstList[i][0], secondList[j][0])
            y = min(firstList[i][1], secondList[j][1])

            if x <= y:
                output.append([x, y])

            if y < secondList[j][1]:
                i += 1
            else:
                j += 1

        return output
