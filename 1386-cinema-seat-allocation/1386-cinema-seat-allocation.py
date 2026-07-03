class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        """
        row_table = defaultdict(set)
        left = {2, 3, 4, 5}
        middle = {4, 5, 6, 7}
        right = {6, 7, 8, 9}

        for row, seat in reservedSeats:
            row_table[row].add(seat)

        count = 0
        for row, seats in row_table.items():
            left_side = not (seats & left)
            middle_side = not (seats & middle)
            right_side = not (seats & right)

            if left_side and right_side:
                count += 2
            elif left_side or middle_side or right_side:
                count += 1
        
        count += (n - len(row_table)) * 2

        return count
        """
        left_side = {2, 3, 4, 5}
        middle = {4, 5, 6, 7}
        right_side = {6, 7, 8, 9}
        rowMap = defaultdict(set)
        count = 0

        for row, seat in reservedSeats:
            rowMap[row].add(seat)

        for _, seats in rowMap.items():
            left = not (left_side & seats)
            right = not (right_side & seats)
            mid = not (middle & seats)

            if left and right:
                count += 2
            elif left or mid or right:
                count += 1
        
        count += (n - len(rowMap)) * 2
        
        return count
                
        
