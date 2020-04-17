x=open("doc.txt","r")
y=x.read()
z=y.split(' ')
#print(z)
for i in z:
    if len(i)%2==0:
        print (i)
x.close()


        