class overloading:

    def add(self,a :int,b :int):
        return a+b

    def sub(self,a: int,b :int=0):
        return a-b
obj=overloading()
print(obj.sub(10,11))
