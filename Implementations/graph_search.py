##########################
### Depth-First Paths. ###
##########################

class DepthFirstPaths:

    # Find vertices connected to v.
    def __init__(self, graph, s):
        self.marked = [False] * graph.V()
        # edgeTo[w] == v means that edge v-w was taken to visit w for first time.
        self.edgeTo = [None] * graph.V()
        self.s = s

        self.__depthFirstSearch(graph, s)

    # Return true if there is a path from s to v.
    def hasPathTo(self, v):
        return self.marked[v]

    # Return the all the vertices on the path from s to v.
    # If no such path exists, return None.
    def pathTo(self, v):
        if not self.hasPathTo(v):
            return None

        path = []
        while v != self.s:
            path.append(v)
            v = self.edgeTo[v]
        path.append(self.s)

        return iter(path[::-1])

    ###
    ### HELPER FUNCTIONS
    ###
    def __depthFirstSearch(self, graph, v):
        self.marked[v] = True

        for w in graph.adj(v):
            if self.marked[w]:
                continue

            self.edgeTo[w]= v
            self.__depthFirstSearch(graph, w)


############################
### Breadth-First Paths. ###
############################

class BreadthFirstPaths:

    # Find the shortest paths from s to all vertices connected to s.
    def __init__(self, graph, s):
        # edgeTo[w] == v means that edge v-w was taken to visit w for first time.
        self.edgeTo = [None] * graph.V()
        # Distances(shortest as this is bfs) from vertices to s. None if not connected.
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

    # Return true if there is a path from s to v.
    def hasPathTo(self, v):
        return self.marked[v]

    # Return the all the vertices on the path from s to v.
    # If no such path exists, return None.
    def pathTo(self, v):
        if not self.hasPathTo(v):
            return None

        path = []
        while v != self.s:
            path.append(v)
            v = self.edgeTo[v]
        path.append(self.s)

        return iter(path[::-1])

