class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # bfs from each rotten fruit
        # actually, calculate the distance from each fresh friut to any rotten fruit
        # return the smalles distance
        # grid       = [[2, 1, 1],
        #               [0, 1, 1],
        #               [1, 0, 1]]
        # dist       = [[-, -, -],
        #               [-, 0, -],
        #               [-, -, -]]
        dist = [[float("inf") for j in range(len(grid[i]))] for i in range(len(grid))]
        visited = set()

        def get_neighbors(cell):
            (i, j) = cell
            neighbors = set()
            if i - 1 >= 0 and grid[i - 1][j] != 0:
                neighbors.add((i - 1, j))
            if j - 1 >= 0 and grid[i][j - 1] != 0:
                neighbors.add((i, j - 1))
            if i + 1 < len(grid) and grid[i + 1][j] != 0:
                neighbors.add((i + 1, j))
            if j + 1 < len(grid[i]) and grid[i][j + 1] != 0:
                neighbors.add((i, j + 1))
            return neighbors

        def bfs(cell):
            queue = deque([cell])
            visited.add(cell)
            while queue:
                curr = queue.popleft()
                neighbors = get_neighbors(curr)
                for neighbor in neighbors:
                    if dist[neighbor[0]][neighbor[1]] > dist[curr[0]][curr[1]] + 1:
                        dist[neighbor[0]][neighbor[1]] = dist[curr[0]][curr[1]] + 1
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 2:
                    # calculate distances from rotten fruit at (i, j)
                    dist[i][j] = 0
                    bfs((i, j))
        
        # get the largest distance
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] != 0 and grid[i][j] != 2:
                    if dist[i][j] == float("inf"):
                        # this cell has not been reached
                        return -1
                    ans = max(ans, dist[i][j])
        return ans
        
        