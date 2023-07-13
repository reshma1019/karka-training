num=0
def adding_values(num):
    while True:
        number=int(input("Number: "))
        if number==0:
            print("The total is",num)
            break
        num=number+num
        print(f"The total so far is ,{num}")

adding_values(num)