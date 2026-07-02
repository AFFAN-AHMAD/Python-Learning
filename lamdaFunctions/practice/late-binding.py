funcs = []

for i in range(5):
    funcs.append(lambda i= i: i)

# without i = i, we went into late-binding mode
# for i in range(5):
#     funcs.append(lambda: i)

# print(funcs[0])
# print(funcs[1])
# print(funcs[2])

# for func in funcs:
#     print(func())


# another way
def make_func(x):
    # print(x)
    return lambda: x

funcs = []
for i in range(5):
    funcs.append(make_func(i))
for func in funcs:
    print(func())