class Person:
    def __init__(self,age):
        self.age=age
        if self.age<0:
            print("Age is not valid")
            self.age=0
    def yearPasses(self):
        self.age +=1
        return self.age
    def amIOld(self):
        if self.age < 13:
            print("You are young")
        elif self.age >12 and self.age < 18:
            print ("You are teenager")
        else:
            print ("You are old")

res=Person(12)
res.amIOld()
print(res.yearPasses())


