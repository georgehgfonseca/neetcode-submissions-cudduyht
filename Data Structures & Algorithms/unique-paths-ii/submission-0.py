class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # paths = [[0 if obstacleGrid[i][j] == 0 else -1 for j in range(len(obstacleGrid[i]))] for i in range(len(obstacleGrid))]
        paths = [[0 for j in range(len(obstacleGrid[i]))] for i in range(len(obstacleGrid))]
        m, n = len(obstacleGrid), len(obstacleGrid[0])

        for i in range(len(obstacleGrid)):
            if obstacleGrid[i][0] == 1:
                break
            paths[i][0] = 1
        for i in range(len(obstacleGrid[0])):
            if obstacleGrid[0][i] == 1:
                break
            paths[0][i] = 1

        for i in range(1, len(obstacleGrid)):
            for j in range(1, len(obstacleGrid[i])):
                if obstacleGrid[i][j] == 1:
                    continue
                paths[i][j] += paths[i-1][j] + paths[i][j-1]
        
        return paths[m - 1][n - 1]
