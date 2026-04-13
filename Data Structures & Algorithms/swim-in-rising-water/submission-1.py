import heapq

class Solution:

    def getCellNeighbors(self, grid, cell):
        i, j = cell
        neighbors = set()
        if i - 1 >= 0:
            neighbors.add((i - 1, j))
        if j - 1 >= 0:
            neighbors.add((i, j - 1))
        if i + 1 < len(grid):
            neighbors.add((i + 1, j))
        if j + 1 < len(grid[i]):
            neighbors.add((i, j + 1))
        return neighbors

    def swimInWater(self, grid: List[List[int]]) -> int:
        # shortest path in graph
        # water limit is the elevation at each taken position based on the number of hops
        start, end = (0, 0), (len(grid) - 1, len(grid[0]) - 1)
        #visited = {start}
        queue = [(0, start)]
        dist = {(i, j): float("inf") for i in range(len(grid)) for j in range(len(grid[i]))}
        prev = {(i, j): None for i in range(len(grid)) for j in range(len(grid[i]))}
        dist[start] = 0
        while queue:
            cellDist, cell = heapq.heappop(queue)
            if cell == end:
                break
            for neighbor in self.getCellNeighbors(grid, cell):
                if dist[neighbor] > max(dist[cell], grid[cell[0]][cell[1]]):
                    dist[neighbor] = max(dist[cell], grid[cell[0]][cell[1]])
                    prev[neighbor] = cell
                    heapq.heappush(queue, (dist[neighbor], neighbor))
        return max(grid[-1][-1], dist[end])