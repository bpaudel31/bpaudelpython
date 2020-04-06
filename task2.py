#TASK TWO: OPERATORS AND DECISION MAKING STATEMENT
# 1
x=5

if x%3==0 and x%5==0:
    print ("consultadd python training")
elif x%3==0:
    print ("consultadd")
elif x%5==0:
    print ("c")

#2 
#prints results and condition for negative, question is not clear if I have to only print sza if result is negative. Can change if condition accordingly
a=int(input("Please enter a number between 1-5:"))
if a==1:
    x=int(input("Please enter a first number:"))
    y=int (input ("Please enter a second number:"))
    addition=x+y
    print ("Addition Result:",addition)
    if addition <0:
        print ("zsa")
if a==2:
    x=int(input("Please enter a first number:"))
    y=int (input ("Please enter a second number:"))
    substraction=x-y
    print ("Substraction Result:",substraction)
    if substraction <0:
        print ("zsa")
if  a==3:
    x=int(input("Please enter a first number:"))
    y=int (input ("Please enter a second number:"))
    division=x/y
    print ("Division Result:",division)
    if division <0:
        print ("zsa")
if  a==4:
    x=int(input("Please enter a first number:"))
    y=int (input ("Please enter a second number:"))
    multiplication=x*y
    print ("Multiplication Result:",multiplication)
    if multiplication <0:
        print ("zsa")
if a==5:
    x=int(input("Please enter a first number:"))
    y=int (input ("Please enter a second number:"))
    z=int(input("Please enter a third number:"))
    b=int(input("Please enter a fourth number:"))
    average=(x+y+z+b)/4
    print ("Average Result:",average)
    if average <0:
        print ("zsa")
#3 Write a program in Python to implement the given flowchart:
a=10
b=20
c=30
avg=(a+b+c)/3
print ("avg=",avg)
if avg>a and avg >b and avg>c:
    print ("avg is higher than a,b,c")
elif avg>a and avg>b:
    print ("avg is higher than a,b,c") 
elif avg>a and avg>c:
    print ("avg is higher than a,c")
elif avg>b and avg>c:
    print ("avg is higher than b,c")
elif avg >a:
    print("avg is higher than a")
elif avg>b:
    print("avg is just higher than b")
elif avg>c:
    print ("avg is just higher than c")

#4
while True:
    x=int(input("Please enter a  number:"))
    if x<0:
        print ("It’s Over")
        break
    if x>=0:
        print("Good Going")
        continue


#5
list_5=[]
for x in range (2000,3200):
    if x%7==0 and x%5 !=0:
        list_5.append(x)
print (list_5)


#6 int type cannot be iterable, it should be list
#6  0,1,2
#6 0,1,2,3,4

#7
for x in range (0,6):
    if x!=3 and x!=6:
        print (x)
        continue
    

#8
x=input("Please enter a string:")
digit_count=0
letter_count=0
for i in x:
    if (i.isdigit()):
        digit_count+=1
    else:
        letter_count+=1
print("Number of digits:",digit_count)
print("Number of strings:",letter_count)

#9
while True:
    x=int(input("Guess the lucky number:"))
    if x!=8:
        print("Incorrect Guess Again")
        continue
    else:
       print ("Congrats you guessed the lucky number")
       break

#9 2nd part
while True:
    number=int(input("Guess the lucky number:"))
    if number!=8:
        print("Incorrect Guess,Try Again")
        answer=input ("Do you want to continue guessing? Yes or No:")
        if answer=="Yes":
            print("Incorrect Guess,Try Again")
            continue
        elif answer =="No":
            print("Thank you for playing")
            break
       
    else:
        print ("Congrats you guessed the lucky number")
        break

#10
counter=1
while counter<=5:
    x=int(input("Guess the lucky number:"))
    if x!=8:
        print("Incorrect number,please try again") 
    else:
        print("Congrats You won")
    counter=counter+1
else:
    print("You do no have any turns left")
 

#11 added break to #10
counter=1
while counter<=5:
    x=int(input("Guess the lucky number:"))
    if x!=8:
        print("Incorrect number,please try again") 
    else:
        print("Congrats You won")
        break
    counter=counter+1
else:
    print("You do no have any turns left")