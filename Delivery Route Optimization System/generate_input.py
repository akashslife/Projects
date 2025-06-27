import json
import os

def get_user_input():
    n = int(input("Enter number of locations (nodes): "))
    
    # Initialize graph with "inf" as strings
    graph = [["inf" for _ in range(n)] for _ in range(n)]
    
    for i in range(n):
        graph[i][i] = 0  # Distance to self is zero
    
    e = int(input("Enter number of direct roads (edges): "))
    
    print("Enter edges in the format: from to cost")
    for _ in range(e):
        u, v, w = map(int, input("Edge (u v w): ").split())
        graph[u][v] = w  # Directed graph (if undirected, add graph[v][u] = w)

    # Delivery points
    delivery_points = list(map(int, input("Enter delivery point indices (space-separated): ").split()))

    # Prepare JSON data
    data = {
        "graph": graph,
        "delivery_points": delivery_points
    }

    # Save JSON
    with open("input_graph.json", "w") as f:
        json.dump(data, f, indent=2)

    print("\n✅ input_graph.json has been saved successfully.")
    print("🚀 Running main.py for optimization...\n")

    # Run main.py
    os.system("python main.py")

if __name__ == "__main__":
    get_user_input()
