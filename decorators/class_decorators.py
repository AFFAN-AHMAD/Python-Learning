class CountCalls:
    def __init__(self, func):
        self.func = func
        self.count = 0
    def __call__(self, *args, **kwds):
        self.count+=1
        print(f'this is executed {self.count} times')
        return 
    # return self

@CountCalls
def repeated():
    print('hi')

repeated()
repeated()