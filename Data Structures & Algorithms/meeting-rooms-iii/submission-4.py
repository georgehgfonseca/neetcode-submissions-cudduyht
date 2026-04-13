import heapq

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        # sort the rooms
        # iterate over them, assign a room if any is free
        # store the freeing time for each room
        # delay the meeting when no room is available
        # meetings           = [[2,13], [3,12], [7,10], [17,19], [18,19]]
        # i                  =                             *
        # rooms              = [ (0, 3, 0) (10, 2, 1) (12, 1, 1) (13, 0, 1) ] use a heap to compute efficiently
        #meetings.sort(key=lambda x: x[1])
        meetings.sort()
        meetCount = [0] * n
        rooms = [(0, i) for i in range(n)] # (releaseTime, index, meetCount)
        heapq.heapify(rooms)

        for (start, end) in meetings:
            while rooms and rooms[0][0] < start:
                (releaseTime, index) = heapq.heappop(rooms)
                heapq.heappush(rooms, (start, index))

            (releaseTime, index) = heapq.heappop(rooms)
            heapq.heappush(rooms, (releaseTime + (end - start), index))
            meetCount[index] += 1

        print(rooms)
        return meetCount.index(max(meetCount))
