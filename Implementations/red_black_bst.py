from binary_search_tree import BinarySearchTree

##################################################
### Left Leaning Red Black Binary Search Tree. ###
##################################################

class LLRedBlackBST(BinarySearchTree):

    # A BST is a reference to a root Node.
    root = None

    # Colors of the parent links.
    RED = True
    BLACK = False

    class _Node:
        left, right = None, None
        color = None

        def __init__(self, key, value, color):
            self.key = key
            self.value = value
            self.color = color
            self.count = 1

    # Associate value with key.
    def put(self, key, value):
        if (key == None):
            raise TypeError('Cannot put key of type None.')

        self.root = self.__put(self.root, key, value)

    """
    Following functions from the BinarySearchTree class need no change:

    1) size()       -> Return the size of the tree.
    2) get(key)     -> Return value corresponding to given key, or None if no
                       such key.
    3) delete(key)  -> Delete the value, key pair associated with the given key.
    4) deleteMin()  -> Delete the value, key pair associated with the smallest
                       key from the tree.
    5) floor()      -> Return the largest key in the tree less than or equal to
                       given key.
    6) rank()       -> The number of keys in the tree less than the given key.
    7) min()        -> Return the node with the smallest key.
    8) rangeSearch()-> Return list of keys between low and high(1d range
                       search).
    9) __iter__()   -> Inorder iterator for the binary search tree.
    """

    ###
    ### HELPER FUNCTIONS
    ###
    # True if the link to a node is red.
    def __isRed(self, node):
        if node == None:
            return False
        return node.color == self.RED

    # Left rotation.
    # Orient a (temporarily) right-leaning red link to lean left.
    def __rotateLeft(self, h):
        assert (self.__isRed(h.right))

        x = h.right
        h.right = x.left
        x.left = h
        x.color = h.color
        h.color = self.RED
        h.count -= 1 + self._BinarySearchTree__size(x.right)
        x.count += 1 + self._BinarySearchTree__size(h.left)

        return x

    # Right rotation.
    # Orient a left-leaning red link to (temporarily) lean right.
    def __rotateRight(self, h):
        assert (self.__isRed(h.left))

        x = h.left
        h.left = x.right
        x.right = h
        x.color = h.color
        h.color = self.RED
        h.count -= 1 + self._BinarySearchTree__size(x.left)
        x.count += 1 + self._BinarySearchTree__size(h.right)

        return x

    # Color flip.
    # Recolor to split a (temporary) 4-node.
    def __flipColors(self, h):
        assert (self.__isRed(h.left))
        assert (self.__isRed(h.right))
        # assert (not self.__isRed(h))

        h.left.color = self.BLACK
        h.right.color = self.BLACK
        h.color = self.RED

        return h

    def __put(self, node, key, value):
        if node == None:
            if self.root == None:
                return self._Node(key, value, self.BLACK)
            return self._Node(key, value, self.RED)

        if key < node.key:
            node.left = self.__put(node.left, key, value)
        elif key > node.key:
            node.right = self.__put(node.right, key, value)
        else:
            node.value = value

        node.count = 1 + self._BinarySearchTree__size(node.left) + \
            self._BinarySearchTree__size(node.right)

        if self.__isRed(node.right) and not self.__isRed(node.left):
            node = self.__rotateLeft(node)
        if self.__isRed(node.left) and self.__isRed(node.left.left):
            node = self.__rotateRight(node)
        if self.__isRed(node.left) and self.__isRed(node.right):
            node = self.__flipColors(node)

        return node

