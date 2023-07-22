name=input("Hey, What's your name?")
Age=int(input(f"Ok,{name}, how old are you?"))
if Age<16:
 print(f"You can't drive, {name}.")
if Age<18:
  print(f"You can't vote, {name} .")
if Age<25:
  print(f"You can't rent a car, {name} .")
if Age>=25:
   print(f"You can do anything that's legal, {name} .")
                                 
