class Shape:
    def __init__(self):
        pass

    def area(self):
        return 0
class Square:
    def __init__(self,l):
        self.l=l

    def area(self):
        A=self.l**2
        return A

res=Square(10)
print(res.area())