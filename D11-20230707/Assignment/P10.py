name=input("Hey,what's your name?(sorry,I keep forgetting..)")
age=int(input(f"Ok, {name}, How old are you?"))
if age<16:
    print(f"you can't drive.{name}!")
if age==16 or age==17:
    print(f"You can drive but not vote. {name}!")
if age>=18 and age<=24:
    print(f"You can vote but not rent a car. {name}!")
if age==25 or age>25:
    print(f"You can do pretty much anything.{name}!")