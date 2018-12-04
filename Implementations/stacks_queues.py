import time
from sys import getsizeof

# Python uses duck typing, so it doesn't need special syntax to handle multiple
# types.
# So, here we define a class LinkedStack instead of LinkedStackOfStrings.
# Same is followed for all other classes.

##########################
### Linked List Stack. ###
##########################

class LinkedStack:

    firstNode = None

    class _Node:
        item, nextNode = None, None

    # Return true if the stack is empty.
    def isEmpty(self):
        return self.firstNode == None

    # Insert a new item onto stack.
    def push(self, item):
        if (item == None):
            raise TypeError('Cannot push item of type None.')

        oldFirstNode = self.firstNode
        self.firstNode = self._Node()
        self.firstNode.item = item
        self.firstNode.nextNode = oldFirstNode

    # Return and remove the most recently added item.
    def pop(self):
        if (self.isEmpty()):
            raise RuntimeError('Cannot pop from empty stack.')

        item = self.firstNode.item
        self.firstNode = self.firstNode.nextNode

        return item

#############################
### Resizing Array Stack. ###
#############################

class ResizingArrayStack:

    # NOTE: The append() function not used to practise resizing array
    #       implementation.

    array = [None] # (Resizing)Array of the stack.
    size = 0 # Size.

    # Return true if the stack is empty.
    def isEmpty(self):
        return self.size == 0

    # Insert a new item onto stack.
    def push(self, item):
        if (item == None):
            raise TypeError('Cannot push item of type None.')

        if (self.size == len(self.array)):
            self.__resize(2 * self.size)

        self.array[self.size] = item
        self.size += 1

    # Return and remove the most recently added item.
    def pop(self):
        if (self.isEmpty()):
            raise RuntimeError('Cannot pop from empty stack.')

        self.size -= 1
        item = self.array[self.size]
        self.array[self.size] = None

        if (self.size > 0 and self.size == len(self.array) // 4):
            self.__resize(len(self.array) // 2)

        return item

    """
    HELPER FUNCTIONS
    """
    def __resize(self, capacity):
        copy = [None] * capacity
        for i in range(self.size):
            copy[i] = self.array[i]
        self.array = copy

##########################
### Linked List Queue. ###
##########################

class LinkedQueue:

    firstNode, lastNode = None, None

    class _Node:
        item, nextNode = None, None

    # Return true if the queue is empty.
    def isEmpty(self):
        return self.firstNode == None

    # Insert a new item onto queue.
    def enqueue(self, item):
        if (item == None):
            raise TypeError('Cannot enqueue item of type None.')

        oldLastNode = self.lastNode
        self.lastNode = self._Node()
        self.lastNode.item = item
        self.lastNode.nextNode = None

        if (self.isEmpty()):
            self.firstNode = self.lastNode
        else:
            oldLastNode.nextNode = self.lastNode

    # Return and remove the least recently added item.
    def dequeue(self):
        if (self.isEmpty()):
            raise RuntimeError('Cannot dequeue from empty queue.')

        item = self.firstNode.item
        self.firstNode = self.firstNode.nextNode
        if (self.isEmpty()):
            self.lastNode = None
        return item

#############################
### Resizing Array Queue. ###
#############################

class ResizingArrayQueue:

    array = [None] * 2 # (Resizing)Array of the queue.
    size = 0 # Size.
    head = 0 # Index of the head.
    tail = 0 # Index of the tail.

    # Return true if the queue is empty.
    def isEmpty(self):
        return self.size == 0

    # Insert a new item onto queue.
    def enqueue(self, item):
        if (item == None):
            raise TypeError('Cannot enqueue item of type None.')

        if (self.size == len(self.array)):
            self.__resize(2 * self.size)

        self.array[self.tail] = item
        self.tail += 1

        if (self.tail == len(self.array)):
            self.tail = 0

        self.size += 1

    # Return and remove the least recently added item.
    def dequeue(self):
        if (self.isEmpty()):
            raise RuntimeError('Cannot dequeue from empty queue.')

        item = self.array[self.head]
        self.array[self.head] = None
        self.head += 1
        self.size -= 1

        if (self.head == len(self.array)):
            self.head = 0

        if (self.size > 0 and self.size == len(self.array) // 4):
            self.__resize(len(self.array) // 2)

        return item

    """
    HELPER FUNCTIONS
    """
    def __resize(self, capacity):
        assert capacity > self.size

        copy = [None] * capacity
        for i in range(self.size):
            copy[i] = self.array[(self.head + i) % len(self.array)]

        self.array = copy
        self.head = 0
        self.tail = self.size
