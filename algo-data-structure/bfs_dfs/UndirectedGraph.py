class LinkedNode:
    def __init__(self, val) -> None:
        self.val = val
        self.next = None

class UndirectedGraph:
    def __init__(self, v: int) -> None:
        """
        - v: number of the vertices
        - adj: Adjacency List
        """
        self.v = v
        self.adj = {}
        for i in range(0, v):
            self.adj[i] = LinkedNode(None)
    
    def __str__(self) -> str:
        s = "\n=== non-oriented graph ===\n"
        s += "v = {}\n".format(self.v)
        s += "adj = \n"
        for node in range(0, self.v):
            p = self.adj[node].next
            s += str(node) + " => ";
            while p is not None:
                s += str(p.val) + ", "
                p = p.next
            s += "\n"
        s += "=== end ===\n"
        return s

    def addNode(self, s: int, t: int):
        """
        add t into self.adj[s]
        """
        p = self.adj[s]
        while p.next is not None:
            p = p.next
        p.next = LinkedNode(t)
    
    def addEdge(self, s: int, t: int)->None:
        """
        add the edge between s and t
        """
        self.addNode(s, t)
        self.addNode(t, s)