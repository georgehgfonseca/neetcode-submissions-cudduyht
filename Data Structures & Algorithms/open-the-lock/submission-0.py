from collections import deque

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        # bfs from the initial state
        # dynamically create a graph of neighbor states in this bfs
        # if is a deadend - do not create
        # otherwise, create a new node
        # check if target has been reached in each step
        # can be optimized (?) - no need to turn +1/-1 at a time for a wheel, can go directly to target if does not hit any deadend
        def getCellFromStr(str: str):
            return [int(wheel) for wheel in str]

        def getNextWheel(wheel: int) -> str:
            return str((wheel + 1) % 10)

        def getPrevWheel(wheel: int) -> str:
            if wheel == 0:
                return '9'
            return str(wheel - 1)

        def getWheelNeighbors(cell: str, i: int):
            neighbors = set()
            cellNextWheel = cell[:i] + getNextWheel(int(cell[i])) + cell[i + 1:]
            if cell not in deadends:
                neighbors.add(cellNextWheel)
            cellPrevWheel = cell[:i] + getPrevWheel(int(cell[i])) + cell[i + 1:]
            if cell not in deadends:
                neighbors.add(cellPrevWheel)
            return neighbors
        
        def getCellNeighbors(cell):
            neighbors = set()
            for i in range(len(cell)):
                neighbors |= getWheelNeighbors(cell, i)
            return neighbors

        def getStrFromCell(cell):
            cellStr = ""
            for wheel in cell:
                cellStr += str(wheel)
            return cellStr

        def bfs(cell):
            visited = {cell: 0} # node: min moves to findit
            queue = deque()
            queue.append(cell)
            while queue:
                node = queue.popleft()
                if node == target: # can optimize comparing an int with 4 chars instead of the 4-sized array
                    return visited[node]
                for neighbor in getCellNeighbors(node):
                    if neighbor not in visited:
                        visited[neighbor] = visited[node] + 1
                        queue.append(neighbor)
            return -1
        
        return bfs("0000")
        