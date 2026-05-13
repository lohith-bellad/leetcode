class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        count = 0

        start = 0
        end = len(people) - 1

        while start < end:
            if people[end] >= limit:
                end -= 1
            elif people[start] >= limit:
                start += 1
            elif people[start] + people[end] <= limit:
                start += 1
                end -= 1
            else:
                end -= 1
            count += 1

        count += end - start + 1
        return count