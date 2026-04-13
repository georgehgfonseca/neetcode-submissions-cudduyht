class Solution:
    def totalNQueens(self, n: int) -> int:
        res = []
        resSet = set()

        def getValidOptions(assignments):
            validOptions = set()
            for i in range(n):
                for j in range(n):
                    validOptions.add((i, j))
            for (i, j) in assignments:
                # remove same row/col
                for i2 in range(n):
                    validOptions.discard((i2, j))
                for j2 in range(n):
                    validOptions.discard((i, j2))
                # remove diagonals
                for k in range(1, n):
                    validOptions.discard((i - k, j - k)) # topLeft
                    validOptions.discard((i - k, j + k)) # topRight
                    validOptions.discard((i + k, j - k)) # botLeft
                    validOptions.discard((i + k, j + k)) # botRight
            return validOptions

        def buildBoard(assignments):
            board = []
            for i in range(n):
                row = ""
                for j in range(n):
                    if (i, j) in assignments:
                        row += "Q"
                    else:
                        row += "."
                board.append(row)
            return board

        def helper(assignments, validOptions, row):
            if len(assignments) == n:
                if frozenset(assignments) not in resSet:
                    resSet.add(frozenset(assignments))
                    res.append(buildBoard(assignments)) # TODO build board
                return

            if not validOptions:
                return
            
            for (i, j) in validOptions:
                if i == row:
                    newAssignments = assignments[:] + [(i, j)]
                    helper(newAssignments, getValidOptions(newAssignments), row + 1)
        
        helper([], getValidOptions([]), 0)
        return len(res)