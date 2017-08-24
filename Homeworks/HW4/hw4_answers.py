import numpy as np
import timeit
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.legend_handler import HandlerLine2D
from matplotlib.backends.backend_pdf import PdfPages

# Define the sorting functions.

# Selection method:
def selection(nlist):
    startedlist = nlist
    sortedlist = []
    while len(startedlist) > 0:
        sortedlist.append(min(startedlist))
        del startedlist[startedlist.index(sortedlist[-1])]
    return sortedlist

# Counting method:
def counting(nlist):
    indexarray = range(min(nlist), max(nlist) + 1)
    countarray = [nlist.count(i) for i in indexarray]
    newcount = [None] * len(countarray)
    n = 0
    total = 0
    while n < len(countarray):
        newcount[n] = total
        d = countarray[n]
        total += countarray[n]
        n += 1
    sortedlist = [None] * len(nlist)
    for i in nlist:
        sortedlist[newcount[indexarray.index(i)]] = i
        newcount[indexarray.index(i)] += 1
    return sortedlist

# Generate an auxiliary function to run simulate() with different
# sorting methods
def wrapper(function, *args):
    def wrapped():
        return function(*args)
    return wrapped

# Generate simulate()
def simulate(function, samplesize, low = 0, high = 100, times = 1):
    results = []
    for i in samplesize:
        np.random.seed(1)
        sample = np.random.randint(low, high, i).tolist()
        wrapped = wrapper(function, sample)
        results.append(timeit.timeit(wrapped, number = times))
    return pd.DataFrame({"samplesize":samplesize, "runtime":results})


# Generate a list with the sample sizes for the first simulation:
samplesize1 = range(1, 1001)

# Run the first simulation for counting() and save the dataset
countingsim1 = simulate(counting, samplesize1, -10, 10, 3)

# Run the first simulation for selection() and save the dataset
selectionsim1 = simulate(selection, samplesize1, -10, 10, 3)

# Plot the results for the first simulation and save the figure
f = plt.figure()
countingsort, = plt.plot(countingsim1.samplesize, countingsim1.runtime, 'r-',
                label = "Counting Sort")
selectionsort, = plt.plot(selectionsim1.samplesize, selectionsim1.runtime, 'b-',
                label = "Selection Sort")
plt.xlabel('Sample Size')
plt.ylabel('Time (in seconds)')
plt.title('Scenario 1: Many repeated numbers in the sample')
plt.legend(handler_map={countingsort: HandlerLine2D(numpoints=1)})
plt.show()
f.savefig("scenario1.pdf", bbox_inches='tight')
plt.close()

# Run the second simulation for counting() and save the dataset
countingsim2 = simulate(counting, samplesize1, -100, 100, 3)

# Run the first simulation for selection() and save the dataset
selectionsim2 = simulate(selection, samplesize1, -100, 100, 3)

# Plot the results for the first simulation and save the figure
f = plt.figure()
countingsort, = plt.plot(countingsim2.samplesize, countingsim2.runtime, 'r-',
                label = "Counting Sort")
selectionsort, = plt.plot(selectionsim2.samplesize, selectionsim2.runtime, 'b-',
                label = "Selection Sort")
plt.xlabel('Sample Size')
plt.ylabel('Time (in seconds)')
plt.title('Scenario 2: Less repeated numbers in the sample')
plt.legend(handler_map={countingsort: HandlerLine2D(numpoints=1)})
plt.show()
f.savefig("scenario2.pdf", bbox_inches='tight')
plt.close()

# Generate a new list with the sample sizes for the third simulation.
# This list is smaller than the first one to make the simulation possible
# in a reasonable amount of time.
samplesize2 = range(1, 101)

# Run the first simulation for counting() and save the dataset
countingsim3 = simulate(counting, samplesize2, -100000, 100000, 3)

# Run the first simulation for selection() and save the dataset
selectionsim3 = simulate(selection, samplesize2, -100000, 100000, 3)

# Plot the results for the first simulation and save the figure
f = plt.figure()
countingsort, = plt.plot(countingsim3.samplesize, countingsim3.runtime, 'r-',
                label = "Counting Sort")
selectionsort, = plt.plot(selectionsim3.samplesize, selectionsim3.runtime, 'b-',
                label = "Selection Sort")
plt.xlabel('Sample Size')
plt.ylabel('Time (in seconds)')
plt.title('Scenario 3: Almost none repeated number in the sample')
plt.legend(handler_map={countingsort: HandlerLine2D(numpoints=1)})
plt.show()
f.savefig("scenario3.pdf", bbox_inches='tight')
plt.close()
