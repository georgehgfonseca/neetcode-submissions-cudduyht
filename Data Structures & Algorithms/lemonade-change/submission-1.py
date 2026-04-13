class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        # bills  = [5, 10, 5, 5, 20]
        # change = 10
        cellCount = {5: 0, 10: 0, 20: 0}
        for bill in bills:
            if bill == 5:
                cellCount[5] += 1
            elif bill == 10:
                cellCount[10] += 1
                cellCount[5] -= 1
            elif bill == 20:
                cellCount[20] += 1
                if cellCount[10] > 0:
                    cellCount[10] -= 1
                    cellCount[5] -= 1
                else:
                    cellCount[5] -= 3
            if cellCount[5] < 0 or cellCount[10] < 0 or cellCount[20] < 0:
                return False
        return True
        