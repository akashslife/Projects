# Delivery Route Optimization Project

This project implements a **delivery route optimization system** using the **Floyd-Warshall algorithm** to compute all-pairs shortest paths and a **brute-force Traveling Salesman Problem (TSP)** solver to find the optimal delivery route for a given set of delivery points. The project takes a weighted directed graph as input, where nodes represent locations, edges represent roads, and weights represent travel times. It outputs the optimal path to visit specified delivery points and the minimum total travel time.

## Project Structure

The project consists of the following files located in the root directory:

- **`main.py`**: The main script that orchestrates the program. It loads the input graph, runs the Floyd-Warshall algorithm, solves the TSP, and prints the optimal delivery path and cost.
- **`floyd_warshall.py`**: Implements the Floyd-Warshall algorithm to compute the shortest paths between all pairs of nodes.
- **`tsp_solver.py`**: Implements a brute-force TSP solver to find the optimal route visiting all delivery points.
- **`generate_input.py`**: A utility script to generate input data by taking user input for the graph and delivery points, saving it to a JSON file, and running `main.py`.
- **`input_graph.json`**: A JSON file containing the input graph (adjacency matrix) and delivery points. This is either user-generated via `generate_input.py` or can be manually created/edited.

## Prerequisites

- **Python 3.x**: Ensure Python 3 is installed on your system.
- **Required Libraries**: The project uses the following standard Python libraries (no external installations required):
  - `json` (for reading/writing JSON files)
  - `itertools` (for generating permutations in TSP solver)
  - `os` (for running `main.py` from `generate_input.py`)

You can verify your Python version by running:
```bash
python --version
```

## File Details and Usage

### 1. `main.py`
**Purpose**: The entry point of the program. It:
- Loads the input graph and delivery points from `input_graph.json`.
- Runs the Floyd-Warshall algorithm (from `floyd_warshall.py`) to compute shortest paths.
- Solves the TSP (using `tsp_solver.py`) to find the optimal delivery route.
- Prints the optimal path and minimum total travel time.

**Dependencies**:
- Imports `json` for reading `input_graph.json`.
- Imports `floyd_warshall` from `floyd_warshall.py`.
- Imports `tsp` from `tsp_solver.py`.

**Execution**:
Run the script directly from the command line:
```bash
python main.py
```

**Input**:
- Expects `input_graph.json` in the root directory (or a valid path specified in the script).
- The JSON file must contain:
  - `"graph"`: An adjacency matrix where `"inf"` represents no direct edge, and integers represent edge weights (travel times).
  - `"delivery_points"`: A list of node indices to visit.

**Output**:
- Prints the optimal delivery path (e.g., `0 -> 2 -> 4`) and the minimum total travel time.

**Note**:
- The script assumes `input_graph.json` exists. If not, you must generate it using `generate_input.py` or create it manually.
- The default file path in `main.py` is `C:\Users\Akash\OneDrive\Desktop\programing\Projects\projects\input_graph.json`. Update this path to match your local file location:
  ```python
  graph, delivery_points = load_input("input_graph.json")  # Update to your path
  ```

### 2. `floyd_warshall.py`
**Purpose**: Implements the Floyd-Warshall algorithm to compute the shortest paths between all pairs of nodes in a weighted directed graph.

**Dependencies**:
- Uses `float('inf')` for representing unreachable nodes.

**Function**:
- `floyd_warshall(graph)`: Takes an adjacency matrix as input and returns a matrix of shortest distances.

**Input**:
- `graph`: A square matrix (list of lists) where `graph[i][j]` is the weight of the edge from node `i` to node `j`. Use `float('inf')` for no direct edge.

**Output**:
- A matrix where `dist[i][j]` represents the shortest path distance from node `i` to node `j`.

**Usage**:
- This module is imported and used by `main.py`. It does not need to be run independently.

### 3. `tsp_solver.py`
**Purpose**: Implements a brute-force Traveling Salesman Problem solver to find the optimal route visiting all delivery points.

**Dependencies**:
- Imports `itertools` for generating permutations.
- Uses `float('inf')` for initializing the minimum cost.

**Function**:
- `tsp(delivery_points, dist)`: Takes a list of delivery point indices and a shortest-path matrix (from Floyd-Warshall) and returns the optimal path and its cost.

**Input**:
- `delivery_points`: List of node indices to visit.
- `dist`: All-pairs shortest path matrix.

**Output**:
- A tuple `(best_path, min_cost)` where:
  - `best_path`: The optimal order of visiting delivery points.
  - `min_cost`: The total travel time for the optimal path.

**Usage**:
- This module is imported and used by `main.py`. It does not need to be run independently.

### 4. `generate_input.py`
**Purpose**: A utility script to:
- Take user input for the graph (number of nodes, edges, and weights) and delivery points.
- Save the input to `input_graph.json`.
- Automatically run `main.py` to compute the optimal delivery route.

