import time
from functools import wraps

def timerr(func):
    @wraps(func)
    def wrapper(*args):
        startTime = time.time()
        print(args)
        func(args[0])
        endTime = time.time()
        execution_time = endTime - startTime
        print(str(execution_time))
    return wrapper

@timerr
def big_task(x):
    for i in range(100000):
        # print(x)
        pass

big_task('abc')