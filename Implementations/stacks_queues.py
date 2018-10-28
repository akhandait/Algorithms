import time
from sys import getsizeof

# Python uses duck typing, so it doesn't need special syntax to
# handle multiple types.
# So, here we define a class LinkedStack instead of LinkedStackOfStrings.
# Same is followed for all other classes.
class LinkedStack:

    firstNode = None

    class Node:
        item, nextNode = None, None

    def isEmpty(self):
        return self.firstNode == None

    def push(self, item):
        if (item == None):
            raise ValueError('Cannot push item of type None.')

        oldFirstNode = self.firstNode
        self.firstNode = self.Node()
        self.firstNode.item = item
        self.firstNode.nextNode = oldFirstNode

    def pop(self):
        if (self.isEmpty()):
            raise ValueError('Cannot pop from empty stack.')

        item = self.firstNode.item
        self.firstNode = self.firstNode.nextNode

        return item

# l = LinkedStack()
# s = [0] * 20000
# for i in range(200000):
#     l.push(i)

# startTime = time.time()

# for i in range(20000):
#     st = time.time()
#     l.pop()
#     s[i] = time.time() - st
#     if (s[i] > 0.0010):
#         print(i)

# print("Time taken -> %s seconds" % (time.time() - startTime))
# print(max(s))
# print(getsizeof(l))


# Function append() not used in the following class.
# (What's the point otherwise?)
class ResizingArrayStack:

    array = [None]
    size = 0

    def isEmpty(self):
        return self.size == 0

    def push(self, item):
        if (item == None):
            raise ValueError('Cannot push item of type None.')

        if (self.size == len(self.array)):
            self.__resize(2 * self.size)

        self.array[self.size] = item
        self.size += 1

    def __resize(self, capacity):
        copy = [None] * capacity
        for i in range(self.size):
            copy[i] = self.array[i]
        self.array = copy

    def pop(self):
        if (self.isEmpty()):
            raise ValueError('Cannot pop from empty stack.')
        self.size -= 1
        item = self.array[self.size]
        self.array[self.size] = None
        if (self.size > 0 and self.size == len(self.array) / 4):
            self.__resize(len(self.array) // 2)
        return item

# p = ResizingArrayStack()
# s = [0] * 20000
# for i in range(20000):
#     p.push(i)

# startTime = time.time()

# for i in range(20000):
#     st = time.time()
#     p.pop()
#     s[i] = time.time() - st
#     if (s[i] > 0.00010):
#         print(i)

# print("Time taken -> %s seconds" % (time.time() - startTime))
# print(max(s))
# print(getsizeof(p.array))


class LinkedQueue:

    firstNode, lastNode = None, None

    class Node:
        item, nextNode = None, None

    def isEmpty(self):
        return self.firstNode == None

    def enqueue(self, item):
        if (item == None):
            raise ValueError('Cannot enqueue item of type None.')

        oldLastNode = self.lastNode
        self.lastNode = self.Node()
        self.lastNode.item = item
        self.lastNode.nextNode = None

        if (self.isEmpty()):
            self.firstNode = self.lastNode
        else:
            oldLastNode.nextNode = self.lastNode

    def dequeue(self):
        if (self.isEmpty()):
            raise ValueError('Cannot dequeue from empty queue.')

        item = self.firstNode.item
        self.firstNode = self.firstNode.nextNode
        if (self.isEmpty()):
            self.lastNode = None
        return item


class ResizingArrayQueue:

    array = [None] * 2
    size = 0
    head = 0
    tail = 0

    def isEmpty(self):
        return self.size == 0

    def __resize(self, capacity):
        assert capacity > self.size

        copy = [None] * capacity
        for i in range(self.size):
            copy[i] = self.array[(self.head + i) % len(self.array)]

        self.array = copy
        self.head = 0
        self.tail = self.size

    def enqueue(self, item):
        if (item == None):
            raise ValueError('Cannot enqueue item of type None.')

        if (self.size == len(self.array)):
            self.__resize(2 * self.size)

        self.array[self.tail] = item
        self.tail += 1

        if (self.tail == len(self.array)):
            self.tail = 0

        self.size += 1

    def dequeue(self):
        if (self.isEmpty()):
            raise ValueError('Cannot dequeue from empty queue.')

        item = self.array[self.head]
        self.array[self.head] = None
        self.head += 1
        self.size -= 1

        if (self.head == len(self.array)):
            self.head = 0

        if (self.size > 0 and self.size == len(self.array) // 4):
            self.__resize(len(self.array) // 2)

        return item
