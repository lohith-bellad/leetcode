class Solution:
    def minDays(self, n: int) -> int:
        """
        def dfs(rem_oranges):
            if rem_oranges <= 1:
                return rem_oranges
            
            if rem_oranges in cache:
                return cache[rem_oranges]

            eat_half = rem_oranges % 2 + dfs(rem_oranges // 2)
            eat_two_third = rem_oranges % 3 + dfs(rem_oranges // 3)
            
            cache[rem_oranges] = min(eat_half, eat_two_third) + 1
            return cache[rem_oranges]

        cache = {}
        return dfs(n)
        """
        queue = deque()
        visited = set()
        queue.append((n, 0))

        while queue:
            rem, level = queue.popleft()

            if rem == 1:
                return level + 1

            if rem in visited:
                continue
            
            visited.add(rem)

            queue.append((rem - 1, level + 1))
            
            if rem % 2 == 0:
                queue.append((rem // 2, level + 1))
            
            if rem % 3 == 0 :
                queue.append((rem // 3, level + 1))
        