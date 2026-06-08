class MyCalendar:
    def __init__(self):
        self.bookings = []

    def book(self, start: int, end: int) -> bool:
        for cur_x, cur_y in self.bookings:
            if start < cur_y and cur_x < end:
                return False
        
        self.bookings.append([start, end])
        self.bookings.sort()
        return True
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)