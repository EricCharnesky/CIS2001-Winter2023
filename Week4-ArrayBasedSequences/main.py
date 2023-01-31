import sys
import time

import matplotlib.pyplot as plt

some_list = []
times = []


# space complexity - how much memory is used

# time complexity - how many operations are done

# appending to a list
# - average is constant O(1)
# - worst case is O(N) - copy from old to new array
# - best case - we don't care, but it's O(1)

def compute_time_to_add(list_to_add_to, item):
    start = time.perf_counter()
    list_to_add_to.append(item)
    end = time.perf_counter()
    return end-start


timings = []
some_list = []
values = range(10_000_000)
for n in values:
    timings.append(compute_time_to_add(some_list, n))

plt.plot(values, timings)
plt.show()

# copy process - O(n) - linear time
new_list = [None] * (len(some_list) * 2)
for index in range(len(some_list)):
    new_list[index] = some_list[index]

# constant time access to a value by index
some_list[67]

# removing an item from a list
some_list.remove(10)
# worst O(N)
# average O(N)
# best - we don't really care O(n)

some_list.pop(98)
# worst - O(N)
# average - O(N) - really .5N - but we throw away the .5
# best - O(1) - the very last index

# log(n)

# linear time - the more N we have, the longer it takes
# throw away coefficients

# n log(n)

# exponential or n^2 time

