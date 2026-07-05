def mygen():
    yield 3
    yield 2
    yield 1
    yield -2
g = mygen()

sumup = sum(g)
# print(sumup)

g = mygen()
# print(sorted(g))

comp = (i for i in range(4))
print(next(comp))
print(next(comp))


def listing(n):
    num = 0
    while True and num < n:
        if num%4 == 0:
             yield num
        num+=1
list_under_2000 = listing(2000)
for num in list_under_2000:
    print(num)

