import time
import random
from elementary_sorts import Insertion

#################################
### Quicksort / Quick-Select. ###
#################################

class Quick:

    # Sort the given array.
    def sort(self, array):
        random.shuffle(array) # Shuffle needed for performance gaurantee.
        self.__sort(array, 0, len(array) - 1)

    # Return the kth smallest item from the given array.
    def select(self, array, k):
        random.shuffle(array) # Shuffle needed for performance gaurantee.
        low = 0
        high = len(array) - 1
        while (high > low):
            j = self.__partition(array, low, high)

            if k < j:
                high = j - 1
            elif k > j:
                low = j + 1
            else:
                return array[k]

    """
    HELPER FUNCTIONS
    """
    def __exchange(self, array, a, b):
        temp = array[a]
        array[a] = array[b]
        array[b] = temp

    def __partition(self, array, low, high):
        i = low
        j = high

        while True:
            while (array[i] < array[low]):
                i += 1
                if i == high:
                    break
            while (array[j] > array[low]):
                j -= 1
                if j == low:
                    break

            if i >= j:
                break

            self.__exchange(array, i, j)

            if i < high:
                i += 1
            if j > low:
                j -= 1

        self.__exchange(array, low, j)
        return j

    def __sort(self, array, low, high):
        if high <= low:
            return

        # Practical improvement: Use insertion sort for small subarrays.

        # self.insertion = Insertion()
        # cutoff = 7
        # if high - low + 1 <= cutoff:
        #     self.insertion.sortLH(array, low, high)
        #     return

        # This doesn't seem to work well, so commented out.
        # In case of mergesort, it does work well.

        j = self.__partition(array, low, high)
        self.__sort(array, low, j - 1)
        self.__sort(array, j + 1, high)

# Experiments to check time complexity.
if __name__ == "__main__":

    Q = Quick()
    array = random.sample(range(0, 1000000), 400000)
    startTime = time.time()
    Q.sort(array)
    assert all(array[i] <= array[i+1] for i in range(0, len(array) - 1))
    print("Time taken to sort 400000 numbers -> " + str(time.time() - startTime) +
        " seconds")

    array = random.sample(range(0, 1000000), 800000)
    startTime = time.time()
    Q.sort(array)
    assert all(array[i] <= array[i+1] for i in range(0, len(array) - 1))
    print("Time taken to sort 800000 numbers -> " + str(time.time() - startTime) +
        " seconds")

    # Selection.
    array = random.sample(range(0, 1000000), 400000)
    startTime = time.time()
    Q.select(array, 50000)
    print("Time taken -> " + str(time.time() - startTime) + " seconds")

    array = random.sample(range(0, 1000000), 800000)
    startTime = time.time()
    Q.select(array, 50000)
    print("Time taken -> " + str(time.time() - startTime) + " seconds")


#######################################################
### 3-way Quicksort.(Dijkstra's 3-way partitioning) ###
#######################################################

class QuickThreeWay(Quick):

    # Sort the given array.
    def sort(self, array):
        random.shuffle(array) # Shuffle needed for performance gaurantee.
        self.__sort(array, 0, len(array) - 1)

    """
    HELPER FUNCTIONS
    """
    def __sort(self, array, low, high):
        if high <= low:
            return

        i = low
        lt = low
        gt = high
        v = array[low]

        while i <= gt:
            if array[i] < v:
                self._Quick__exchange(array, lt, i)
                lt += 1
                i += 1
            elif array[i] > v:
                self._Quick__exchange(array, gt, i)
                gt -= 1
            else:
                i += 1

        self.__sort(array, low, lt - 1)
        self.__sort(array, gt + 1, high)

# Experiments to check time complexity.
if __name__ == "__main__":

    Qt = QuickThreeWay()
    array = random.sample(range(0, 1000000), 400000)
    startTime = time.time()
    Qt.sort(array)
    assert all(array[i] <= array[i+1] for i in range(0, len(array) - 1))
    print("Time taken to sort 400000 numbers -> " + str(time.time() - startTime) +
        " seconds")

    array = random.sample(range(0, 1000000), 800000)
    startTime = time.time()
    Qt.sort(array)
    assert all(array[i] <= array[i+1] for i in range(0, len(array) - 1))
    print("Time taken to sort 800000 numbers -> " + str(time.time() - startTime) +
        " seconds")
