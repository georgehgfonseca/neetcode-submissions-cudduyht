class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # create a graph to store connection information
        graph = {(i, j): set() for i in range(len(grid)) for j in range(len(grid[i]))}

        def addEdge(graph, node1, node2):
            graph[node1].add(node2)
            graph[node2].add(node1)

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == -1:
                    continue
                if j < len(grid[i]) - 1 and grid[i][j + 1] != -1:
                    addEdge(graph, (i, j), (i, j + 1))
                if j - 1 >= 0 and grid[i][j - 1] != -1:
                    addEdge(graph, (i, j), (i, j - 1))
                if i < len(grid) - 1 and grid[i + 1][j] != -1:
                    addEdge(graph, (i, j), (i + 1, j))
                if i - 1 >= 0 and grid[i - 1][j] != -1:
                    addEdge(graph, (i, j), (i - 1, j))

        # traverse the graph calculating paths
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] in [0, -1]:
                    continue
                # run bfs to get the number of hops
                level = {
                    (i, j): 0 for i in range(len(grid)) for j in range(len(grid[i]))
                }
                queue = deque()
                queue.append((i, j))
                level[(i, j)] = 0
                while queue:
                    (currI, currJ) = queue.popleft()
                    if grid[currI][currJ] == 0:
                        # found the treasure with level hops
                        grid[i][j] = level[(currI, currJ)]
                        break

                    for neighbor in graph[(currI, currJ)]:
                        if level[neighbor] == 0:
                            queue.append(neighbor)
                            level[neighbor] = level[(currI, currJ)] + 1
