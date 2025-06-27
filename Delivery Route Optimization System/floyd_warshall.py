INF = float('inf')

def floyd_warshall(graph):
    """
    Function to compute the shortest paths between all pairs of vertices
    using Floyd-Warshall algorithm.

    Parameters:
        graph (list of lists): Adjacency matrix of the graph where
        graph[i][j] represents weight from node i to j. Use float('inf') if no direct edge.

    Returns:
        list of lists: Matrix of shortest distances between all pairs.
    """
    n = len(graph)
    # Create a copy of the graph to store distances
    dist = [row[:] for row in graph]

    # Floyd-Warshall algorithm
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    
    return dist
