def selection(nlist):
    startedlist = nlist
    sortedlist = []
    while len(startedlist) > 0:
        sortedlist.append(min(startedlist))
        del startedlist[sortedlist.index(sortedlist[-1])]

test = [2, 3, 1, 6, 2]
