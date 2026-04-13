from collections import deque

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        
        # Fill first row
        for j in range(1, cols):
            grid[0][j] += grid[0][j - 1]
        
        # Fill first column
        for i in range(1, rows):
            grid[i][0] += grid[i - 1][0]
        
        # Fill the rest of the grid
        for i in range(1, rows):
            for j in range(1, cols):
                grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])
        
        return grid[rows - 1][cols - 1]

    def minPathSum2(self, grid: List[List[int]]) -> int:
        if len(grid) == 1 and len(grid[0]) == 1:
            return grid[0][0]
            
        cellMinSum = {(0,0): grid[0][0]}
        i, j = 0, 0
        cellsToTest = deque()
        testedCells = {(0, 0)}
        if i + 1 < len(grid):
            cellsToTest.append((1, 0))
        if j + 1 < len(grid[0]):
            cellsToTest.append((0, 1))
        while cellsToTest:
            (i, j) = cellsToTest.popleft()
            testedCells.add((i, j))
            prevUp = cellMinSum[(i - 1, j)] if i - 1 >= 0 else float("inf")
            prevLeft = cellMinSum[(i, j - 1)] if j - 1 >= 0 else float("inf")
            
            cellMinSum[(i, j)] = min(prevUp, prevLeft) + grid[i][j]

            if i + 1 < len(grid) and (i + 1, j) not in testedCells:
                cellsToTest.append((i + 1, j))
            if j + 1 < len(grid[0]) and (i, j + 1) not in testedCells:
                cellsToTest.append((i, j + 1))

        return cellMinSum[(len(grid) - 1, len(grid[0]) - 1)]