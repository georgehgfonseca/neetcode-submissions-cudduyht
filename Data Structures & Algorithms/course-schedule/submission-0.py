class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # verify if corresponding courses graph is acyclic (DAG)
        # create a prerequisite graph
        # can do bellman-ford, but expensive O(n * m)
        # detect cycle - dfs
        # prerequisites         = [(1, 0), (2, 0), (2, 1)]  true (no cycle)
        # graph                 = {0: {1, 2}, 2: {1}}
        # stack                 = {}
        # visited               = {0, 1, 2}
        graph = {i: set() for i in range(numCourses)}
        for prereq in prerequisites:
            before = prereq[1]
            after = prereq[0]
            graph[before].add(after)

        visited = set()

        print(graph)
        def has_cycle(start):
            stack = [start]
            while stack:
                print(stack)
                node = stack[-1]
                visited.add(node)
                has_unseen_neighbor = False
                for neighbor in graph[node]:
                    if neighbor in stack:
                        return True
                    if neighbor not in visited:
                        stack.append(neighbor)
                        has_unseen_neighbor = True
                        break
                if not has_unseen_neighbor:
                    stack.pop()
            return False
        
        for node in graph:
            if node not in visited and has_cycle(node):
                return False
        return True


        