from functools import reduce
listing = [1,3,4,5]
prod = reduce(lambda x,y: x*y, listing)
print(prod)

