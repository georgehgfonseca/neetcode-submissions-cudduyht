class CountSquares:

    def __init__(self):
        self.pointsPerX = defaultdict(lambda: defaultdict(int))
        self.pointsPerY = defaultdict(lambda: defaultdict(int))
        self.points = list()

    def add(self, point: List[int]) -> None:
        x, y = point
        self.pointsPerX[x][y] += 1
        self.pointsPerY[y][x] += 1
        self.points.append((x, y))
        
    def count(self, point: List[int]) -> int:
        # for each point (x2, y2), search points that x2 == y and y2 == x
        res = 0
        x, y = point
        for (x2, y2) in self.points:
            if x2 == x or y2 == y:
                continue
                
            res += (self.pointsPerX[x2][y] * self.pointsPerY[y2][x])
        return res

