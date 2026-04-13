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
        
    def setZeroes(self, matrix: List[List[int]]) -> None:
        zero1stRow = False
        for col in range(len(matrix[0])):
            if matrix[0][col] == 0:
                zero1stRow = True
        zero1stCol = False
        for row in range(len(matrix)):
            if matrix[row][0] == 0:
                zero1stCol = True

        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                if matrix[row][col] == 0:
                    matrix[0][col] = 0
                    matrix[row][0] = 0

        for row in range(1, len(matrix)):
            for col in range(1, len(matrix[row])):
                if matrix[0][col] == 0 or matrix[row][0] == 0:
                    matrix[row][col] = 0
        
        if zero1stCol:
            for row in range(len(matrix)):
                matrix[row][0] = 0
        if zero1stRow:
            for col in range(len(matrix[0])):
                matrix[0][col] = 0
        return
        
        print(matrix)
        for row in range(len(matrix)):
            if matrix[row][0] == 0:
                for col in range(len(matrix)):
                    matrix[row][col] = 0
        
        for col in range(len(matrix)):
            if matrix[0][col] == 0:
                for row in range(len(matrix)):
                    matrix[row][col] = 0
        
        

        
        