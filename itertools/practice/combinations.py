import itertools

listing = [1,3,4,0,6,2,5]
combo = itertools.combinations(listing, 2)
filtered = filter(lambda x: (x[0]+x[1] == 9), combo)
print(list(filtered))