Mango=int(input("Enter the amount of Mango:" ))
Apple=int(input("Enter the amount of Apple:" ))
Orange=int(input("Enter the amount of Orange:" ))
Grapes=int(input("Enter the amount of Grapes:" ))
total=Mango+Apple+Orange+Grapes
print(total)
if total>=500 and total<= 1000:
    print("You have owned a silver token ")
if total>1000:
    print("You have owned a golden token")
if total<500:
    print("You have owned no token")
