class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # compute reacheable cells from pacific, then atlantic
        # answer is the intesection of them
        n, m = len(heights), len(heights[0])
        reachPacific = set()
        reachAtlantic = set()

        for x in range(n):
            reachPacific.add((x, 0))
            reachAtlantic.add((x, m - 1))
        for y in range(m):
            reachPacific.add((0, y))
            reachAtlantic.add((n - 1, y))

        # bfs multi-source
        def bfs(nodes, visited):
            queue = deque(nodes)
            while queue:
                node = queue.popleft()
                visited.add(node)
                x, y = node[0], node[1]
                for neigh in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                    if neigh in visited or neigh[0] < 0 or neigh[1] < 0 or neigh[0] >= n or neigh[1] >= m:
                        continue 
                    if heights[x][y] <= heights[neigh[0]][neigh[1]]:
                        queue.append(neigh)
        
        visited_pacific, visited_atlantic = set(), set()
        bfs(reachPacific, visited_pacific)
        bfs(reachAtlantic, visited_atlantic)
        
        return list(visited_pacific & visited_atlantic)

    def pacificAtlanticv2(self, heights: List[List[int]]) -> List[List[int]]:
        # for each cell, use dfs to check if can hit both oceans
        n, m = len(heights), len(heights[0])
        visited = set()
        self.reachsPacific = False
        self.reachsAtlantic = False

        def dfs(node):
            visited.add(node)
            x, y = node[0], node[1]
            for neigh in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                if neigh in visited:
                    continue 
                if neigh[0] < 0 or neigh[1] < 0:
                    self.reachsPacific = True
                    continue
                if neigh[0] >= n or neigh[1] >= m:
                    self.reachsAtlantic = True
                    continue
                if heights[x][y] >= heights[neigh[0]][neigh[1]]:
                    dfs(neigh)

        res = set()
        for x in range(n):
            for y in range(m):
                node = (x, y)
                if node in res:
                    continue
                visited = set()
                self.reachsPacific = False
                self.reachsAtlantic = False
                dfs(node)
                if self.reachsPacific and self.reachsAtlantic:
                    res.add(node)
        
        return [list(node) for node in res]
                
                