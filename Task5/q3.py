while True:
    try:
         x=input("please enter a number with four digit: ")
         if len (x)<=4:
             print (x)
             break
    except:
        if len(x)>4:
            x=int(input("Please length is too short/long !!! Please provide only four digits:"))