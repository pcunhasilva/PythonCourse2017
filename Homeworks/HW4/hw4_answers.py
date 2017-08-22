def selection(nlist):
    startedlist = nlist
    sortedlist = []
    while len(startedlist) > 0:
        sortedlist.append(min(startedlist))
        del startedlist[startedlist.index(sortedlist[-1])]
    return sortedlist

def counting(nlist):
    unsortedlist = nlist
    # Part 1
    indexarray = range(min(unsortedlist), max(unsortedlist) + 1)
    countarray = [unsortedlist.count(i) for i in indexarray]
    # Part 2
    newcount = []
    n = 0
    while n < len(countarray):
        if n == 0:
            newcount.append(countarray[n])
        elif n == len(countarray):
            newcount.append(countarray[n - 1])
        else:
            newcount.append(newcount[n - 1] + countarray[n])
        n += 1
    # Part 3
    sortedlist = [None] * len(unsortedlist)
    for i in range(len(unsortedlist)):
        if i >= len(unsortedlist): continue
        if unsortedlist[i] in sortedlist:
            sortedlist[newcount[unsortedlist[i] - 1] - 2] = unsortedlist[i]
        else:
            sortedlist[newcount[unsortedlist[i] - 1] - 1] = unsortedlist[i]
    return sortedlist


# def counting(nlist):
#     unsortedlist = nlist
#     # Part 1
#     indexarray = range(min(unsortedlist), max(unsortedlist) + 1)
#     countarray = [unsortedlist.count(i) for i in indexarray]
#     # Part 2
#     newcount = []
#     n = 0
#     while n < len(countarray):
#         if n == 0:
#             newcount.append(countarray[n])
#         elif n == len(countarray):
#             newcount.append(countarray[n - 1])
#         else:
#             newcount.append(newcount[n - 1] + countarray[n])
#         n += 1
#     # Part 3
#     sortedlist = [None] * len(unsortedlist)
#     for i in range(len(unsortedlist)):
#         if i >= len(unsortedlist): continue
#         if unsortedlist[i] in sortedlist:
#             sortedlist[newcount[unsortedlist[i] - 1] - 2] = unsortedlist[i]
#         else:
#             sortedlist[newcount[unsortedlist[i] - 1] - 1] = unsortedlist[i]
#     return sortedlist
