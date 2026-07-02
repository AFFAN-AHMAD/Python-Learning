from functools import wraps
def shout(func):
    @wraps(func)
    def wrapper(*args):
        newStr =  args[0].upper()
        func(newStr)
    return wrapper

@shout
def make_shout(x):
    print(x)

make_shout('abc')


# 

