from stacks_queues import ResizingArrayQueue

# Design pattern: Decouple graph data types from graph processing.

##########################
### Graph(Undirected). ###
##########################

class Graph:

    # Create an empty graph with nV vertices.
    def __init__(self, nV):
        # Number of vertices in the graph(size of the graph).
        self.nV = nV
        # Adjacency list.
        self.adjList = [[] for _ in range(nV)]

    # Add an edge v-w.
    def addEdge(self, v, w):
        self.adjList[v].append(w)
        self.adjList[w].append(v)

    # Return the number of vertices in the graph.
    def V(self):
        return len(self.adjList)

    # Return the number of edges in the graph.
    def E(self):
        return sum([len(i) for i in self.adjList]) // 2

    # Iterator for all vertices adjacent to v.
    def adj(self, v):
        return iter(self.adjList[v])

    # Return the degree of vertex v.
    def degree(self, v):
        return len(self.adjList[v])

    # Return the maximum degree of the graph.
    def maxDegree(self):
        maxDegree = 0
        for v in self.adjList:
            if self.degree(v) > maxDegree:
                maxDegree = self.degree(v)

        return maxDegree

    # Return the average degree of the graph.
    def averageDegree(self):
        # 2 * E() gives the sum of degrees of all vertices.
        return 2 * self.E() / self.V()

    # Return the number of self loops in the graph.
    # Implementation in slides probably wrong.
    def nSelfLoops(self):
        count = 0
        for v in range(len(self.adjList)):
            for w in v:
                if v == w:
                    count += 1

        return count


#############################
### Connected Components. ###
#############################

class ConnectedComponents:

    # Find connected components in the given graph.
    def __init__(self, graph):
        self.marked = [False] * graph.V()
        # ID of connected component each vertex belongs to (will be in range [0, nCC-1]).
        self.idCC = [None] * graph.V()
        self.nCC = 0 # Number of connected components.

        for v in range(graph.V()):
            if self.marked[v]:
                continue

            self.__depthFirstSearch(graph, v)
            self.nCC += 1

    # Return true if vertices v and w are connected.
    def connected(self, v, w):
        return self.idCC[v] == self.idCC[w]

    # Return the number of connected components in the graph.
    def count(self):
        return self.nCC

    def id(self, v):
        return self.idCC[v]

    ###
    ### HELPER FUNCTIONS
    ###
    def __depthFirstSearch(self, graph, v):
        self.marked[v] = True
        self.idCC[v] = self.nCC

        for w in graph.adj(v):
            if not self.marked[w]:
                self.__depthFirstSearch(graph, w)



