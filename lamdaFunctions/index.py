from functools import reduce
points2D=[(1,2), (15,1),(5,-1),(10,4)]
points_Sorted2D = sorted(points2D, key=lambda a: a[1])
print(points_Sorted2D)

mappedPoints = map(lambda x: (x[0]*2, x[1]*2), points2D)
print(list(mappedPoints))

filteredPoints = filter(lambda x: (x[0]+ x[1]) > 5, points2D)
print(list(filteredPoints))

a=[1,2,3,4]
reducedPoints = reduce(lambda x,y: x*y, a)
print(reducedPoints)