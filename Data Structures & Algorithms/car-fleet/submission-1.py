class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_speed_arrival = [[position[i], speed[i], (target - position[i]) / speed[i], True] for i in range(len(position))]
        pos_speed_arrival.sort(reverse=True)
        for i in range(len(pos_speed_arrival)):
            if not pos_speed_arrival[i][3]:
                continue
            for j in range(i + 1, len(pos_speed_arrival)):
                will_collide = pos_speed_arrival[i][2] >= pos_speed_arrival[j][2]
                if will_collide:
                    pos_speed_arrival[j][3] = False
                else:
                    break
        ans = 0
        for elem in pos_speed_arrival:
            if elem[3]:
                ans += 1
        return ans
        