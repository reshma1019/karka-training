your_cart=0
def add_keychain(your_cart):
    add=int(input("\nYou have 0 keychains.How many to add? "))
    your_cart=your_cart+add
    print(f"You now have {your_cart} keychains")
    return (your_cart)
    
def remove_keychain(your_cart):
    remove=int(input(f"\nYou have {your_cart} keychains.How many to remove? "))
    your_cart=your_cart-remove
    print(f"You now have {your_cart} keychains.")
    return(your_cart)

def view_order(your_cart):
    print(f"You have {your_cart} keychains.")
    cost=your_cart*10
    print(f"Keychain cost is 10 each.\nTotal cost is {cost}")
    return(your_cart)

def check_out(your_cart):
    name=input("What is your name? ")
    cost=your_cart*10
    return(f"You have {your_cart} keychains\nKeychains cost is 10 each.\nTotal cost is {cost}.\nThanks for your order,{name}")
    
print("Ye Old Keychain Shopee")

while True:
    print("\n1).Add Keychains To Order\n2).Remove Keychains From Order\n3).View Current Order\n4).Checkout")
    choice=int(input("\nPlease enter your choice:"))
    if choice==1:
        your_cart=(add_keychain(your_cart))
    elif choice==2:
        your_cart=(remove_keychain(your_cart))
    elif choice==3:
        print(view_order(your_cart))
    elif choice==4:
        print(check_out(your_cart))
        break

    else:
        print("choose between 1 and 4")

     