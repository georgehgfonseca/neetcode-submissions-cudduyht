import heapq

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda x: x[1])

        endHeap = []
        currPass = 0

        for i in range(len(trips)):
            pas, start, end = trips[i]
            while endHeap and start >= endHeap[0][0]:
                currEnd, endPass = heapq.heappop(endHeap)
                currPass -= endPass

            currPass += pas
            heapq.heappush(endHeap, (end, pas))
            if currPass > capacity:
                return False

        return True
            



    def carPooling2(self, trips: List[List[int]], capacity: int) -> bool:
        startHeap = [(trip[1], trip[2], trip[0]) for trip in trips]
        endHeap = [(trip[2], trip[1], trip[0]) for trip in trips]
        heapq.heapify(startHeap)
        heapq.heapify(endHeap)
        (startStart, startEnd, startPass) = heapq.heappop(startHeap)
        (endEnd, endStart, endPass) = heapq.heappop(endHeap)
        currPass = startPass
        popStart = True
        while endHeap:
            while startStart < endEnd:
                if popStart:
                    (startStart, startEnd, startPass) = heapq.heappop(startHeap)
                if startStart >= endEnd:
                    popStart = False
                    break
                popStart = True
                currPass += startPass
                #%print("picked")
                #rint(startStart, startEnd, startPass, currPass)
                if currPass > capacity:
                    return False
            (endStart, endEnd, endPass) = heapq.heappop(endHeap)
            currPass -= endPass
            #print("dropped")
            #print(endStart, endEnd, endPass, currPass)
        
        return True

            



