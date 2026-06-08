class RangeModule:
    def __init__(self):
        self.ranges = []

    def addRange(self, left: int, right: int) -> None:
        new_ranges = []
        i, n = 0, len(self.ranges)

        while i < n and self.ranges[i][1] < left:
            new_ranges.append(self.ranges[i])
            i += 1

        while i < n and self.ranges[i][0] <= right:
            left  = min(left, self.ranges[i][0])
            right = max(right, self.ranges[i][1])
            i += 1
        new_ranges.append([left, right])

        while i < n:
            new_ranges.append(self.ranges[i])
            i += 1

        self.ranges = new_ranges

    def queryRange(self, left: int, right: int) -> bool:
        for cur_x, cur_y in self.ranges:
            if cur_x <= left and right <= cur_y:
                return True

        return False

    def removeRange(self, left: int, right: int) -> None:
        new_ranges = []
        for cur_x, cur_y in self.ranges:
            if cur_y <= left or cur_x >= right:
                # No overlap — keep the interval untouched.
                new_ranges.append([cur_x, cur_y])
            else:
                # Overlaps the removed region; keep the surviving remnants.
                if cur_x < left:
                    new_ranges.append([cur_x, left])
                if right < cur_y:
                    new_ranges.append([right, cur_y])

        self.ranges = new_ranges
        return



# Your RangeModule object will be instantiated and called as such:
# obj = RangeModule()
# obj.addRange(left,right)
# param_2 = obj.queryRange(left,right)
# obj.removeRange(left,right)