import time
from random import randint
from binary_search import binarySearch

def threeSum(array):
    array.sort()
    count = 0
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            if (binarySearch(array, -(array[i] + array[j])) != -1):
                if (array[i] < array[j] < -(array[i] + array[j])):
                    print(str(array[i]) + " " + str(array[j]) + " " +
                        str(-(array[i] + array[j])))
                    count += 1

    return count

a = list(range(2000))
a[20] = -40
start_time = time.time()
print(threeSum(a))
print("Time taken -> " + str(time.time() - start_time))

# The following will take slightly more than 4 times the time.(N**2LogN)
a = list(range(4000))
a[20] = -40
start_time = time.time()
print(threeSum(a))
print("Time taken -> " + str(time.time() - start_time))


# 3-Sum in quadratic time.
def threeSumQuad(array):
    array.sort()
    count = 0
    for i in range(len(array) - 2):
        a = array[i]
        start = i + 1
        end = len(array) - 1
        while (start < end):
            b = array[start]
            c = array[end]
            if (a + b + c == 0):
                print(str(a) + " " + str(b) + " " + str(c))
                count += 1
            elif (a + b + c > 0):
                end -= 1
            else:
                start += 1

    return count

a = list(range(2000))
a[20] = -40
start_time = time.time()
print(threeSum(a))
print("Time taken -> " + str(time.time() - start_time))

# The following will take 4 times the time.(N**2)
a = list(range(4000))
a[20] = -40
start_time = time.time()
print(threeSum(a))
print("Time taken -> " + str(time.time() - start_time))
