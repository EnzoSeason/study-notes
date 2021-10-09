#  Graph

Graph is a **non-linear** data structure, like Tree.

There are concepts in the graph.

- **vertex**: The element in a graph

- **edge**: The connection between 2 vertices

- **degree** of a vertex: The number of edges owned by the vertex

If the edge has the **orientation**, than the graph is **directed graph**.

If the edge has the **weight**, than the graph is **weighted graph**.

# #  Stock a graph

# # #  Adjacency Matrix

Adjacency Matrix has 2 dimensions. `adj[i][j]` represents a edge **from vertex *i* to vertex *j***.

In a **undirected** graph, if there is an edge between vertex *i* and vertex *j* without the weight, then:

```python
adj[i][j] == 1 and adj[j][i] == 1
```

In a **weighted directed** graph, if the weight of the edge between from vertex *i* to vertex *j* is `3`, then:

```python
adj[i][j] == 3
```

Adjacency Matrix is based on the array, so **it's easy to do the calculation**. 

However, if a graph has a lot of vertices but few of edges, than the adjacency matrix becomes a **sparse matrix**. It **wastes space**.

# # #  Adjacency List

Since Adjacency Matrix can waste a lot of space, Adjacency List is created.

Adjacency List is simalar to the **hash table**. All the vertices are saved in the table. Each vertex has a **linked list**, stocking all the vertice it **pointes to**.

Adjacency List saves the space, but makes *search*, *insert* and *delete* more difficult. We can solve this problem by replacing **linked list** with **skip list**. 

This makes **Adjacency List approach Adjacency Matrix**. The more **indexes** in the skip list, the more **edges** is represented, the more **space** is used.

