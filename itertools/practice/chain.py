import itertools
a = [1,2,3,4]
b = [1,3,4,5,6,3]
c = [1,5,8,3]
chainedList = itertools.chain(a,b,c)
print(list(chainedList))