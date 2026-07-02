import sys

mygenerator  = (i for i in range(10000) if i%2==0)
# print(sys.getsizeof(list(mygenerator)))
myList  = [i for i in range(10000) if i%2==0]
# print(sys.getsizeof(myList))
print(
sum(mygenerator),
sum(myList))