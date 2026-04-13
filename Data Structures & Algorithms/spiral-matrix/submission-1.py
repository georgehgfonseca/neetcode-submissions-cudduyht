class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # move all the way in one direction, then in other, in the order (right, down, left, up)
        # keep track of visited cells to forbid revisiting

        ROWS, COLS = len(matrix), len(matrix[0])
        visited = set()
        direction = "R"
        i, j = 0, 0
        res = []
        while len(visited) < ROWS * COLS:
            visited.add((i, j))
            res.append(matrix[i][j])
            if direction == "R":
                if j + 1 < COLS and (i, j + 1) not in visited:
                    j += 1
                else:
                    i += 1
                    direction = "D"
            elif direction == "D":
                if i + 1 < ROWS and (i + 1, j) not in visited:
                    i += 1
                else:
                    j -= 1
                    direction = "L"
            elif direction == "L":
                if j - 1 >= 0 and (i, j - 1) not in visited:
                    j -= 1
                else:
                    i -= 1
                    direction = "U"
            elif direction == "U":
                if i - 1 >= 0 and (i - 1, j) not in visited:
                    i -= 1
                else:
                    j += 1
                    direction = "R"
        return res

            