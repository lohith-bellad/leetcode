class Solution:
    def checkIfPrerequisite(
        self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]
    ) -> List[bool]:
        def dfs(course, visited, hash_map):
            if course in visited:
                return

            visited.add(course)

            if course not in hash_map:
                return

            for prereqs in hash_map[course]:
                dfs(prereqs, visited, hash_map)

            return

        hash_map = defaultdict(list)

        for prereqs in prerequisites:
            hash_map[prereqs[1]].append(prereqs[0])

        order = []
        pre_map = {}

        for course in range(numCourses):
            visited = set()
            dfs(course, visited, hash_map)
            pre_map[course] = visited

        output = []
        for prereq, course in queries:
            if prereq in pre_map[course]:
                output.append(True)
            else:
                output.append(False)

        return output
