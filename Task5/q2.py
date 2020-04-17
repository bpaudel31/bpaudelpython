from sys import argv
programname,filename=argv
while True:
    try:
        o=open(filename)   
        file_content=o.read()
        print (file_content)
        o.close
        break
    except:
        filename=input( "Wrong file name!Please enter file name again: ")


