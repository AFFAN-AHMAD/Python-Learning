# setA = {2,4,6,8,10}
# setA.add(12)
# print(setA)

# setA.remove(12)
# print(setA)

# setA.remove(11) - keyError
# print(setA)

# setA.discard(11) # if not found no problem
# print(setA)

# setA.clear()
# print(setA)

# setA = {2,3,4,5,6}
# setB = {2,5,8,34,56}
# print(setA.union(setB))
# print(setA.intersection(setB))
# print(setA.difference(setB))
# print(setA.symmetric_difference(setB))


setA = {2,3,4,5,6}
setB = {2,5,8,34,56}
# setA.update(setB)
# print(setA) # {2,3,4,5,6,8,34,56}

# setA.intersection_update(setB)
# print(setA) # {2,5}

# setA.difference_update(setB)
# print(setA) # {3,4,6}

# setA.symmetric_difference_update(setB)
# print(setA) # {3,4,6,8,34,56}