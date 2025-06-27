import json
from floyd_warshall import floyd_warshall
from tsp_solver import tsp

INF = float('inf')

def load_input(file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)
    graph = [
        [INF if cell == "inf" else cell for cell in row]
        for row in data["graph"]
    ]
    delivery_points = data["delivery_points"]
    return graph, delivery_points

def main():
    graph, delivery_points = load_input(r"C:\Users\Akash\OneDrive\Desktop\programing\Projects\projects\input_graph.json")

    shortest_paths = floyd_warshall(graph)
    optimal_path, min_cost = tsp(delivery_points, shortest_paths)

    print("Optimal Delivery Path:", ' -> '.join(map(str, optimal_path)))
    print("Minimum Total Travel Time:", min_cost)

if __name__ == "__main__":
    main()
