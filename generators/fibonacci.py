# 0,1,1,2,3,5,8,13
def fibonacci(n):
    a,b = 0,1
    while n>0:
        yield a
        a, b = b, a + b
        n-=1

print(list(fibonacci(6)))