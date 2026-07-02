from functools import wraps
def repeat(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        num = kwargs['n']
        for _ in range(num):
            func(args[0])
    return wrapper

@repeat
def any_func(name):
    print(name)
any_func('Affan', n=2)