#1
print ("\n")
x=[1,"task3",2+3j,2.345,5,"bikash",3,0.456,"abc123",10000]
print (x)
print ("\n")

##2
x=[1,2,3,4,5]
print (x[:])
print (x[1:4])
print(x[2:])
print(x[:4])
print (x[::2])
print ("\n")

#3
x=[100,200,300,400,500,[1,2,3,4,5,[10,20,30,40,50],6,7,8,9],600,700,800]
print(x[5][:4])
print(x[6:8])
print(x[::2])
print (x[::-1])
print (x[5][5][:1])
print (x[100:])

#4 run in python 2.x
# range is a list while xrange  type is xrange
#x=range(1,1001)
#print (type(x))
#print ("\n")
#print (x)
#print ("\n")
#x=xrange (1,1001)
#print(x)
#print (type(x))

#5
#Tuple is not mutable while list is
#Tuple is faster than list
#Tuple consume less memory

#6
x=range(1,101)
for i in x:
    if i%3==0 and i%2==0:
        print(i)
 
#7
x="bikashpaudel"
y = x[::-1]
v = ('a', 'e', 'i', 'o', 'u')  
for x in y:
    if x not in v: 
        y = y.replace(x, "") 
print(y) 
    
#8
a="hello my name is abcde"
z=a.split(' ')
y=[]
for x in z:
    if len(x)%2==0:
        y.append (x)

print (y)

#9
x=[1,2,3,4,5,6,7,8,9,-1]
y=[]
for i in x:
    for j in x:
        if i+j==8:
            y.append((i,j))
print (y)

#10
even_list=[]
odd_list=[]
while True:
    x=int(input("enter a number between 1 and 50:"))
    if x in range(51):
        if x%2==0:
            even_list.append(x)
            if len(even_list)==5 and len(odd_list)>4:
                break
            elif len(even_list) >4:
                print('Limit exceeded')
        else:
            odd_list.append(x)
            if (len(odd_list)) == 5 and len(even_list) > 4:
               break
            elif len(odd_list) > 4:
               print('Limit exceeded')
    else:
        print("not in range")
print("even list:",even_list)
print("sum:",sum(even_list))
print ("max:",max(even_list))
print("odd list:",odd_list)
print("sum:",(odd_list))
print("max:",(odd_list))

#11
x='12abcbacbaba344ab'
y={}
for i in x:
    if i.isalpha():
        if i not in y:
            y[i]=1
        else:
            y[i] =y[i]+1
print(y)


#12
x=(1,2,3,4,5,6,7,8,9,10)
y=[]
for i in x:
    if i%2==0:
        y.append(i)
print (tuple(y))




