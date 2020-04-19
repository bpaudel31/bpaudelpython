import math
C=50
H=30
D= (input ("please enter comma seperate sequence of numbers: "))
val=D.split(",")
D_i =[int(i) for i in val]
Q=[((2*C*a)/H)**(0.5) for a in D_i]
print (Q)


