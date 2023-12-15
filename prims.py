import heapq

def prim(graph):
    visited, mst, pq = set(), [], [(0, list(graph.keys())[0])]

    while pq:
        cost, current = heapq.heappop(pq)
        if current not in visited:
            visited.add(current)
            mst.append((cost, current))
            pq.extend((neighbor_cost, neighbor) for neighbor, neighbor_cost in graph[current] if neighbor not in visited)
            #pq.extend((y, x) for x,y in graph[node] if x not in visited)

    return mst

# Example usage
graph = {'A': [('B', 2), ('C', 3)], 'B': [('A', 2), ('C', 4), ('D', 1)],
         'C': [('A', 3), ('B', 4), ('D', 5)], 'D': [('B', 1), ('C', 5)]}

result = prim(graph)
print("Minimum Spanning Tree:", result)
