def mygen():
    yield 3
    yield 2
    yield 1
    yield -2
g = mygen()

sumup = sum(g)
print(sumup)

g = mygen()
print(sorted(g))


