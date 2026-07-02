def start_fun(func):
    def wrapper(*args, **kwargs):
        print('start')
        func(*args, **kwargs)
        print('end')
    return wrapper

@start_fun
def add_5(args):
    print(args)
    # print(kwargs)
    return 5+ args

print(add_5(10))