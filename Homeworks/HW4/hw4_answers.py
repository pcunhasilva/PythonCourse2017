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
    unsortedlist = nlist
    indexarray = range(min(unsortedlist), max(unsortedlist) + 1)
    countarray = [unsortedlist.count(i) for i in indexarray]
    newcount = [None] * len(countarray)
    n = 0
    total = 0
    while n < len(countarray):
        newcount[n] = total
        d = countarray[n]
        total += countarray[n]
        n += 1
    # Part 3
    sortedlist = [None] * len(unsortedlist)
    for i in unsortedlist:
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
def simulate(function, samplelist, times):
    results = []
    for i in samplelist:
        np.random.seed(1)
        sample = np.random.randint(-1000000, 1000000, i).tolist()
        wrapped = wrapper(function, sample)
        results.append(timeit.timeit(wrapped, number = times))
    return pd.DataFrame({"samplesize":samplelist, "runtime":results})


# Generate a list with the sample sizes:
samplesize = [5, 10, 50, 100, 1000, 10000, 100000]

# Run simulate for counting() and save the dataset
countingsim = simulate(counting, samplesize, 1)

# Run simulate for selection() and save the dataset
selectionsim = simulate(selection, samplesize, 1)

# Plot the results
countingsort, = plt.plot(countingsim.samplesize, countingsim.runtime, 'r-',
                label = "Counting Sort")
selectionsort, = plt.plot(selectionsim.samplesize, selectionsim.runtime, 'b-',
                label = "Selection Sort")
plt.xlabel('Sample Size')
plt.ylabel('Time (in seconds)')
plt.title('Comparison between selection and counting sort')
plt.legend(handler_map={countingsort: HandlerLine2D(numpoints=1)})
