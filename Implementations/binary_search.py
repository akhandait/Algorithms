import time
from random import randint

# Iterative implementation.
def binarySearch(array, key):
    low = 0
    high = len(array) - 1

    while (low <= high):
        mid = low + (high - low) // 2

        if (key < array[mid]):
            high = mid - 1
        elif (key > array[mid]):
            low = mid + 1
        else:
            return mid

    return -1

if __name__ == "__main__":
    a = list(range(100000))
    start_time = time.time()
    for i in range(50000):
        binarySearch(a, randint(0, 99999))
    print("Time taken -> " + str(time.time() - start_time))

    # The following will take just slightly more time. (logarithmic)
    a = list(range(200000))
    start_time = time.time()
    for i in range(50000):
        binarySearch(a, randint(0, 199999))
    print("Time taken -> " + str(time.time() - start_time))

# Recursive implementation.
def binarySearchRecur(array, low, high, key):
    if low > high:
        return -1

    mid = low + (high - low) // 2
    if (key < array[mid]):
        high = mid - 1
        return binarySearchRecur(array, low, high, key)
    elif (key > array[mid]):
        low = mid + 1
        return binarySearchRecur(array, low, high, key)
    else:
        return mid

if __name__ == "__main__":
    a = list(range(100000))
    start_time = time.time()
    for i in range(50000):
        binarySearchRecur(a, 0, len(a) - 1, randint(0, 99999))
    print("Time taken -> " + str(time.time() - start_time))

    # The following will take just slightly more time. (logarithmic)
    a = list(range(200000))
    start_time = time.time()
    for i in range(50000):
        binarySearchRecur(a, 0, len(a) - 1, randint(0, 199999))
    print("Time taken -> " + str(time.time() - start_time))

