earth_weight=int(input("Please enter your current earth weight:"))
print("I have information for the following planets:\n\t1.Venus \t2.Mars  \t3.Jupiter \n\t4.Saturn \t5.Uranus \t6.Neptune")
planet=int(input("Which planet are you visiting?"))
venus=0.78
mars=0.39
jupiter=2.65
satrun=1.17
uranus=1.05
neptune=1.23
if planet==1:
    gravity=(earth_weight)*(venus)
    print(f"Your weight would be {gravity} pounds on that planet")
elif planet==2:
    gravity=(earth_weight)*(mars)
    print(f"Your weight would be {gravity} pounds on that planet")
elif planet==3:
    gravity=(earth_weight)*(jupiter)
    print(f"Your weight would be {gravity} pounds on that planet")
elif planet==4:
    gravity=(earth_weight)*(satrun)
    print(f"Your weight would be {gravity} pounds on that planet")
elif planet==5:
    gravity=(earth_weight)*(uranus)
    print(f"Your weight would be {gravity} pounds on that planet")
elif planet==6:
    gravity=(earth_weight)*(neptune)
    print(f"Your weight would be {gravity} pounds on that planet")
else:
    print("planet not found")



