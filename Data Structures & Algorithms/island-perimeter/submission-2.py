class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # count the landCells
        landCells = set() 
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    landCells.add((i, j))
        # each land cell can add up to 4 to perimeter
        perimeter = len(landCells) * 4
        # discount from perimeter overlaps (land touching other land cell)
        for (i, j) in landCells:
            if (i + 1, j) in landCells:
                perimeter -= 1
            if (i - 1, j) in landCells:
                perimeter -= 1
            if (i, j + 1) in landCells:
                perimeter -= 1
            if (i, j - 1) in landCells:
                perimeter -= 1
        
        return perimeter



        # search a land node
        firstLandCell = None
        for i in range(len(grid)):
            if firstLandCell:
                break
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    firstLandCell = (i, j)
                    break
        perimeter = 4

        # try to increase the land to bot-top-left-right using bfs
        stack = [firstLandCell]
        visited = [[False if grid[i][j] == 1 else True for j in range(len(grid[i]))] for i in range(len(grid))]
        visited[firstLandCell[0]][firstLandCell[1]] = True

        while stack:
            (i, j) = stack.pop()
            # when find new land cell, increase the perimeter by 2
            if j < len(grid[i]) and not visited[i][j + 1]:
                stack.add((i, j + 1))
                visited[i][j + 1] = True
                perimeter += 2
            if j >= 0 and not visited[i][j - 1]:
                stack.add((i, j - 1))
                visited[i][j - 1] = True
                perimeter += 2
            if i < len(grid) and not visited[i + 1][j]:
                stack.add((i + 1, j))
                visited[i + 1][j] = True
                perimeter += 2
            if i >= 0 and not visited[i - 1][j]:
                stack.add((i - 1, j))
                visited[i - 1][j] = True
                perimeter += 2
        
        return perimeter


        