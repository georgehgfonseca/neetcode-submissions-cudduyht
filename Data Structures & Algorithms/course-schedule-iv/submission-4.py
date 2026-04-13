from collections import deque

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # create a prerequisite graph
        graph = {i: set() for i in range(numCourses)}
        for prereq in prerequisites:
            source = int(prereq[0])
            sink = int(prereq[1])
            graph[source].add(sink)
        
        # we can also precalculate distances, for faster computation when many queries, if dist inf not prerequisit
        # or actually, reuse calcualted distances as needed
        def bfs(node):
            queue = deque()
            queue.append(node)
            distance = [float("inf") for i in range(numCourses)]
            visited = [False for i in range(numCourses)]
            distance[node] = 0
            visited[node] = True
            while queue:
                node = queue.popleft()
                for neighbor in graph[node]:
                    if distance[neighbor] > distance[node] + 1:
                        distance[neighbor] = distance[node] + 1
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        queue.append(neighbor)
            return distance

        ans = []
        distances = dict()
        # for each query search the sink course in this graph
        for query in queries:
            source = int(query[0])
            sink = int(query[1])
            if source in distances:
                # reuse calculatation
                isPrerequisite = distances[source][sink] != float("inf")
                ans.append(isPrerequisite)
            else:
                # run bfs/dfs to se if sink is reachable from source
                distancesFromSource = bfs(source)
                distances[source] = distancesFromSource
                isPrerequisite = distances[source][sink] != float("inf")
                ans.append(isPrerequisite)
        
        return ans


        def dfs(node, target, visited):
            if node == target:
                # is prerequisite
                self.isPrerequisite = True
                return
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    dfs(neighbor, target, visited)
                    visited.remove(neighbor)

        ans = []
        # for each query search the sink course in this graph
        for query in queries:
            # run bfs/dfs to se if sink is reachable from source
            self.isPrerequisite = False
            dfs(query[0], query[1], {query[0]})
            ans.append(self.isPrerequisite)

        

        return ans

