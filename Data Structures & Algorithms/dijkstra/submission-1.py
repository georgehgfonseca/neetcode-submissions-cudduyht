import heapq

class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        graph = {node: dict() for node in range(n)}
        for (source, sink, weight) in edges:
            graph[source][sink] = weight

        dist = {node: float("inf") for node in graph}
        dist[src] = 0
        queue = [(0, src)]
        while queue:
            (_, node) = heapq.heappop(queue)
            for nei in graph[node]:
                if dist[nei] > dist[node] + graph[node][nei]:
                    dist[nei] = dist[node] + graph[node][nei]
                    heapq.heappush(queue, (dist[nei], nei))

        for node in graph:
            dist[node] = -1 if dist[node] == float("inf") else dist[node]
        return dist

