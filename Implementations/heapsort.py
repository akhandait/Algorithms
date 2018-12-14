import time
import random

#################
### Heapsort. ###
#################

class Heap:

    # Sort the given array.
    def sort(self, array):
        n = len(array)

        # Heap formation.
        for i in reversed(range(1, n // 2 + 1)):
            self.__sink(array, i, n)

        while (n > 0):
            self.__exchange(array, 1, n)
            n -= 1
            self.__sink(array, 1, n)

    ###
    ### HELPER FUNCTIONS
    ###
    def __exchange(self, array, a, b):
        temp = array[a - 1]
        array[a - 1] = array[b - 1]
        array[b - 1] = temp

    def __sink(self, array, k, n):
        while (k <= n // 2):
            temp = 2 * k
            if temp < n and array[temp] > array[temp - 1]:
                temp += 1

            if array[k - 1] > array[temp - 1]:
                break

            self.__exchange(array, temp, k)
            k = temp

# Experiments to check time complexity.
if __name__ == "__main__":

    H = Heap()
    array = random.sample(range(0, 1000000), 400000)
    startTime = time.time()
    H.sort(array)
    assert all(array[i] <= array[i+1] for i in range(0, len(array) - 1))
    print("Time taken to sort 400000 numbers -> " + str(time.time() - startTime) +
        " seconds")

    array = random.sample(range(0, 1000000), 800000)
    startTime = time.time()
    H.sort(array)
    assert all(array[i] <= array[i+1] for i in range(0, len(array) - 1))
    print("Time taken to sort 800000 numbers -> " + str(time.time() - startTime) +
        " seconds")
