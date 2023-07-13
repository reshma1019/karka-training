def arithmetic_operations (num_1,operator,num_2):
    if operator=="+":
     return(num_1+num_2)
    if operator=="-":
       return(num_1-num_2)
    if operator=="*":
       return(num_1*num_2)
    if operator=="/":
       return(num_1/num_2)
    if operator=="%":
       return(num_1%num_2)
    if operator=="**":
       return(num_1**num_2)
    else:
       return("operator not found")
    
num_1=int(input("enter a first number="))
operator= input("enter  a operator")
num_2=int(input("enter a third number="))
final_value=arithmetic_operations (num_1,operator,num_2)
print(final_value)



















