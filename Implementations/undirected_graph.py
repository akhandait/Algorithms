from stacks_queues import ResizingArrayQueue

##########################
### Graph(Undirected). ###
##########################

class Graph:

    # Creat an empty graph with nV vertices.
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

    # Return the degree of v.
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



class DepthFirstPaths:

    def __init__(self, graph, v):
        self.marked = [False] * graph.V()
        self.edgeTo = [None] * graph.V()
        self.s = v

        self.__depthFirstSearch(graph, v)


    def __depthFirstSearch(self, graph, v):
        self.marked[v] = True

        for w in graph.adj(v):
            if self.marked[w]:
                continue

            self.edgeTo[w]= v
            self.__depthFirstSearch(graph, w)

    def hasPathTo(self, v):
        return self.marked[v]

    def pathTo(self, v):
        if not self.hasPathTo(v):
            return None

        path = []
        while v != self.s:
            path.append(v)
            v = self.edgeTo[v]
        path.append(self.s)

        return iter(path[::-1])


class BreadthFirstPaths:

    def __init__(self, graph, v):
        self.edgeTo = [None] * graph.V()
        self.dist = [None] * graph.V()
        self.marked = [False] * graph.V()
        self.queue = ResizingArrayQueue()
        self.s = v

        self.queue.enqueue(v)
        self.marked[v] = True
        self.dist[v] = 0

        while not self.queue.isEmpty():
            w = self.queue.dequeue()
            for q in graph.adj(w):
                if self.marked[q]:
                    continue

                self.queue.enqueue(q)
                self.marked[q] = True
                self.dist[q] = self.dist[w] + 1
                self.edgeTo[q] = w


class CC:

    def __init__(self, graph):
        self.marked = [False] * graph.V()
        self.ccId = [None] * graph.V()
        self.c = 0

        for v in range(graph.V()):
            if self.marked[v]:
                continue

            self.__depthFirstSearch(graph, v)
            self.c += 1

    def __depthFirstSearch(self, graph, v):
        self.marked[v] = True
        self.ccId[v] = self.c

        for w in graph.adj(v):
            if not self.marked[w]:
                self.__depthFirstSearch(graph, w)

    def connected(self, v, w):
        return self.ccId[v] == self.ccId[w]

    def count(self):
        return self.c

# graph = Graph(13)
# graph.addEdge(0, 5)
# graph.addEdge(5, 3)
# graph.addEdge(3, 4)
# graph.addEdge(5, 4)
# graph.addEdge(6, 4)
# graph.addEdge(0, 6)
# graph.addEdge(0, 2)
# graph.addEdge(1, 0)
# graph.addEdge(7, 8)
# graph.addEdge(9, 10)
# graph.addEdge(9, 11)
# graph.addEdge(12, 11)
# graph.addEdge(9, 12)

# cc = CC(graph)

# for Id in cc.ccId:
#     print(Id)

# print('\n' + str(cc.count()))
# print('\n' + str(cc.connected(0, 6)))



