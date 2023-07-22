print("WELCOME TO METO'S TINY ADVENTURE!\n")
qn_1=input("You are in a creepy house! Would you like to go 'upstairs' or into the 'kitchen'?\n>")
if qn_1=="upstair":
    print("\nThere is balcony with lots of flowering plants you go and enjoy")
if qn_1=="kitchen":
    print("\nThere is a long countertop with dirty dishes everywhere, off to one side there is, as you'd expect a refrigerator")
    qn_2=input("You may open the 'refrigerator' or look in a 'cabinet'\n>")
    if qn_2=="refrigerator":
        qn_3=input("\nInside the refrigerator you see food and stuff. It looks pretty nasty, \nWould yo like to eat some of the food?('yes' or 'no')\n>")
        if qn_3=="yes":
            print("\nYou die of starvation...eventually")
            if qn_3=="no":
                print("\ngood you choose the healthy answer")
    if qn_2=="cabinet":
        print("\nThere is a cutting board,food containers")
