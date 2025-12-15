class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        def dfs(course, visited, path, hash_map, order):
            if course in path:
                return False

            if course in visited:
                return True

            path.append(course)
            visited.add(course)

            if course not in hash_map:
                order.append(course)
                path.pop()
                return True

            for prereqs in hash_map[course]:
                if dfs(prereqs, visited, path, hash_map, order) == False:
                    return False

            order.append(course)
            path.pop()

            return True

        hash_map = defaultdict(list)

        for prereq in prerequisites:
            hash_map[prereq[0]].append(prereq[1])

        order = []
        visited = set()

        for course in range(numCourses):
            if dfs(course, visited, [], hash_map, order) == False:
                return []

        return order
