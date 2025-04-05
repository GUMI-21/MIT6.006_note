## Scope
+ 6 lectures on graphs, L09-L14, 2Problem Sets
## Graph Problems
+ Grpah reachability by DFS or BFS in O(|E| + |V|) time
+ Grpah exploration/connected components via Full-BFS or Full-DFS
+ Topological sort / Cycle detection via DFS
+ Negative-weight cycle detection via Bellman-Ford
+ Single Source Shortest Paths(SSSP)
![[QQ_1743666539741.png]]
+ All Pairs Shortest Paths(APSP)
-Run a SSSP algorithm |V| times
-Johnson's solves APSP with negative weihts in $O(|V|^2\log{|V|}+|V||E|)$
## Graph Problem Strategies
+ Be sure to explicitly describe a graph in terms of problem parameters.
+ Convert problem into finding a shortest path, cycle, topo. sort, conn. comps., etc.
+ May help to duplicate graph vertices to encode additional information
+ May help to add auxiliary vertices/edges to graph
+ May help to pre-process the graph (e.g., to remove part of the graph)
## Supplement
#### DFS decte cycle in DG
In the **color marking method** for detecting cycles in a **directed graph**:
- **White**: A node that has not been visited (not in the recursion stack).
- **Gray**: A node that is currently in the recursion stack (being processed).
- **Black**: A node whose DFS traversal is complete (all its descendants have been processed).
If a **gray node** is encountered during DFS traversal, it means there is a **cycle** in the graph.
```python
def has_negative_cycle(graph, V):
    WHITE, GRAY, BLACK = 0, 1, 2  # Color states
    color = {i: WHITE for i in range(V)}  # Initialize all nodes as WHITE (unvisited)
    dist = {i: 0 for i in range(V)}  # Distance array to track path weights

    def dfs(node):
        color[node] = GRAY  # Mark node as being processed (in recursion stack)
        for neighbor, weight in graph[node]:
            if color[neighbor] == WHITE:  # If the neighbor is unvisited, explore it
                dist[neighbor] = dist[node] + weight  # Update distance
                if dfs(neighbor):  # Recur and check for a negative cycle
                    return True
            elif color[neighbor] == GRAY:  # If a back edge to a GRAY node is found (cycle detected)
                if dist[neighbor] > dist[node] + weight:  # Check if it's a negative cycle
                    return True
                if dist[neightbor] <= dist[node] + weight: # positive cycle
        color[node] = BLACK  # Mark node as fully processed
        return False

    for node in range(V):
        if color[node] == WHITE:  # Start DFS from unvisited nodes
            if dfs(node):
                return True
    return False

# Test case
graph = {
    0: [(1, 1)], 
    1: [(2, -1)], 
    2: [(0, -1)]  # Negative cycle
}
print(has_negative_cycle(graph, 3))  # Output: True

```
