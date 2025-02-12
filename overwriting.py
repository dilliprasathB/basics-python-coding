class mathoperation:
    def add(self,a: int,b: int):
        return a + b

class mathfunction(mathoperation):
    def add(self,a: int, b: int):
        return a - b

obj=mathfunction()
print(obj.add(10, 5))
