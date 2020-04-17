u_email="bikash.paudel31@gmail.com"
u_pwd="bp31"
count=0
while count<3:
        x=input("Please enter Username: ")
        y=input("Please enter Password: ")
        if y==u_pwd:
            print ("Login Success")
            break
        elif y!=u_pwd:
                print("wrong pwd Please enter Password: ")
                count +=1
