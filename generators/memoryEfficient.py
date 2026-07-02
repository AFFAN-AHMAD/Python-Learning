import sys
def first_n(n):
    nums = []
    num = 0
    while num < n:
        nums.append(num)
        num+=1
    return nums
print(first_n(10))

def first_n_gen(n):
    num = 0
    while num < n:
        yield num
        num += 1
print(list(first_n_gen(10)))

print(sys.getsizeof(first_n(10000)))
print(sys.getsizeof(first_n_gen(10000)))

"""
    results
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    85176
    200
"""
