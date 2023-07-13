def add_keychains():
    print("\nADD KEYCHAINS ")
def  remove_keychains():
    print("\nREMOVE KEYCHAINS ")
def view_order():
    print("\nVIEW ORDER")
def check_out():
    print("\nCHECHOUT")




print("Ye Old Keychain Shopee")
while True:
    print("\n1).Add Keychains To Order\n2).Remove Keychains From Order\n3).View Current Order\n4).Checkout")
    qn_1=int(input("\nPlease enter your choice:"))
    if qn_1==1:
        add_keychains()
    elif qn_1==2:
        remove_keychains()
    elif qn_1==3:
        view_order()
    elif qn_1==4:
        check_out()
        break
    else:
        print("invalid comment")


     
    