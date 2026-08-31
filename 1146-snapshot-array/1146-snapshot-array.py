class SnapshotArray:

    def __init__(self, length: int):
        self.snaps = [[(-1, 0)] for i in range(length)]
        self.snap_id = 0

    def set(self, index: int, val: int) -> None:
        cur_record = self.snaps[index]

        if cur_record[-1][0] == self.snap_id:
            cur_record[-1] = (self.snap_id, val)
        else:
            cur_record.append((self.snap_id, val))

    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        cur_record = self.snaps[index]

        start = 0
        end = len(cur_record) - 1

        while start < end:
            mid = start + (end - start + 1) // 2
            
            if cur_record[mid][0] <= snap_id:
                start = mid
            else:
                end = mid - 1
        
        return cur_record[start][1]

# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)
