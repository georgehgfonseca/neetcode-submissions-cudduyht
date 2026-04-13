from collections import defaultdict

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # graph edge means the multiple to get sink from source eg. a / b = 0.5 b --- 0.5 --> a
        graph = defaultdict(dict)
        for i, (a, b) in enumerate(equations):
            graph[b][a] = values[i]
            graph[a][b] = 1 / values[i]
        

        def dfs(node, target):
            self.currPath.append(node)
            self.visited.add(node)
            if node == target:
                self.pathBA = self.currPath.copy()
                return
            for neighbor in graph[node]:
                if neighbor not in self.visited:
                    dfs(neighbor, target)
            self.currPath.pop()

        # for each query find a path in the graph and perform the multiplations
        res = []
        for a, b in queries:
            # find a path from b to a
            self.visited = set()
            self.currPath = []
            self.pathBA = []
            dfs(b, a)
            if b not in graph or a not in graph:
                res.append(-1)
                continue
            if b == a:
                res.append(1)
                continue
            if len(self.pathBA) < 2:
                res.append(-1)
                continue
            
            queryAns = graph[self.pathBA[0]][self.pathBA[1]]
            for i in range(2, len(self.pathBA)):
                queryAns *= graph[self.pathBA[i - 1]][self.pathBA[i]]
            res.append(queryAns)
        return res
