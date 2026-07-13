class Counter:
    count =0
    # @classmethod
    def increment(self):
        self.count+=1

c = Counter()
c.increment()
c.increment()
print(c.count)