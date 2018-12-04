###########################
### Binary Search Tree. ###
###########################

class BinarySearchTree:

    # A Binary Search Tree is a reference to a root Node.
    root = None

    class _Node:
        left, right = None, None

        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.count = 1

    # Return the size of the tree.
    def size(self):
        return self.__size(self.root)

    # Associate value with key.
    def put(self, key, value):
        if (key == None):
            raise TypeError('Cannot put key of type None.')

        self.root = self.__put(self.root, key, value)

    # Return value corresponding to given key, or None if no such key.
    def get(self, key):
        if (key == None):
            raise TypeError('Cannot search for key of type None.')

        node = self.root

        while (node != None):
            if key < node.key:
                node = node.left
            elif key > node.key:
                node = node.right
            else:
                return node.value

        return None

    # Delete the value, key pair associated with the given key.
    def delete(self, key):
        if (key == None):
            raise TypeError('Cannot delete key of type None.')

        self.root = self.__delete(self.root, key)

    # Delete the value, key pair associated with the smallest key from the tree.
    def deleteMin(self):
        self.root = self.__deleteMin(self.root)

    # Return the largest key in the tree less than or equal to given key.
    def floor(self, key):
        if (key == None):
            raise TypeError('Cannot return floor for key of type None.')

        node = self.__floor(self.root, key)

        if node == None:
            return None
        return node.key

    # The number of keys in the tree less than the given key.
    def rank(self, key):
        if (key == None):
            raise TypeError('Cannot return rank for key of type None.')

        return self.__rank(key, self.root)

    # Return the node with the smallest key.
    def min(self):
        return self.__min(self.root)

    # Inorder iterator for the binary search tree.
    def __iter__(self):
        self.inorder = []
        self.__inorder(self.root, self.inorder)
        return iter(self.inorder)

    """
    HELPER FUNCTIONS
    """
    def __size(self, node):
        if node == None:
            return 0
        return node.count

    def __put(self, node, key, value):
        if node == None:
            return self._Node(key, value)

        if key < node.key:
            node.left = self.__put(node.left, key, value)
        elif key > node.key:
            node.right = self.__put(node.right, key, value)
        else:
            node.value = value

        node.count = 1 + self.__size(node.left) + self.__size(node.right)

        return node

    def __floor(self, node, key):
        if node == None:
            return None

        if key < node.key:
            return self.__floor(node.left, key)
        elif key > node.key:
            temp = self.__floor(node.right, key)
            if temp != None:
                return temp
            return node
        else:
            return node

    def __rank(self, key, node):
        if node == None:
            return 0

        if key < node.key:
            return self.__rank(key, node.left)
        elif key > node.key:
            return self.__size(node.left) + 1 + self.__rank(key, node.right)
        else:
            return self.__size(node.left)

    def __inorder(self, node, inorder):
        if node == None:
            return

        self.__inorder(node.left, inorder)
        inorder.append(node.key)
        self.__inorder(node.right, inorder)

    def __deleteMin(self, node):
        if node == None:
            return None
        if node.left == None:
            return node.right

        node.left = self.__deleteMin(node.left)
        node.count = self.__size(node.left) + 1 + self.__size(node.right)

        return node

    def __delete(self, node, key):
        if node == None:
            return None

        if key < node.key:
            node.left = self.__delete(node.left, key)
        elif key > node.key:
            node.right = self.__delete(node.right, key)

        else:
            if node.right == None:
                return node.left
            if node.left == None:
                return node.right

            temp = node
            node = self.__min(temp.right)
            node.right = self.__deleteMin(temp.right)
            node.left = temp.left

        node.count = self.__size(node.left) + 1 + self.__size(node.right)
        return node

    def __min(self, node):
        if node == None:
            return None

        if node.left == None:
            return node

        return self.__min(node.left)

