class Solution:
    def minAvailableDuration(
        self, slots1: List[List[int]], slots2: List[List[int]], duration: int
    ) -> List[int]:
        output = []
        p1 = 0
        p2 = 0
        slots1.sort(key=lambda x: x[0])
        slots2.sort(key=lambda x: x[0])

        while p1 < len(slots1) and p2 < len(slots2):
            new_x = max(slots1[p1][0], slots2[p2][0])
            new_y = min(slots1[p1][1], slots2[p2][1])

            if new_x <= new_y:
                if (new_y - new_x) >= duration:
                    return [new_x, new_x + duration]

            if new_y < slots2[p2][1]:
                p1 += 1
            else:
                p2 += 1

        return []
