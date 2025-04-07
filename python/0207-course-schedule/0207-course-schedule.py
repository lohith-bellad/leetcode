class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def dfs(adj_list, course: int) -> bool:
            if not adj_list[course]:
                return True
            
            if course in self.links:
                return False
            
            self.links.add(course)

            for prereq in adj_list[course]:
                if dfs(adj_list, prereq) == False:
                    return False
            
            adj_list[course] = []
            return True

        
        adj_list = defaultdict(list)
        self.links = set()

        for course, prereq in prerequisites:
            adj_list[course].append(prereq)

        for i in range(numCourses):
            if dfs(adj_list, i) == False:
                return False
            
        return True

            