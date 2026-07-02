from itertools import (product, permutations, combinations,
                       combinations_with_replacement, accumulate, groupby, count, cycle, repeat)
import operator
a=[1,2]
b=[3,4]
prod =product(a,b)
print('ffff',list(prod))

a = [1,3,2]
perm = permutations(a)
# print(list(perm))

a = [2,3,4]
comb = combinations(a,2)
# print(list(comb))


a = [2,3,4]
comb = combinations_with_replacement(a,2)
print(list(comb)) # self repetitions allowed

a = (2,4,3)
acc = accumulate(a)
# acc = accumulate(a, func=operator.mul)
# acc = accumulate(a, func=operator.add)
# acc = accumulate(a, func=max)
print(list(acc))

a = [2,3,4]

# def smaller_than_3(c):
#     return c<3
# group = groupby(a,key=smaller_than_3)
group =groupby(a, key=lambda x: x<3) # this is same as the above function
# print(list(group))
for key, value in group:
    print (key, list(value))

persons = [
    {
        "name": "Affan",
        "age": 25
    },
    {
        "name": "Ahmad",
        "age": 26
    },
    {
        "name": "Ali",
        "age": 25
    },
    {
        "name": "Khan",
        "age": 28
    },
]
# if I don't sort, the result would be different,
# there would be two keys for 25 as they are not adjacent
# thus sorted the persons list first

persons = sorted(persons, key=lambda x: x['age'])

group = groupby(persons, key=lambda x: x['age'])
for key, value in group:
    print (key, list(value))


for i in count(10):
    print(i)
    if(i>15):
        break
x = [1,2,3]

# for i in cycle(x):
#         print(i)
         
x = [2,2,5]
for i in repeat(x, 5):
     print(i)