**Dependencies**:
- Imports `json` for writing to `input_graph.json`.
- Imports `os` for executing `main.py`.

**Execution**:
Run the script from the command line:
```bash
python generate_input.py
```

**Input (via command line prompts)**:
- Number of locations (nodes).
- Number of direct roads (edges).
- Edge details in the format `u v w` (from node, to node, weight).
- Space-separated list of delivery point indices.

**Output**:
- Creates `input_graph.json` in the root directory.
- Runs `main.py` and displays its output (optimal path and cost).

**Example Interaction**:
```bash
Enter number of locations (nodes): 5
Enter number of direct roads (edges): 8
Enter edges in the format: from to cost
Edge (u v w): 0 1 3
Edge (u v w): 1 0 2
Edge (u v w): 0 3 5
Edge (u v w): 1 3 4
Edge (u v w): 1 4 6
Edge (u v w): 2 1 1
Edge (u v w): 2 4 2
Edge (u v w): 3 2 2
Enter delivery point indices (space-separated): 0 2 4

✅ input_graph.json has been saved successfully.
🚀 Running main.py for optimization...

Optimal Delivery Path: 0 -> 2 -> 4
Minimum Total Travel Time: 5
```

### 5. `input_graph.json`
**Purpose**: Stores the input graph and delivery points in JSON format.

**Structure**:
- `"graph"`: An adjacency matrix where:
  - `"inf"` (string) represents no direct edge.
  - Integers represent edge weights.
  - `graph[i][i] = 0` for all nodes.
- `"delivery_points"`: A list of node indices to visit.

**Example** (from provided file):
```json
{
  "graph": [
    [0, 3, "inf", 5, "inf"],
    [2, 0, "inf", 4, 6],
    ["inf", 1, 0, "inf", 2],
    ["inf", "inf", 2, 0, 1],
    [3, "inf", "inf", "inf", 0]
  ],
  "delivery_points": [0, 2, 4]
}
```

**Usage**:
- Generated by `generate_input.py` or manually edited.
- Read by `main.py` for processing.

**File Path**:
- By default, savedイ

System: **How to Run the Project**

1. **Generate Input**:
   - Run `generate_input.py` to create or update `input_graph.json`:
     ```bash
     python generate_input.py
     ```
   - Follow the prompts to input the number of nodes, edges, edge weights, and delivery points.
   - This script will generate `input_graph.json` and automatically run `main.py` to display the results.

2. **Run Directly** (if `input_graph.json` already exists):
   - Ensure `input_graph.json` is in the correct directory (or update the path in `main.py`).
   - Run:
     ```bash
     python main.py
     ```
   - This will read `input_graph.json`, compute the shortest paths using Floyd-Warshall, solve the TSP, and print the optimal delivery path and total travel time.

**Example Output** (using the provided `input_graph.json`):
```bash
Optimal Delivery Path: 0 -> 2 -> 4
Minimum Total Travel Time: 5
```

## Notes
- **Graph Assumptions**: The graph is directed. For an undirected graph, you must add symmetric edges (e.g., `graph[u][v] = w` and `graph[v][u] = w`) in `generate_input.py`.
- **Performance**: The TSP solver uses a brute-force approach, which is computationally expensive for large numbers of delivery points (factorial time complexity). For production use, consider optimizing with dynamic programming or heuristic methods for larger inputs.
- **File Paths**: Update the file path in `main.py` to match the location of `input_graph.json` on your system:
  ```python
  graph, delivery_points = load_input("input_graph.json")  # Update path as needed
  ```
- **Error Handling**: Ensure `input_graph.json` exists and is correctly formatted to avoid errors in `main.py`.

## Example Workflow
1. Run:
   ```bash
   python generate_input.py
   ```
2. Enter the graph details (e.g., 5 nodes, 8 edges, and delivery points `[0, 2, 4]` as shown in the example).
3. The script generates `input_graph.json` and runs `main.py`, which outputs the optimal path and cost.

## Limitations
- The brute-force TSP solver is inefficient for large numbers of delivery points (>10) due to its O(n!) complexity.
- The program assumes valid input (e.g., non-negative weights, valid node indices). Invalid inputs may cause errors.
- The graph is treated as directed unless modified in `generate_input.py` to support undirected edges.

## Future Improvements
- Replace the brute-force TSP solver with a more efficient algorithm (e.g., dynamic programming or nearest-neighbor heuristic) for better scalability.
- Add input validation in `generate_input.py` to handle invalid user inputs gracefully.
- Support undirected graphs by automatically adding symmetric edges in `generate_input.py`.
- Add support for visualizing the graph and path using a library like `matplotlib` or `networkx`.