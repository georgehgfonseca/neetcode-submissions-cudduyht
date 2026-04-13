from collections import deque

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # sort tickets to ensure ordering
        tickets.sort()

        # create a graph
        graph = {source: [] for source, sink in tickets}
        for (source, sink) in tickets:
            graph[source].append(sink)
        

        # find an eulerian path in the graph
        def is_bridge_edge(graph, edge):
            source, sink = edge
            if sink not in graph:
                return True
            for neighbor in graph[sink]:
                if graph[sink][neighbor] > 0:
                    return False
            return True

        # dfs
        initial_node = "JFK"
        itinerary = [initial_node]
        def dfs(node):
            if len(itinerary) == len(tickets) + 1:
                return True
            if node not in graph:
                return False
            
            neighbors = graph[node].copy()
            for i, neighbor in enumerate(neighbors):
                graph[node].pop(i)
                itinerary.append(neighbor)
                if dfs(neighbor):
                    return True
                
                graph[node].insert(i, neighbor)
                itinerary.pop()
            return False
                
        dfs(initial_node)
        return itinerary
