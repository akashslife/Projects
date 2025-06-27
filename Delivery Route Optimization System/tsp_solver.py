import itertools
INF = float('inf')

def tsp(delivery_points, dist):
    """
    Solves the Traveling Salesman Problem (TSP) for a given set of delivery points
    using brute-force permutations.

    Parameters:
        delivery_points (list): List of location indices to visit.
        dist (list of lists): All-pairs shortest path matrix (e.g., from Floyd-Warshall).

    Returns:
        tuple: (best_path, min_cost)
            - best_path (tuple): The order of visiting delivery points.
            - min_cost (float): Minimum total travel cost.
    """
    min_cost = INF
    best_path = []

    for perm in itertools.permutations(delivery_points):
        cost = 0
        for i in range(len(perm) - 1):
            cost += dist[perm[i]][perm[i + 1]]
        if cost < min_cost:
            min_cost = cost
            best_path = perm

    return best_path, min_cost
