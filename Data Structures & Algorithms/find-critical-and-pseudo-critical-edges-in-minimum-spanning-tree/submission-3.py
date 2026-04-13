import heapq

class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        # prim algorithm
        graph = defaultdict(dict)
        for i, (source, sink, weight) in enumerate(edges):
            graph[source][sink] = (weight, i)
            graph[sink][source] = (weight, i)
        
        def prim(forbiddenEdge, include = False):
            node = 0
            mstWeight = 0
            if include:
                node = forbiddenEdge[0]
                mstWeight += forbiddenEdge[2]
            connected = {node}
            heap = []
            while len(connected) < n:
                for neighbor in graph[node]:
                    if (node, neighbor) == (forbiddenEdge[0], forbiddenEdge[1]) or (neighbor, node) == (forbiddenEdge[0], forbiddenEdge[1]):
                        # artificially add edge with 0 cost
                        if include:
                            heapq.heappush(heap, (0, graph[node][neighbor][1], node, neighbor))
                        continue
                    if neighbor not in connected:
                        heapq.heappush(heap, (graph[node][neighbor][0], graph[node][neighbor][1], node, neighbor))
                if not heap:
                    # prim's ran on a disconnected graph
                    return float("inf")
                nextWeight, idx, nextNode, nextNeighbor = heapq.heappop(heap)
                while nextNode in connected and nextNeighbor in connected:
                    if not heap:
                        # prim's ran on a disconnected graph
                        return float("inf")
                    nextWeight, idx, nextNode, nextNeighbor = heapq.heappop(heap)
                mstWeight += nextWeight
                connected.add(nextNeighbor)
                node = nextNeighbor
            return mstWeight
        
        mstWeight = prim((-1, -1, -1, -1))
        critical, pseudo = [], []
        for i, e in enumerate(edges):
            if mstWeight < prim((e[0], e[1], e[2], i), False):
                critical.append(i)
                continue
            if mstWeight == prim((e[0], e[1], e[2], i), True):
                pseudo.append(i)
        return [critical, pseudo]