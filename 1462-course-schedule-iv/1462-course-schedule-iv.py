class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        def dfs(course, visited, hash_map, order):
            if course in visited:
                return
            
            visited.add(course)

            if course not in hash_map:
                order.append(course)
                return
            
            for prereqs in hash_map[course]:
                dfs(prereqs, visited, hash_map, order)
            
            order.append(course)
            return

        hash_map = defaultdict(list)

        for prereqs in prerequisites:
            hash_map[prereqs[1]].append(prereqs[0])
        
        visited = set()
        order = []

        for course in range(numCourses):
            temp = []
            dfs(course, visited, hash_map, temp)
            order.append(temp)
        
        output = []
        
        for course_a, course_b in queries:
            for i in range(len(order)):
                if course_b in order[i]:
                    m_ind = i
                    break
            
            ind_b = order[m_ind].index(course_b)
            if course_a in order[m_ind][:ind_b]:
                output.append(True)
            else:
                output.append(False)
        
        return output
