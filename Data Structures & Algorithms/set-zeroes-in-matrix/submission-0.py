class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rowsWith0 = set()
        colsWith0 = set()
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                if matrix[row][col] == 0:
                    rowsWith0.add(row)
                    colsWith0.add(col)
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                if row in rowsWith0 or col in colsWith0:
                    matrix[row][col] = 0
        
        

        
        