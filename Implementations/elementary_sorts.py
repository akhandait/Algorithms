import time
import random

#######################
### Selection Sort. ###
#######################

class Selection:

    # Sort the given array.
    def sort(self, array):
        l = len(array)
        for i in range(l):
            minIndex = i
            for j in range(i, l):
                if array[j] < array[minIndex]:
                    minIndex = j
            self.__exchange(array, i, minIndex)

    """
    HELPER FUNCTIONS
    """
    def __exchange(self, array, a, b):
        temp = array[a]
        array[a] = array[b]
        array[b] = temp

# Experiments to check time complexity.
if __name__ == "__main__":

    s = Selection()
    array = random.sample(range(0, 100000), 4000)
    startTime = time.time()
    s.sort(array)
    print("Time taken to sort 4000 numbers -> " + str(time.time() - startTime) +
        " seconds")

    array = random.sample(range(0, 100000), 8000)
    startTime = time.time()
    s.sort(array) # This will take ~4 times longer.
    print("Time taken to sort 8000 numbers -> " + str(time.time() - startTime) +
        " seconds")

#######################
### Insertion Sort. ###
#######################

class Insertion:

    # Sort the given array.
    def sort(self, array):
        l = len(array)
        for i in range(1, l):
            for j in reversed(range(i)):
                if array[j + 1] < array[j]:
                    self.__exchange(array, j + 1, j)
                else:
                    break

    # For practical improvement in mergesort an quicksort.
    def sortLH(self, array, low, high):
        for i in range(low + 1, high + 1):
            for j in reversed(range(low, i)):
                if array[j + 1] < array[j]:
                    self.__exchange(array, j + 1, j)
                else:
                    break

    """
    HELPER FUNCTIONS
    """
    def __exchange(self, array, a, b):
        temp = array[a]
        array[a] = array[b]
        array[b] = temp

# Experiments to check time complexity.
if __name__ == "__main__":

    i = Insertion()
    array2 = random.sample(range(0, 100000), 4000)
    startTime = time.time()
    i.sort(array2)
    print("Time taken to sort 4000 numbers -> " + str(time.time() - startTime) +
        " seconds")

    array4 = random.sample(range(0, 100000), 8000)
    startTime = time.time()
    i.sort(array4) # This will take ~4 times longer.
    print("Time taken to sort 8000 numbers -> " + str(time.time() - startTime) +
        " seconds")

    # Now we try sorting partially sorted arrays.
    for j in range(500):
        a = random.randint(0, 3999)
        b = random.randint(0, 3999)

        temp = array2[a]
        array2[a] = array2[b]
        array2[b] = temp

        c = random.randint(0, 7999)
        d = random.randint(0, 7999)

        temp = array4[c]
        array4[c] = array4[d]
        array4[d] = temp

    startTime = time.time()
    i.sort(array2)
    print("Time taken to sort 4000 numbers -> " + str(time.time() - startTime) +
        " seconds")

    # Insertion sort in linear time for partially sorted array.
    # So, the following should take ~2 times longer.
    startTime = time.time()
    i.sort(array4)
    print("Time taken to sort 8000 numbers -> " + str(time.time() - startTime) +
        " seconds")

###################
### Shell Sort. ###
###################

class Shell:

    # Sort the given array.
    def sort(self, array):
        l = len(array)
        h = 1
        while (h < l // 3):
            h = 3 * h + 1

        while (h >= 1):
            for i in range(int(h), l):
                j = i
                while True:
                    if array[j] < array[j - int(h)]:
                        self.__exchange(array, j, j - int(h))
                    j -= h
                    if j < h:
                        break
            h //= 3

    """
    HELPER FUNCTIONS
    """
    def __exchange(self, array, a, b):
        temp = array[a]
        array[a] = array[b]
        array[b] = temp

# Experiments to check time complexity.
if __name__ == "__main__":

    s = Shell()
    array = random.sample(range(0, 100000), 4000)
    startTime = time.time()
    s.sort(array)
    print("Time taken to sort 4000 numbers -> " + str(time.time() - startTime) +
        " seconds")

    array = random.sample(range(0, 100000), 8000)
    startTime = time.time()
    s.sort(array)
    print("Time taken to sort 8000 numbers -> " + str(time.time() - startTime) +
        " seconds")



