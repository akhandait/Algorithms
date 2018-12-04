import time
import random

###########################################
### Unordered Array Max Priority Queue. ###
###########################################

class UnorderedMaxPQ:

    # NOTE: The append() function not used to practise resizing array
    #       implementation.

    pq = [None] * 2 # (Resizing)Array of the priority queue.
    N = 0 # Size.

    # Return true if the priority queue is empty.
    def isEmpty(self):
        return self.N == 0

    # Insert a key into the priority queue.
    def insert(self, key):
        if (key == None):
            raise TypeError('Cannot insert item of type None.')

        if self.N == len(self.pq):
            self.__resize(2 * self.N)

        self.pq[self.N] = key
        self.N += 1

    # Return and remove the largest key.
    def delMax(self):
        if self.isEmpty():
            raise RuntimeError('Cannot delete from empty priority queue')

        m = 0
        for i in range(self.N):
            if self.pq[i] > self.pq[m]:
                m = i
        self.__exchange(m, self.N - 1)

        m = self.pq[self.N - 1]
        self.pq[self.N - 1] = None
        self.N -= 1

        if (self.N > 0 and self.N == len(self.pq) // 4):
            self.__resize(len(self.pq) // 2)

        return m

    """
    HELPER FUNCTIONS
    """
    def __resize(self, capacity):
        temp = [None] * capacity
        for i in range(self.N):
            temp[i] = self.pq[i]
        self.pq = temp

    def __exchange(self, a, b):
        temp = self.pq[a]
        self.pq[a] = self.pq[b]
        self.pq[b] = temp

# Experiments to check time complexity.
if __name__ == "__main__":

    M = UnorderedMaxPQ()
    for i in range(100000):
        M.insert(random.randint(0, 1000000))

    startTime = time.time()
    M.delMax()
    print('Time taken to delete max from 100000 elements: ' + str(time.time() -
        startTime) + 'seconds')

    for i in range(100001):
        M.insert(random.randint(0, 1000000))

    startTime = time.time()
    M.delMax()
    print('Time taken to delete max from 200000 elements: ' + str(time.time() -
        startTime) + 'seconds')

#######################################
### Binary Heap Max Priority Queue. ###
#######################################

class MaxPQ(UnorderedMaxPQ):

    pq = [None] * 3 # (Resizing)Array of the priority queue.
    N = 0 # Size.

    # Insert a key into the priority queue.
    def insert(self, key):
        if (key == None):
            raise TypeError('Cannot insert item of type None.')

        if self.N == len(self.pq) - 1:
            self.__resize(2 * (self.N + 1))

        self.N += 1
        self.pq[self.N] = key
        self.__swim(self.N)

    # Return and remove the largest key.
    def delMax(self):
        if self.N == 0:
            raise RuntimeError('Cannot delete from empty priority queue.')

        self._UnorderedMaxPQ__exchange(1, self.N)
        m = self.pq[self.N]
        self.pq[self.N] = None
        self.N -= 1
        self.__sink(1)

        if (self.N > 0 and self.N + 1 == len(self.pq) // 4):
            self.__resize(len(self.pq) // 2)

        return m

    """
    HELPER FUNCTIONS
    """
    def __swim(self, k):
        while (k > 1 and self.pq[k // 2] < self.pq[k]):
            self._UnorderedMaxPQ__exchange(k, k // 2)
            k //= 2

    def __resize(self, capacity):
        temp = [None] * capacity
        for i in range(self.N + 1):
            temp[i] = self.pq[i]
        self.pq = temp

    def __sink(self, k):
        while (k <= self.N // 2):
            temp = 2 * k
            if temp < self.N and self.pq[temp + 1] > self.pq[temp]:
                temp += 1

            if self.pq[k] > self.pq[temp]:
                break

            self._UnorderedMaxPQ__exchange(temp, k)
            k = temp

# Experiments to check time complexity.
if __name__ == "__main__":

    M = MaxPQ()
    for i in range(100000):
        M.insert(random.randint(0, 1000000))

    startTime = time.time()
    M.delMax()
    print('Time taken to delete max from 100000 elements: ' + str(time.time() -
        startTime) + 'seconds')

    for i in range(100001):
        M.insert(random.randint(0, 1000000))

    startTime = time.time()
    M.delMax()
    print('Time taken to delete max from 200000 elements: ' + str(time.time() -
        startTime) + 'seconds')
