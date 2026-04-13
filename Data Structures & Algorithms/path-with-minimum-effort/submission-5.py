import heapq

class Solution:


    def get_neighbor_cells(self, i, j, heights):
        neighbors = dict()
        if i - 1 >= 0:
            neighbors[(i - 1, j)] = abs(heights[i][j] - heights[i - 1][j])**10
        if j - 1 >= 0:
            neighbors[(i, j - 1)] = abs(heights[i][j] - heights[i][j - 1])**10
        if i + 1 < len(heights):
            neighbors[(i + 1, j)] = abs(heights[i][j] - heights[i + 1][j])**10
        if j + 1 < len(heights[i]):
            neighbors[(i, j + 1)] = abs(heights[i][j] - heights[i][j + 1])**10
        return neighbors
    
    def dijkstra(self, graph, start, end):
        dist = {node: float("inf") for node in graph}
        prev = {node: None for node in graph}
        # optmize with heapq
        queue = [(0, start)]
        dist[start] = 0
        while queue:
            (_, node) = heapq.heappop(queue)
            for neighbor in graph[node]:
                if dist[neighbor] > dist[node] + graph[node][neighbor]:
                    dist[neighbor] = dist[node] + graph[node][neighbor]
                    prev[neighbor] = node
                    heapq.heappush(queue, (dist[neighbor], neighbor))
        return dist, prev

    def get_most_expensive_edge(self, graph, dist, prev, start, end):
        path = [end]
        edge_costs = [0] # dummy cost for empty edges
        curr = end
        while curr != start:
            if not prev:
                break
            edge_costs.append(graph[prev[curr]][curr]**(1/10))
            curr = prev[curr]
            path.append(curr)

        return int(max(edge_costs))


    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        # create a graph of cells and effort to neighboring cells
        graph = dict()
        for i in range(len(heights)):
            for j in range(len(heights[i])):
                graph[(i, j)] = self.get_neighbor_cells(i, j, heights)
        
        # compute dijkstra's for shortest path
        start, end = (0, 0), (len(heights) - 1, len(heights[0]) - 1)
        dist, prev = self.dijkstra(graph, start, end)
        # get the most expensive edge in the path
        return self.get_most_expensive_edge(graph, dist, prev, start, end)

