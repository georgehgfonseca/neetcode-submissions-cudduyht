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
            mst = []
            mstMaxWeight = float("-inf")
            mstIdxs = set()
#            if include:
#                node = forbiddenEdge[0]
#                mst.append(forbiddenEdge)
#                mstIdxs.add(forbiddenEdge[3])
#                mastWeight += forbiddenEdge[2]
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
                    return [], float("inf"), set(), mstMaxWeight
                nextWeight, idx, nextNode, nextNeighbor = heapq.heappop(heap)
                while nextNode in connected and nextNeighbor in connected:
                    if not heap:
                        # prim's ran on a disconnected graph
                        return [], float("inf"), set(), mstMaxWeight
                    nextWeight, idx, nextNode, nextNeighbor = heapq.heappop(heap)
                mst.append((nextNode, nextNeighbor, nextWeight, idx))
                mstIdxs.add(idx)
                mstWeight += nextWeight
                mstMaxWeight = max(mstMaxWeight, nextWeight)
                connected.add(nextNeighbor)
                node = nextNeighbor
            return mst, mstWeight, mstIdxs, mstMaxWeight
        
        mst, mstWeight, mstIdxs, mstMaxWeight = prim((-1, -1, -1, -1))
        critical, pseudo = [], []
        for i, e in enumerate(edges):
            mstI, mstWeightI, mstIdxsI, mstMaxWeightI = prim((e[0], e[1], e[2], i), False)
            if mstWeight < mstWeightI:
                critical.append(i)
                continue
            mstI, mstWeightI, mstIdxsI, mstMaxWeightI = prim((e[0], e[1], e[2], i), True)
            if mstWeight == mstWeightI:
                pseudo.append(i)
        return [critical, pseudo]



            
        critical = mstIdxs
        pseudo = set()
        #print(graph)
        #print(mst)
        for (node, nextNode, nextWeight, nextIdx) in mst:
            #print(node, nextNode, nextWeight, nextIdx)
            newMst, newMstWeight, newMstIdxs = prim((node, nextNode))
            if not newMst:
                continue
            for newEdgeIdx in newMstIdxs:
                pseudo.add(newEdgeIdx)
            toRemove = set()
            for edgeIdx in critical:
                if edgeIdx not in newMstIdxs and edgeIdx != nextIdx:
                    toRemove.add(edgeIdx)
            for edgeIdx in toRemove:
                critical.discard(edgeIdx)
        
        toRemove = set()
        for edgeIdx in pseudo:
            if edgeIdx in critical:
                toRemove.add(edgeIdx)
        for edgeIdx in toRemove:
            pseudo.discard(edgeIdx)
        

        return [list(critical), list(pseudo)]

        
        appearAll = [True for _ in edges]
        appearAny = [False for _ in edges]
        for (node, nextNode, nextWeight, nextIdx) in mst:
            newMst, newMstWeight, newMstIdxs = prim((node, nextNode))
            for idx in newMstIdxs:
                appearAny[idx] = True