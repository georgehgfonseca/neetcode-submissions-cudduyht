class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        l, r = 0, len(matrix[0]) - 1
        while l < r:
            t, b = l, r
            for offset in range(r - l):
                # do a square rotation
                top = matrix[t][l + offset]
                matrix[t][l + offset] = matrix[b - offset][l]
                matrix[b - offset][l] = matrix[b][r - offset]
                matrix[b][r - offset] = matrix[t + offset][r]
                matrix[t + offset][r] = top
            l += 1
            r -= 1
