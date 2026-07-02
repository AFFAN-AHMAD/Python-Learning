from functools import wraps
from index import start_fun
def repeat_n_times(func):
    @wraps(func)
    def wrapper(name, **kwargs):
        for i in range(kwargs['n']):
            func(name)
    return wrapper

@repeat_n_times
def greet(name):
    """Hi this is a wrap function"""
    print(f'Hi {name}')
greet('Affan', n=3 )

print(greet.__name__)
print(greet.__doc__)
print(greet.__module__)






# @start_fun
# def repeat_itself(name):
#     print(f'hi {name}')
# repeat_itself('Affan')