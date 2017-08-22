def selection(nlist):
    startedlist = nlist
    sortedlist = []
    while len(startedlist) > 0:
        sortedlist.append(min(startedlist))
        del startedlist[startedlist.index(sortedlist[-1])]
    return sortedlist

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
