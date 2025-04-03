class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        
        rooms = [intervals[0]]

        for i in range(1, len(intervals)):
            s, e = intervals[i]
            found = False
            for i in range(len(rooms)):
                room_start, room_end = rooms[i]
                if room_start < s < room_end:
                    continue
                elif s >= room_end:
                    found = True
                    rooms[i][1] = e
                    break
            if found == False:
                rooms.append([s, e])

        print(rooms)
        return len(rooms)    
            