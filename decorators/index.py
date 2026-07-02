# def start_fun(func):
#     def wrapper(name): 
#         print('start')
#         func(name)
#         print('end')
#     return wrapper

# def anotherFunc():
#     print('name')

# # printName = start_fun(anotherFunc)
# # printName()

# @start_fun
# def anotherFunc(name): 
#         print(name)
# anotherFunc('Affan')


def say_hello(name):
    return f"hello {name}"

def be_awsome(name):
    return f"hi {name}. We are awesome together!"

def greetBob(func):
    return func('bob')
print(greetBob(be_awsome))

def parentFunction():
    print("acs")
    def first_child():
        print('first Child')
    def second_child():
        print('second Child')
    return {
        'first_child': first_child
    }
    # second_child()
print(parentFunction()['first_child']())