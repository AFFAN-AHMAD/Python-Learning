
class count_calls:
    def __init__(self,  func):
        self.func = func
        self.count = 0
    def __call__(self):
        self.count+=1
        return self.count

@count_calls
def funcCalled():
    print('sdkf')

print(funcCalled())
print(funcCalled())
print(funcCalled())