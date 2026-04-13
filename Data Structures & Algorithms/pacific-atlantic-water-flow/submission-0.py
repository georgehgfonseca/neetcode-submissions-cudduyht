class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
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
                
                