num=0
def adding_values():
    while True:
        number=int(input("Number: "))
        if number==0:
            print("The total is",add)
            break
        if number>=0:
            add=number+num
            num=num+add
            print(f"The total so far is ,{add}")

adding_values()