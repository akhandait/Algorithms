#################################
### Linked List Symbol Table. ###
#################################

class LinkedST:

    firstNode = None
    N = 0 # Size of the symbol table.

    class _Node:
        def __init__(self, key, value, nextNode):
            self.key = key
            self.value = value
            self.nextNode = nextNode

    # Associate value with key.
    def put(self, key, value):
        if (key == None):
            raise TypeError('Cannot put key of type None.')

        node = self.__get(key)
        if node != None:
            node.value = value
            return

        oldFirstNode = self.firstNode
        self.firstNode = self._Node(key, value, oldFirstNode)
        self.N += 1

    # Return true if the symbol table is empty.
    def isEmpty(self):
        return self.firstNode == None

    # Return the size of the symbol table.
    def size(self):
        return self.N

    # Return value corresponding to given key, or None if no such key.
    def get(self, key):
        if (key == None):
            raise TypeError('Cannot search for key of type None.')

        node = self.__get(key)
        if node == None:
            return None

        return node.value

    # Return true if the symbol table has the given key.
    def contains(self, key):
        if (key == None):
            raise TypeError('Cannot search for key of type None.')

        return self.__get(key) != None

    # Delete the value, key pair associated with the given key.
    def delete(self, key):
        if self.isEmpty():
            raise RuntimeError('Cannot delete from empty symbol table.')

        if self.firstNode.key == key:
            oldFirstNode = self.firstNode
            self.firstNode = self.firstNode.nextNode
            oldFirstNode = None
            return

        currentNode = self.firstNode
        currentNextNode = self.firstNode.nextNode

        while (currentNextNode != None):
            if currentNextNode.key == key:
                currentNode.nextNode = currentNextNode.nextNode
                currentNextNode = None
                self.N -= 1
                return

            currentNode = currentNextNode
            currentNextNode = currentNextNode.nextNode

        raise RuntimeError('Key not in symbol table.')


    ###
    ### HELPER FUNCTIONS
    ###
    def __get(self, key):
        currentNode = self.firstNode

        while (currentNode != None):
            if currentNode.key == key:
                return currentNode
            currentNode = currentNode.nextNode

        return None


###################################
### Binary Search Symbol Table. ###
###################################

class BinarySearchST:

    # NOTE: The append() function not used to practise resizing array
    #       implementation.

    keys = [None] * 2 # (Resizing)Array of the keys.
    values = [None] * 2 # (Resizing)Array of the values(parallel to the keys).
    N = 0 # Size.

    # Associate value with key.
    def put(self, key, value):
        if (key == None):
            raise TypeError('Cannot put key of type None.')

        i = self.rank(key)

        if i < self.N and self.keys[i] == key:
            self.values[i] = value
            return

        if len(self.keys) == self.N:
            self.__resize(2 * self.N)

        for j in reversed(range(i + 1, self.N + 1)):
            self.keys[j] = self.keys[j - 1]
            self.values[j] = self.values[j - 1]

        self.keys[i] = key
        self.values[i] = value
        self.N += 1

    # Return true if the symbol table is empty.
    def isEmpty(self):
        return self.N == 0

    # Return the size of the symbol table.
    def size(self):
        return self.N

    # Return value corresponding to given key, or None if no such key.
    def get(self, key):
        if (key == None):
            raise TypeError('Cannot search for key of type None.')

        if self.isEmpty():
            return None

        i = self.rank(key)
        if i < self.N and self.keys[i] == key:
            return self.values[i]

        return None

    # Return true if the symbol table has the given key.
    def contains(self, key):
        if (key == None):
            raise TypeError('Cannot search for key of type None.')

        return self.get(key) != None

    # Delete the value, key pair associated with the given key.
    def delete(self, key):
        if self.isEmpty():
            raise RuntimeError('Cannot delete from empty symbol table.')

        i = self.rank(key)
        if self.keys[i] != key:
            raise RuntimeError('Key not in symbol table.')

        for j in range(i, self.N - 1):
            self.keys[j] = self.keys[j + 1]
            self.values[j] = self.values[j + 1]

        self.keys[self.N - 1] = None
        self.values[self.N - 1] = None
        self.N -= 1

        if self.N == len(self.keys) // 4:
            self.__resize(len(self.keys) // 2)

    # The number of keys in the tree less than the given key.
    def rank(self, key):
        if (key == None):
            raise TypeError('Cannot return rank for key of type None.')

        low = 0
        high = self.N - 1

        while (high >= low):
            mid = low + (high - low) // 2

            if key > self.keys[mid]:
                low = mid + 1
            elif key < self.keys[mid]:
                high = mid - 1
            else:
                return mid

        return low

    ###
    ### HELPER FUNCTIONS
    ###
    def __resize(self, capacity):
        keysCopy = [None] * capacity
        valuesCopy = [None] * capacity

        for i in range(self.N):
            keysCopy[i] = self.keys[i]
            valuesCopy[i] = self.values[i]

        self.keys = keysCopy
        self.values = valuesCopy


