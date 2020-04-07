#1

x=[1,"task3",2+3j,2.345,5,"bikash",3,0.456,"abc123",10000]
print (x)

#2
x=[1,2,3,4,5]
print (x[:])
print (x[1:4])
print(x[2:])
print(x[:4])
print (x[::2])

#3 Multiplication
x=[1,2,3,4,5]
y=1
for i in x:
    y=y*i
print (y)

##3 Addition
x=[1,2,3,4,5]
y=0
for i in  x:
    y=y+i
print (y)

##4
x=[1,2,3,4,5]
print ("Max value:",max(x))
print ("Max value:",min(x))

#5
x=[4,5,6,8,7,10,344,355,400]
for i in x[:]:
    if i%2==0:
        x.remove(i)
print("List after removing even numbers:",x)

#6
x=[]
for i in range (1,31):
    y=i**2
    x.append (y)
z= (x[:5])
a=(x[-5:])
print ("First five and last five:",z+a)

#7
x=[1,3,5,7,9,10]
y=[2,4,6,8]
x=x[:-1]+y
print (x)

#8
a={1:10,2:20}
b={3:30,4:30}
x={}
for z in (a,b):
    x.update(z)
print (x)

#9
n=int(input("Please Enter a number"))
x = dict()

for i in range(1,n+1):
    x[i]=i*i

print(x)

#10
x=input("Enter comma seperated numbers:")
list=x.split(",")
tuple=tuple(list)
print("List:",list)
print("Tuple:",tuple)