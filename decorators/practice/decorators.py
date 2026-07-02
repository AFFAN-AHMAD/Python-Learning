import functools
import time

def slow_down(rate=1, _func=None):

    def slow_down_wrapper(func):
        def wrapper(*args, **kwargs):
            time.sleep(rate)
            # print(args)
            return func(args[0])
        return wrapper
    if _func is not None:
        return slow_down_wrapper(_func)
    else:
        return slow_down_wrapper
    
@slow_down(rate = 2)
def countDown(num):
    if num <1:
        print('Lift Off')
    else:
        print(num)
        countDown(num-1)
countDown(3)