#1
x=[1,7,14,21,28,6,9,49]
res=list(filter(lambda x:(x%3!=0 and x%7==0),x))
print (res)

#2
def task_2(x): 
    return x*x
y = [1, 2, 3, 4] 
res = list(map(task_2, y) )
print(res)

##3
x="pthyontrainingtwentytwenty"
res=[y for y in x if y.isupper()] 
print (res)

##4
Student = ['Smit', 'Jaya', 'Rayyan']
capital = ['CSE', 'Networking', 'Operating System']
res=zip(Student,capital)
print (dict(res))

#5
#Yield:yield is a keyword that is used like return, except the function will return a generator.
#next:The next() function returns the next item in an iterator.
#Generators:Generator functions allow you to declare a function that behaves like an iterator

#6
def task_6(str):
    rev_str=''
    for i in range(len(str) - 1,-1,-1):
        rev_str = rev_str + str[i]
    yield rev_str


for i in task_6("Consultadd Training"):
     print(i)


#7
# a decorator takes in a function, adds some functionality and returns it.
#code samples from geeksforgeeks

def hello_decorator(func): 
  
    
    def inner1(): 
        print("Hello, this is before function execution") 
        func() 
        print("This is after function execution") 
    return inner1 
  
def function_to_be_used(): 
    print("This is inside the function !!") 
function_to_be_used = hello_decorator(function_to_be_used) 
function_to_be_used() 

#8
#5 top notch technologies of Frontend:Angular JS,SAAS,HTML,Javascript,CSS
# mentioned the name of companies using those 5 technologies individually: Google, Amazon,Twitter,Allegis