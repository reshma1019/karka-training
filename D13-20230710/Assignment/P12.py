Quiz=input("Are you ready for a quizz?")
ans="Y" or "N"

if Quiz=="Y":
    print("Okay,here it comes!\n")
if Quiz=="N":
    print("Thankyou")
total_score=0

qn_1=int(input("Q1) What is the capital of India?\n\t1.Amaravathi \n\t2.Hyderabad \n\t3.New Delhi \n>"))
if (qn_1==3):
    print("That's right! \n")
    total_score=total_score + 1

else:
    print("wrong answer \n")
    
qn_2=int(input("Q2) Can you store the value 'cat' in a variable of type int?\n\t1.yes \n\t2.no \n>"))
if qn_2==2:
    print("That's correct! \n")
    total_score=total_score+1
else:
    print("Sorry,'cat' is a string.ints can only store numbers.\n")
    

qn_3=int(input("Q3) What is the result of 35/5?\n\t1.5 \n\t2.7 \n\t3.8 \n>"))   
if qn_3==2:
    print("That's correct! \n")
    total_score=total_score+1
else:
    print("Wrong answer \n")

    
print(f"overall, you got {total_score} out of  3  correct. \nThanks for playing!")