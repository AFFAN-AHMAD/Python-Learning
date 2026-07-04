from itertools import tee, islice

tupple = (1,2,3,4,5)
n = 3
length = len(tupple)
list1, list2 = tee(tupple)
print(list(list1), list(list2))
