class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.prefixSum = [[matrix[i][j] for j in range(len(matrix[i]))] for i in range(len(matrix))]
        # prefix sum for each row
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if j - 1 >= 0:
                    self.prefixSum[i][j] += self.prefixSum[i][j - 1]

        # prefix sum row-wise
        for i in range(1, len(matrix)):
            for j in range(len(matrix[i])):
                if i - 1 >= 0:
                    self.prefixSum[i][j] += self.prefixSum[i - 1][j]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # get prefix sum of (row2, col2) and subtract area outside of (row1, col1)
        total = self.prefixSum[row2][col2]
        if row1 > 0:
            total -= self.prefixSum[row1 - 1][col2]
        if col1 > 0:
            total -= self.prefixSum[row2][col1 - 1]
        
        # avoid duplicated subtraction
        if row1 > 0 and col1 > 0:
            total += self.prefixSum[row1 - 1][col1 - 1]
        return total
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)