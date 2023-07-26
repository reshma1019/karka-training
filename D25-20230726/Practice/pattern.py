# n=int(input("Enter a rows and coloumn:"))
# for i in range(n):
#     print("*" * n)



# n=int(input("Enter a rows and coloumn:"))
# for i in range(n):
#     for j in range(n):
#         print("*" ,end=" ")
#     print(" " )

# n=int(input("enter a rows and coloumn:"))
# a=0
# for i in range(n):
#     for j in range(n):
#         a=a+1
#         print(a,end=" ")
#     print(" ")


n=int(input("enter a rows and coloumn:"))
for i in range(1,(n*n)+1):
    
    print(i,end=" ")
    if i%n==0:
    #  print(" ")
     print("\n")
#reverse print
n=int(input("enter a rows and coloumn:"))
for i in range((n*n),0,-1):
    if i%n==0:
        print("")
    print(i,end=" ")
    







    


