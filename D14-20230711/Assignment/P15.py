def game():
    print("TWO QUESTIONS BABY!\n\nThink of something and I'll try to guess it!\n")
    qn_1=input("Question 1) Does it stay inside or outside or both?")
    qn_2=input("Question 2) Is it a living thing?")   
    if qn_1=="inside" and qn_2=="yes":
     print("It's a houseplant")
    if qn_1=="inside" and qn_2=="no":
     print("It's a shower curtain")
    if qn_1=="outside" and qn_2=="yes":
     print("It's a bison")
    if qn_1=="outside" and qn_2=="no":
     print("It's a billboard")
    if qn_1=="both" and qn_2=="yes":
     print("It's a dog")
    if qn_1=="both" and qn_2=="no":
     print("It's a cell phone")
    if qn_1!="inside" and qn_1!="outside" and qn_1!= "both" and qn_2!="yes" and qn_2!="no":
     print("\nThen what else could you be thinking of besides a python?!?")
    
game()