import time
from random import randint

# These data structures are also called disjoint sets.

##############################
### Quick Find Union Find. ###
##############################

class QuickFindUF:

    # Initialize union-find data structure with N objects (0 to N – 1).
    def __init__(self, N):
        self.id = [0] * N
        for i in range(N):
            self.id[i] = i

    # Return true if p and q are in the same component.
    def connected(self, p, q):
        if (p not in range(len(self.id)) or q not in range(len(self.id))):
            raise IndexError('p and q should be in range [0, N)')

        return self.id[p] == self.id[q]

    # Add connection between p and q.
    def union(self, p, q):
        if (p not in range(len(self.id)) or q not in range(len(self.id))):
            raise IndexError('p and q should be in range [0, N)')

        pid = self.id[p]
        qid = self.id[q]
        for i in range(len(self.id)):
            if (self.id[i] == pid):
                self.id[i] = qid

# Experiments to check time complexity.
if __name__ == "__main__":

    qf = QuickFindUF(500)

    start_time = time.time()
    for i in range(500):
        i1 = randint(0, 499)
        i2 = randint(0, 499)
        qf.union(i1, i2)
    print("Quick-find 500 takes %s seconds" % (time.time() - start_time))

    # The following will take ~4 times longer.
    qf = QuickFindUF(1000)

    start_time = time.time()
    for i in range(1000):
        i1 = randint(0, 999)
        i2 = randint(0, 999)
        qf.union(i1, i2)
    print("Quick-find 1000 takes %s seconds" % (time.time() - start_time))


###############################
### Quick Union Union Find. ###
###############################

class QuickUnionUF:

    # Initialize union-find data structure with N objects (0 to N – 1).
    def __init__(self, N):
        self.id = [0] * N
        for i in range(N):
            self.id[i] = i

    # Returns the depth of a node from its root.
    # Used for analysis here, it's not in the slides.
    def depth(self, i):
        c = 0
        while (i != self.id[i]):
            i = self.id[i]
            c += 1
        return c

    # Return true if p and q are in the same component.
    def connected(self, p, q):
        if (p not in range(len(self.id)) or q not in range(len(self.id))):
            raise IndexError('p and q should be in range [0, N)')

        return self.__root(p) == self.__root(q)

    # Add connection between p and q.
    def union(self, p , q):
        if (p not in range(len(self.id)) or q not in range(len(self.id))):
            raise IndexError('p and q should be in range [0, N)')

        i = self.__root(p)
        j = self.__root(q)
        self.id[i] = j

    """
    HELPER FUNCTIONS
    """
    def __root(self, i):
        while (i != self.id[i]):
            i = self.id[i]
        return i

# Experiments to check time complexity.
if __name__ == "__main__":

    qu = QuickUnionUF(5000)

    start_time = time.time()
    for i in range(5000):
        i1 = randint(0, 4999)
        i2 = randint(0, 4999)
        qu.union(i1, i2)

    print("Quick-union 5000 takes %s seconds" % (time.time() - start_time))

    a = [None] * 5000
    for i in range(5000):
        a[i] = qu.depth(i)
    print("Maximum depth -> " + str(max(a)))
    print("Average depth -> " + str(sum(a) / len(a)))

    # The following will take ~4 times longer in the worst case.
    qu = QuickUnionUF(10000)

    start_time = time.time()
    for i in range(10000):
        i1 = randint(0, 9999)
        i2 = randint(0, 9999)
        qu.union(i1, i2)

    print("Quick-union 10000 takes %s seconds" % (time.time() - start_time))


########################################
### Weighted Quick Union Union Find. ###
########################################

class WeightedQuickUnionUF(QuickUnionUF):

    # Initialize union-find data structure with N objects (0 to N – 1).
    def __init__(self, N):
        self.id = [0] * N
        for i in range(N):
            self.id[i] = i
        self.sz = [1] * N

    # Add connection between p and q.
    def union(self, p , q):
        if (p not in range(len(self.id)) or q not in range(len(self.id))):
            raise IndexError('p and q should be in range [0, N)')

        i = self._QuickUnionUF__root(p)
        j = self._QuickUnionUF__root(q)
        if (i == j):
            return

        if (self.sz[i] < self.sz[j]):
            self.id[i] = j
            self.sz[j] += self.sz[i]
        else:
            self.id[j] = i
            self.sz[i] += self.sz[j]

# Experiments to check time complexity.
if __name__ == "__main__":

    wqu = WeightedQuickUnionUF(5000)

    start_time = time.time()
    for i in range(5000):
        i1 = randint(0, 4999)
        i2 = randint(0, 4999)
        wqu.union(i1, i2)

    print("Weighted quick-union 5000 takes %s seconds" % (time.time() - start_time))

    a = [None] * 5000
    for i in range(5000):
        a[i] = wqu.depth(i)
    print("Maximum depth -> " + str(max(a)))
    print("Average depth -> " + str(sum(a) / len(a)))

    # The following will take ~2 times longer. (Linearithmic)
    wqu = WeightedQuickUnionUF(10000)

    start_time = time.time()
    for i in range(10000):
        i1 = randint(0, 9999)
        i2 = randint(0, 9999)
        wqu.union(i1, i2)

    print("Weighted quick-union 10000 takes %s seconds" % (time.time() - start_time))


#########################################################
### Weighted Quick Union Path Compression Union Find. ###
#########################################################

class WeightedQuickUnionPCUF(WeightedQuickUnionUF):

    # Add connection between p and q.
    def union(self, p , q):
        if (p not in range(len(self.id)) or q not in range(len(self.id))):
            raise IndexError('p and q should be in range [0, N)')

        i = self._QuickUnionUF__root(p)
        j = self._QuickUnionUF__root(q)
        if (i == j):
            return

        if (self.sz[i] < self.sz[j]):
            self.id[i] = j
            self.sz[j] += self.sz[i]
        else:
            self.id[j] = i
            self.sz[i] += self.sz[j]

# Experiments to check time complexity.
if __name__ == "__main__":

    wqupc = WeightedQuickUnionPCUF(5000)

    start_time = time.time()
    for i in range(5000):
        i1 = randint(0, 4999)
        i2 = randint(0, 4999)
        wqupc.union(i1, i2)

    print("Weighted quick-union with path compression 5000 takes %s seconds"
        % (time.time() - start_time))

    a = [None] * 5000
    for i in range(5000):
        a[i] = wqupc.depth(i)
    print("Maximum depth -> " + str(max(a)))
    print("Average depth -> " + str(sum(a) / len(a)))

    wqupc = WeightedQuickUnionPCUF(10000)

    start_time = time.time()
    for i in range(10000):
        i1 = randint(0, 9999)
        i2 = randint(0, 9999)
        wqupc.union(i1, i2)

    print("Weighted quick-union with path compression 10000 takes %s seconds"
        % (time.time() - start_time))
