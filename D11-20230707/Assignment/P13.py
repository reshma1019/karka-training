print("TWO QUESTIONS!\nThink of an object, and I'll try to guess it.")

qn_1=input("\nQuestion 1) Is it animal, vegetable, or mineral?\n>")
qn_2=input("\nQuestion 2) Is it bigger than a breadbox?\n>")
if qn_1=="animal":
   if qn_2=="yes":
      print("\nMy guess is that you are thinking of mouse.\nI would ask you if I'm right, but I don't actually care.")
   elif qn_2=="no":
        print("My guess is that you are thinking of squirrel")
   else:
       print("invalid comment")

if qn_1=="mineral":
   if qn_2=="yes":
      print("My guess is that you are thinking of camaro.\nI would ask you if I'm right, but I don't actually care.")
   elif qn_2=="no":
      print("My guess is that you are thinking of paper clip ")
   else:
      print("invalid comment")


if qn_1=="vegetable":
   
   if qn_2=="yes":
      print("My guess is that you are thinking of watermelon.\nI would ask you if I'm right, but I don't actually care.")
   elif qn_2=="no":
      print("My guess is that you are thinking of carrot ")
   else:
      print("invalid comment")