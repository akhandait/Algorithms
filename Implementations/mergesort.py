import time
import random
from elementary_sorts import Insertion

##################
### Mergesort. ###
##################

class Merge:

    # Sort the given array.
    def sort(self, array):
        aux = [None] * len(array)
        low = 0
        high = len(array) - 1

        self.__sort(array, aux, 0, len(array) - 1)

    """
    HELPER FUNCTIONS
    """
    def __merge(self, a, aux, low, mid, high):
        for i in range(low, high + 1):
            aux[i] = a[i]

        j = low
        k = mid + 1

        for i in range(low, high + 1):
            if j > mid:
                a[i] = aux[k]
                k += 1
            elif k > high:
                a[i] = aux[j]
                j += 1
            elif aux[k] < aux[j]:
                a[i] = aux[k]
                k += 1
            else:
                a[i] = aux[j]
                j += 1

        assert all(a[i] <= a[i+1] for i in range(low, high))

    def __sort(self, a, aux, low, high):
        # if high <= low:
        #     return

        # Practical improvement: Use insertion sort for small subarrays.
        self.insertion = Insertion()
        cutoff = 7
        if high - low + 1 <= cutoff:
            self.insertion.sortLH(a, low, high)
            return

        mid = low + (high - low) // 2
        self.__sort(a, aux, low, mid)
        self.__sort(a, aux, mid + 1, high)

        # Practical improvement: Stop if already sorted.
        if a[mid] < a[mid + 1]:
            return

        self.__merge(a, aux, low, low + (high - low) // 2, high)

# Experiments to check time complexity.
if __name__ == "__main__":

    M = Merge()
    array = random.sample(range(0, 1000000), 400000)
    startTime = time.time()
    M.sort(array)
    print("Time taken to sort 400000 numbers -> " + str(time.time() - startTime) +
        " seconds")

    array = random.sample(range(0, 1000000), 800000)
    startTime = time.time()
    M.sort(array) # This will take ~2 times longer.(Linearithmic)
    print("Time taken to sort 800000 numbers -> " + str(time.time() - startTime) +
        " seconds")

############################
### Bottom-up Mergesort. ###
############################

class MergeBU(Merge):

    # Sort the given array.
    def sort(self, array):
        l = len(array)
        aux = [None] * l
        i = 1
        while True:
            for j in range(0, l, i * 2):
                self._Merge__merge(array, aux, j, j + i - 1,
                    min(j + 2 * i - 1, l - 1))

            i *= 2
            if i >= l:
                break

# Experiments to check time complexity.
if __name__ == "__main__":

    Mb = MergeBU()
    array = random.sample(range(0, 1000000), 400000)
    startTime = time.time()
    Mb.sort(array)
    print("Time taken to sort 400000 numbers -> " + str(time.time() - startTime) +
        " seconds")

    array = random.sample(range(0, 1000000), 800000)
    startTime = time.time()
    Mb.sort(array) # This will take ~2 times longer.(Linearithmic)
    print("Time taken to sort 800000 numbers -> " + str(time.time() - startTime) +
        " seconds")
