## BFS & DFS

BFS(Breadth-First-Search) and DFS(Depth-First-Search) are 2 common ways to **search a path from A to B** in the graph.

This article will focus on **UndirectedGraph Graph**.

### BFS

BFS will traverse **all the adjacent vertices** before moving to the next **vertex**.

It's similar to **Level traversing** of Tree. So we need a **queue** to traverse the vertices.

Here, we use BFS to find a path in a graph.

```python
def bfs(graph: UndirectedGraph, start: int, end: int) -> None:
    if start == end:
        print("The start is equal to the end.")
        return
    if start not in range(0, graph.v) or end not in range(0, graph.v):
        print("The start or end is out of the range.")
        return

    visited = [False for _ in range(0, graph.v)]
    visited[start] = True
    prev_vertices = [-1 for _ in range(0, graph.v)]
    queue = [start]

    while len(queue) != 0:
        vertex = queue.pop(0)
        p = graph.adj[vertex].next
        is_found = False
        
        while p is not None:
            adj_vertex = p.val
            
            if not visited[adj_vertex]:
                prev_vertices[adj_vertex] = vertex
                
                if adj_vertex == end:
                    show_path(prev_vertices, start, end)
                    is_found = True
                    break
                
                visited[adj_vertex] = True
                queue.append(adj_vertex)
            
            p = p.next
        
        if is_found:
            break
```

We suppose that `V` is the number of the vertices and `E` is the number of the edges.

The worst case is that **all the edges and vertrices** are visited. The time complexity is `O(V+E)`. If the graph is **connected** (all the vertices are connected), then `E > V - 1`. So, the time complexity can be simplified as `O(E)`.

The space complexity is `O(V)` because the length of both 2 assist array, `visited` and `prev_vertices`, is `V`.


### DFS

BFS will traverse **all the descendant vertices** before moving to the next **branch**.

It's similar to **InOrder traversing**, *(left -> mid -> right)*, of Binary Tree. So we need a **stack** to traverse the vertices. (Recursion also use a stack behind.)

So, we replace the `queue` in BFS by the `stack`, (`queue.pop(0)` is replaced by `stack.pop()`, too), then we have DFS.

Here, we use DFS to find a path in a graph in the recursive way.

> Attention: The place to updated `visited` array is different.

```python
is_found = False 

def dfs_recursive(graph: UndirectedGraph, start: int, end: int) -> None:
    if start not in range(0, graph.v) or end not in range(0, graph.v):
        print("The start or end is out of the range.")
        return

    visited = [False for _ in range(0, graph.v)]
    prev_vertices = [-1 for _ in range(0, graph.v)]

    dfs_worker(graph, start, end, visited, prev_vertices)
    show_path(prev_vertices, start, end)


def dfs_worker(graph: UndirectedGraph, start: int, end: int, visited: List[bool], prev_vertices: List[int]) -> None:
    global is_found

    if is_found:
        return
    if start == end:
        is_found = True
        return
    
    ## The following line can't be placed inside of while loop.
    ## Because the last function in recursion stack is first executed.
    ## Some function can be executed before the vertex is marked visited 
    ## if the following line is in the while loop.
    visited[start] = True
    
    p = graph.adj[start].next
    while p is not None:
        adj_vertex = p.val

        if not visited[adj_vertex]:
            prev_vertices[adj_vertex] = start
            dfs_worker(graph, adj_vertex, end, visited, prev_vertices)
        
        p = p.next
```

The worst case is that each **vertex** is visited **once**, and each **edge** is visited **twice** (forward and backward).

- Time complexity: `O(E)`
- Space complexity: `O(V)`


