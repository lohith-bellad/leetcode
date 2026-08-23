class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        """
        meetings.sort(key = lambda x: x[0])

        free_rooms = [i for i in range(n)]
        booked_rooms = []
        room_usage = {}

        for start, end in meetings:
            while booked_rooms and booked_rooms[0][0] <= start:
                _, room_num = heapq.heappop(booked_rooms)
                heapq.heappush(free_rooms, room_num)
            
            if free_rooms:
                cur_room = heapq.heappop(free_rooms)
                heapq.heappush(booked_rooms, (end, cur_room))
            else:
                room_end, cur_room = heapq.heappop(booked_rooms)
                heapq.heappush(booked_rooms, ((end - start) + room_end, cur_room))

            room_usage[cur_room] = room_usage.get(cur_room, 0) + 1
        
        max_room_freq = max(room_usage.values())

        for key in sorted(room_usage.keys()):
            if room_usage[key] == max_room_freq:
                return key
        """
        meetings.sort()
        booked_rooms = []
        free_rooms = [i for i in range(n)]
        heapq.heapify(free_rooms)
        room_usage = {}

        for start, end in meetings:
            while booked_rooms and booked_rooms[0][0] <= start:
                _, room_num = heapq.heappop(booked_rooms)
                heapq.heappush(free_rooms, room_num)

            if free_rooms:
                new_free_room = heapq.heappop(free_rooms)
                heapq.heappush(booked_rooms, (end, new_free_room))
            else:
                next_available_time, new_free_room = heapq.heappop(booked_rooms)
                heapq.heappush(booked_rooms, (next_available_time - start + end, new_free_room))

            room_usage[new_free_room] = room_usage.get(new_free_room, 0) + 1

        max_hosted_room = max(room_usage.values())

        for room in sorted(room_usage.keys()):
            if room_usage[room] == max_hosted_room:
                return room
