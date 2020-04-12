#1
x="1234abcd"
y=x[::-1]
print (y)

##2
def case():
    x="AbcDef"
    y=0
    z=0
    for i in x:
        if i.isupper():
            y=y+1
        elif i.islower():
            z=z+1
    print("No. of Upper case characters :",y)
    print("No. of Lower case Characters:",z)
case()

##3
def unique():
    x=[1,2,3,4,5,2,3,45,56,4]
    y=set(x)
    print (list(y))
unique()


#4
x=input("Enter  hypen seperated words:")
y=x.split('-')
print('-'.join (y))


##5
x=input("Enter a sentence:")
y=x.upper()
print(y)

#6
def sum(x,y):
    y=int(x)+int(y)
    print(y)
sum("2","3")

##7
def task_7(x,y):
    if len(x)>len(y):
        print(x)
    elif len(y)>len(x):
        print(y)
    elif len(x)==len(y):
        print(x)
        print(y)
task_7("bikashaaaaaaaaaaaaaa","paudelaaa")

#8
def task_8():
    x=[]
    for i in range(1,21):
        i=i**2
        x.append (i)
    t=tuple(x)
    print(t)
task_8()

#9
def showNumbers(limit):
    for x in range(limit+1):
        if x%2==0:
            print (x,"EVEN")
        else:
            print(x,"ODD")
showNumbers(3)

#10

x=range(1,21)
y=list(filter(lambda z :(z%2==0),x))
print (y)

#11
x=[1,2,3,4,5,6,7,8,9,10]
y=list(filter(lambda z :(z%2==0),x))
res=list(map(lambda a:a*a,y))
print(res)

#12
def task_12(x,y):
    try:
        print(x/y)
    except:
        print("You cannot divide a number by 0")
task_12(5,0)

##13
from functools import reduce
l= [[1,2,3],[4,5],[6,7,8]]
y=reduce(lambda a,z:a+z,l)
print(''.join(str(x) for x in y))

#14
#(i) returns 2
#(ii) returns error (f is not defined)



