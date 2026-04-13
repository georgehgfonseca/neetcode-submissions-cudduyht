from collections import defaultdict, deque

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # bfs on each node and count the height
        graph = {i: set() for i in range(n)}
        for source, sink in edges:
            graph[source].add(sink)
            graph[sink].add(source)
        

        def bfs(start) -> int:
            depth = [-1 for _ in graph]
            queue = deque([start])
            depth[start] = 0
            while queue:
                node = queue.popleft()
                for neighbor in graph[node]:
                    if depth[neighbor] == -1:
                        queue.append(neighbor)
                        depth[neighbor] = depth[node] + 1
            return max(depth)

        minHeight = float("inf")
        minHeightNodes = []
        for node in graph:
            # run bfs
            nodeHeight = bfs(node)
            if nodeHeight < minHeight:
                minHeight = nodeHeight
                minHeightNodes = [node]
            elif nodeHeight == minHeight:
                minHeightNodes.append(node)

        return minHeightNodes
        