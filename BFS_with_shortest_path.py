from collections import deque

def bfs_with_shortest_paths(graph, start):
    # Initialize a queue for BFS and a dictionary to store the distance and path counts.
    queue = deque()
    distance = {vertex: float('inf') for vertex in graph}
    path_count = {vertex: 0 for vertex in graph}

    # Initialize the starting vertex.
    queue.append(start)
    distance[start] = 0
    path_count[start] = 1

    while queue:
        current_vertex = queue.popleft()

        for neighbor in graph[current_vertex]:
            if distance[neighbor] == float('inf'):
                # If the neighbor is being visited for the first time, enqueue it.
                queue.append(neighbor)
                distance[neighbor] = distance[current_vertex] + 1

            # If the neighbor is on a shortest path, update the path count.
            if distance[neighbor] == distance[current_vertex] + 1:
                path_count[neighbor] += path_count[current_vertex]

    return distance, path_count


# Example graph represented as an adjacency list.
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['E'],
    'D': ['F'],
    'E': ['F'],
    'F': []
}

start_vertex = 'A'
distances, paths = bfs_with_shortest_paths(graph, start_vertex)

for vertex in graph:
    print(f"Shortest distance to {vertex} from {start_vertex}: {distances[vertex]}")
    print(f"Number of shortest paths to {vertex}: {paths[vertex]}")
