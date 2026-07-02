import itertools
listing = itertools.count(2,2)
first10 = itertools.islice(listing, 10)
print(list(first10))