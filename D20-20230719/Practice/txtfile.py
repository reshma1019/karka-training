#read
# file=open("/home/reshma/reshma.txt","r")
# print(file.read())


#read
# file=open("/home/reshma/reshma.txt","r")
# for line in file:
#      print(line)

#read
# file=open("/home/reshma/reshma.txt","r")
# data=file.read()
# print(data)


#write 
# file=open("/home/reshma/reshma.txt","w")
# file.write("I'm reshma\nI am from pmd")
# file.close()
# file=open("/home/reshma/reshma.txt","r")
# print(file.read(3))

#append
# file=open("/home/reshma/reshma.txt","a")
# file.write("I'm reshma\nI am from pmd")
# file.close()
# file=open("/home/reshma/reshma.txt","r")
# print(file.read())


#line split
file=open("/home/reshma/reshma.txt","r")
for line in file:
    print(line.split())



