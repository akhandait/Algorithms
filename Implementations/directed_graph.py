from undirected_graph import Graph

# Design pattern: Decouple graph data types from graph processing.

########################
### Graph(Directed). ###
########################

class Digraph():

    # Create an empty graph with nV vertices.
    def __init__(self, nV):
        # Number of vertices in the graph(size of the graph).
        self.nV = nV
        # Adjacency list.
        self.adjList = [[] for _ in range(nV)]

    # Add a directed edge v-w.
    def addEdge(self, v, w):
        self.adjList[v].append(w)

    # Return the number of vertices in the graph.
    def V(self):
        return len(self.adjList)

    # Return the number of edges in the graph.
    def E(self):
        return sum([len(i) for i in self.adjList])

    # Return the reverse of this directed graph.
    def reverse(self):
        reverseGraph = Digraph(self.V())

        for v in range(self.V()):
            for w in self.adjList[v]:
                reverseGraph.addEdge(w, v)

        return reverseGraph

    # Iterator for all vertices pointing from v.
    def adj(self, v):
        return iter(self.adjList[v])

    # Return the outdegree of vertex v.
    def outDegree(self, v):
        return len(self.adjList[v])

    # Return the indegree of vertex v.
    def inDegree(self, v)
        count = 0
        for w in self.adjList:
            count += w.count(v)

    # Return the number of self loops in the graph.
    def nSelfLoops(self):
        count = 0
        for v in range(len(self.adjList)):
            for w in v:
                if v == w:
                    count += 1

        return count


#################################
### Depth-first search order. ###
#################################

class DepthFirstOrder:

    # Topological sort -> All edges point upwards.
    def __init__(self, digraph):
        self.marked = [False] * digraph.V()
        self.postOrder = [] # Reverse of topological order.

        for v in range(digraph.V()):
            if not self.marked[v]:
                self.__depthFirstSearch(digraph, v)

    # Return all vertices in reverse DFS postorder(topological order).
    def reversePost(self):
        return self.postOrder[::-1]

    ###
    ### HELPER FUNCTIONS
    ###
    def __depthFirstSearch(self, digraph, v):
        self.marked[v] = True

        for w in digraph.adj(v):
            if not self.marked[w]:
                self.__depthFirstSearch(digraph, w)

        self.postOrder.append(v)

######################################################
### Kosaraju-Sharir Strongly Connected Components. ###
######################################################

class StronglyCC:

    # Find strongly connected components in the given directed graph.
    # Kosaraju-Sharir algorithm used.
    def __init__(self, digraph):
        self.marked = [False] * digraph.V()
        # ID of strongly connected component each vertex belongs to (will be in range[0, nCC-1]).
        self.idStronglyCC = [None] * digraph.V()
        self.nStronglyCC = 0 # Number of strongly connected components.

        depthFirstOrder = DepthFirstOrder(digraph.reverse())

        for v in depthFirstOrder.reversePost():
            if self.marked[v]:
                continue

            self.__depthFirstSearch(digraph, v)
            self.nStronglyCC += 1

    # Return true if vertices v and w are strongly connected.
    def stronglyConnected(self, v, w):
        return self.idStronglyCC[v] == self.idStronglyCC[w]

    # Return the number of strongly connected components in the graph.
    def count(self):
        return self.nStronglyCC

    def id(self, v):
        return self.idStronglyCC[v]

    ###
    ### HELPER FUNCTIONS
    ###
    def __depthFirstSearch(self, digraph, v):
        self.marked[v] = True
        self.idStronglyCC[v] = self.nStronglyCC

        for w in digraph.adj(v):
            if not self.marked[w]:
                self.__depthFirstSearch(digraph, w)

