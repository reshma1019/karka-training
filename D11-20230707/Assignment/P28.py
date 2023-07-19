sales_tax=8.25
shipping_cost=5.00
your_cart=0
shipping_cost_per_keychain=1.00
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

def view_order(sales_tax,shipping_cost,your_cart,shipping_cost_per_keychain):
    print(f"You have {your_cart} keychains.")
    subtotal=your_cart*10
    shipping_charges=shipping_cost+(your_cart*shipping_cost_per_keychain)
    tax=subtotal*sales_tax
    total_cost=subtotal+shipping_charges+tax
    print(f"Keychain cost is 10 each.\nShipping charges {shipping_charges}.\nSub total{subtotal}\nTax{tax}\nTotal cost ${total_cost}")
    return(your_cart)

def check_out(sales_tax,shipping_cost,your_cart,shipping_cost_per_keychain):
    name=input("What is your name? ")
    subtotal=your_cart*10
    shipping_charges=shipping_cost+(your_cart*shipping_cost_per_keychain)
    tax=(subtotal*sales_tax)/100
    total_cost=subtotal+shipping_charges+tax
    return(f"You have {your_cart} keychains\nKeychains cost is 10 each.\nShipping charges {shipping_charges}.\nSub total{subtotal}\nTax{tax}\nTotal cost ${total_cost}\nThanks for your order,{name}")
    
print("Ye Old Keychain Shopee")

while True:
    print("\n1).Add Keychains To Order\n2).Remove Keychains From Order\n3).View Current Order\n4).Checkout")
    choice=int(input("\nPlease enter your choice:"))
    if choice==1:
        your_cart=(add_keychain(your_cart))
    elif choice==2:
        your_cart=(remove_keychain(your_cart))
    elif choice==3:
        print(view_order(sales_tax,shipping_cost,your_cart,shipping_cost_per_keychain))
    elif choice==4:
        print(check_out(sales_tax,shipping_cost,your_cart,shipping_cost_per_keychain))
        break

    else:
        print("invalid comments")

    