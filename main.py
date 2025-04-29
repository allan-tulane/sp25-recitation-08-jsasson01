from collections import deque
from heapq import heappush, heappop
import heapq

def shortest_shortest_path(graph, source):
    """
    graph: dict where keys are nodes and values are sets of (neighbor, weight) tuples
    source: starting node
    returns: dict mapping node to (shortest path total weight, number of edges)
    """
    result = {}
    heap = []
    heapq.heappush(heap, (0, 0, source))  # (distance_so_far, edges_so_far, node)
    visited = set()

    while heap:
        dist, edges, node = heapq.heappop(heap)

        if node in visited:
            continue

        # Record (distance, number of edges)
        result[node] = (dist, edges)
        visited.add(node)

        for neighbor, weight in graph.get(node, []):
            if neighbor not in visited:
                heapq.heappush(heap, (dist + weight, edges + 1, neighbor))

    return result



def bfs_path(graph, source):
    """
    Returns:
      a dict where each key is a vertex and the value is the parent of 
      that vertex in the shortest path tree.
    """
    parents = {}
    visited = set()
    queue = deque()

    queue.append(source)
    visited.add(source)

    while queue:
        u = queue.popleft()
        for v in graph.get(u, []):
            if v not in visited:
                parents[v] = u
                visited.add(v)
                queue.append(v)

    return parents
    pass

def get_sample_graph():
     return {'s': {'a', 'b'},
            'a': {'b'},
            'b': {'c'},
            'c': {'a', 'd'},
            'd': {}
            }


    
def get_path(parents, destination):
    """
    Returns:
      The shortest path from the source node to this destination node 
      (excluding the destination node itself). See test_get_path for an example.
    """
    path = []
    current = destination
    while current in parents:
        path.append(current)
        current = parents[current]
    path.append(current)  # append the source (has no parent)
    path.reverse()
    path =path[:-1]
    return ''.join(path)
    pass



