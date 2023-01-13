
class MyIterable:

    def __init__(self,maxval):
        self.maxval = maxval
        self.value = 2
        self.exponent = 0
    
    def __iter__(self):
        return self
        
    def __next__(self):            
        self.value = 2
        self.value **= self.exponent
        self.exponent += 1
        if self.value > self.maxval:
            raise StopIteration
        return self.value
        
potens_iterator = MyIterable(20)
for i in potens_iterator:
    print(i)


