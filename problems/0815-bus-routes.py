"""
815. Bus Routes
Hard

You are given an array routes representing bus routes where routes[i] is a bus
route that the ith bus repeats forever.

For example, if routes[0] = [1, 5, 7], this means that the 0th bus travels in
the sequence 1 -> 5 -> 7 -> 1 -> 5 -> 7 -> 1 -> ... forever.

You will start at the bus stop source and want to go to the bus stop target.
You can travel between bus stops by buses only.

Return the least number of buses you must take to travel from source to target.
Return -1 if it is not possible.


Example 1:
    Input: routes = [[1,2,7],[3,6,7]], source = 1, target = 3
    Output: 2
    Explanation: The best strategy is take the first bus to the bus stop 7, then take the second bus to the bus stop 3.

Example 2:
    Input: routes = [[7,12],[4,5,15],[6],[15,19,26,7]], source = 15, target = 26
    Output: -1


Constraints:
    * 1 <= routes.length <= 500.
    * 1 <= routes[i].length <= 10^5
    * All the values of routes[i] are unique.
    * sum(routes[i].length) <= 10^5
    * 0 <= routes[i][j] < 10^6
    * 0 <= source, target < 10^6

"""

from typing import List
from collections import deque, defaultdict


class Solution:
    def numBusesToDestination(
        self, routes: List[List[int]], source: int, target: int
    ) -> int:
        if source == target:
            return 0

        stops_to_buses = defaultdict(list)
        queue = deque()
        visited = set()

        for i, bus in enumerate(routes):
            for stop in bus:
                stops_to_buses[stop].append(i)

        if source not in stops_to_buses or target not in stops_to_buses:
            return -1

        for bus in stops_to_buses[source]:
            queue.append((bus, 1))
            visited.add(bus)

        while queue:
            cur_bus, buses_taken = queue.popleft()

            if target in routes[cur_bus]:
                return buses_taken

            for stop in routes[cur_bus]:
                for next_bus in stops_to_buses[stop]:
                    if next_bus not in visited:
                        queue.append((next_bus, buses_taken + 1))
                        visited.add(next_bus)

        return -1
