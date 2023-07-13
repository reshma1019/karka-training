#intrest calculation
def calc_intrest(p,n,r):
    intrest=p*n*r/100
    return intrest
p=1000
n=10
r=5
intrest=calc_intrest(p,n,r)
print(intrest)

#twice of a
def twice(a):
    b=2*a
    return(b)
a=20
b=twice(a)
print(b)

#elligiblity check
def passed_out_yr(year):
    if year >=2024:
     return "you are elligible"
    else:
       return "you are not elligible"
   
year=int(input("enter a year:"))   
b=passed_out_yr(year)
print(b)  


    




