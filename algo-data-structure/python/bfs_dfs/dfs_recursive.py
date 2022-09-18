import sys
from typing import List

sys.path.append('..')
from bfs_dfs.UndirectedGraph import UndirectedGraph


is_found = False 

def dfs_recursive(graph: UndirectedGraph, start: int, end: int) -> None:
    if start == end:
        print("The start is equal to the end.")
        return
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

    visited[start] = True
    
    p = graph.adj[start].next
    while p is not None:
        adj_vertex = p.val

        if not visited[adj_vertex]:
            prev_vertices[adj_vertex] = start
            dfs_worker(graph, adj_vertex, end, visited, prev_vertices)
        
        p = p.next

def show_path(prev_vertices: List[int], start: int, end: int) -> str:
    print(end)
    if prev_vertices[end] != -1 and start != end:
        show_path(prev_vertices, start, prev_vertices[end])


if __name__ == "__main__":
    graph = UndirectedGraph(8)
    graph.addEdge(0, 1)
    graph.addEdge(0, 3)
    graph.addEdge(1, 2)
    graph.addEdge(1, 4)
    graph.addEdge(2, 5)
    graph.addEdge(3, 4)
    graph.addEdge(4, 5)
    graph.addEdge(4, 6)
    graph.addEdge(5, 7)
    graph.addEdge(6, 7)
    print(graph)

    dfs_recursive(graph, 0, 7)
