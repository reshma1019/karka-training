passed_out_yr=input("Which year you passed out from college:")
print(passed_out_yr)
#type_of_passed_out_yr=type(passed_out_yr)
#print(type_of_passed_out_yr)
passed_out_yr=int(passed_out_yr)
#type_of_passed_out_yr=type(passed_out_yr)
#print(type_of_passed_out_yr)

#NOT operator
long_hair=True
is_elligible=not long_hair
if is_elligible:
    print("the student is elligible")
else:
    print("the student is not elligible")  
#OR operator
is_elligible=passed_out_yr==2022 or passed_out_yr==2023
print(is_elligible)

#AND operator
is_elligible=passed_out_yr==2022 and long_hair==False 
print(is_elligible)


