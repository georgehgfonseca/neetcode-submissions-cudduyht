class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {i: set() for i in range(numCourses)}
        for prereq in prerequisites:
            source = prereq[1]
            sink = prereq[0]
            graph[source].add(sink)
        
        visited = set()
        order = []
        self.has_cycle = False

        def dfs(node, stack):
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor in stack:
                    self.has_cycle = True
                    break
                if neighbor not in visited:
                    updatedStack = stack.copy()
                    updatedStack.add(neighbor)
                    dfs(neighbor, updatedStack)
            order.append(node)

        for node in graph:
            if node not in visited:
                dfs(node, {node})
                if self.has_cycle:
                    return []
        
        print(order)
        return order[::-1]


        