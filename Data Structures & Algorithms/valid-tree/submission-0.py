class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # make a valid tree - has not cycle & connected
        if n - 1 != len(edges):
            return False

        graph = {node: set() for node in range(n)}
        for (source, sink) in edges:
            graph[source].add(sink)
            graph[sink].add(source)

        visited = set()
        self.has_cycle = False

        def dfs(node, parent):
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor != parent and neighbor in visited:
                    self.has_cycle = True
                    return
                if neighbor not in visited:
                    dfs(neighbor, node)
        
        dfs(0, None)
        return not self.has_cycle and len(visited) == n
        