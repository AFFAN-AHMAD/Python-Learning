myTuple = (1,2,3,4,5)
i1, *i2 = myTuple

print(i1,*i2) # 1 2 3 4 5
print(i1,i2) # 1 [2, 3, 4, 5]