class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        years = [0 for i in range(101)]

        for start, end in logs:
            for i in range(start, end):
                years[i - 1950] += 1

        print(years)
        max_pop = max(years)

        for i in range(len(years)):
            if years[i] == max_pop:
                return i + 1950
