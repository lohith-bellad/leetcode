class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        start = 0
        output = 0

        for m_start, m_end in meetings:
            if start < m_start:
                output += m_start - start - 1
                start = m_end
            else:
                start = max(start, m_end)

        if start < days:
            output += (days - start)
        
        return output