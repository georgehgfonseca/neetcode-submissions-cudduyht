from collections import defaultdict
import heapq

class Solution:
    def findCheapestPriceBF(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Bellman Ford
        dist = [float("inf") for _ in range(n)]
        dist[src] = 0

        for _ in range(k + 1):
            tmpDist = dist.copy()
            for source, sink, weight in flights:
                if dist[source] == float("inf"):
                    continue

                if tmpDist[sink] > dist[source] + weight:
                    tmpDist[sink] = dist[source] + weight
            
            dist = tmpDist
        
        return -1 if dist[dst] == float("inf") else dist[dst]

    def findCheapestPrice3(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(dict)
        for source, sink, price in flights:
            graph[source][sink] = price
        
        queue = [(0, src, -1)]
        dist = [[float("inf") for i in range(n)] for _ in range(k + 1)] # (cost, hops)
        dist[src][0] = 0
        #visited = set()

        while queue:
            distNode, node, stops = heapq.heappop(queue)
            if node == dst:
                return distNode
            if stops == k or dist[node][stops + 1] < distNode:
                # prioritize paths with less hops
                continue
            #if node in visited or stops == k:
            #    continue
            #visited.add(node)

            for neighbor in graph[node]:
                nextCost = dist[node][stops] + graph[node][neighbor]
                nextStops = stops + 1
                if dist[neighbor][nextStops + 1] > nextCost:
                    dist[neighbor][nextStops + 1] = nextCost
                    heapq.heappush(queue, (nextCost, neighbor, nextStops))
        
        return -1

    def findCheapestPrice2(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(dict)
        for source, sink, price in flights:
            graph[source][sink] = price
        
        queue = [(0, src)]
        dist = [(float("inf"), 0) for i in range(n)] # (cost, hops)
        dist[src] = (0, 0)
        visited = set()

        while queue:
            distNode, node = heapq.heappop(queue)
            if node in visited:
                continue
            if node == dst:
                return distNode
            visited.add(node)

            for neighbor in graph[node]:
                if dist[neighbor][0] > dist[node][0] + graph[node][neighbor] and (dist[node][1] < k or (neighbor == dst and dist[node][1] <= k)):
                    dist[neighbor] = (dist[node][0] + graph[node][neighbor], dist[node][1] + 1)
                    heapq.heappush(queue, (dist[neighbor][0], neighbor))
        
        return -1

    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(dict)
        for source, sink, price in flights:
            graph[source][sink] = price
        
        queue = [(0, src, -1)]
        dist = [[float("inf") for _ in range(k + 2)] for i in range(n)] # (cost, hops)
        dist[src][0] = 0
        visited = set()

        while queue:
            print(dist)
            distNode, node, stops = heapq.heappop(queue)
            if node == dst:
                return distNode
            if node in visited or stops == k or dist[node][stops + 1] < distNode:
                continue
            #visited.add(node)

            for neighbor in graph[node]:
                nextStops = stops + 1
                if dist[neighbor][nextStops + 1] > distNode + graph[node][neighbor]:
                    dist[neighbor][nextStops + 1] = distNode + graph[node][neighbor]
                    heapq.heappush(queue, (dist[neighbor][nextStops + 1], neighbor, nextStops))
        
        return -1