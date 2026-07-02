import itertools
listOfWords = ['Affan', 'Toofan', 'Halkan', 'Hindustan', 'Uzbekistan', 'Afghanistan']
sortedList = sorted(listOfWords, key=lambda x: x[0])
grouping = itertools.groupby(list(sortedList),key= lambda x: x[0] )
for key, value in grouping:
    print(key, list(value))
print(grouping)
