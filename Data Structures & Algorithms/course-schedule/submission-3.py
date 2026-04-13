class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # detect cycle in undirected graph
        graph = {course: set() for course in range(numCourses)}
        for course, prereq in prerequisites:
            graph[course].add(prereq)

        visited = set()
        self.has_cycle = False

        def dfs(node):
            if node in visited:
                self.has_cycle = True
                return
            
            visited.add(node)
            
            for neighbor in graph[node]:
                dfs(neighbor)
            
            visited.remove(node)

        for node in graph:
            dfs(node)
            if self.has_cycle:
                return False

        return True

        