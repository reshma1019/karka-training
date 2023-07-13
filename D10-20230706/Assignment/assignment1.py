#find sum of list 
numbers=[10,20,30,40,50]
sum=0
for number in numbers:
      print("before",sum)
      sum=number+sum
      print("after",sum)
print("total",sum)

#find average
numbers=[10,20,30,40,50]
sum=0
for number in numbers:
   sum=number+sum
print(sum)
average=sum/len(numbers)
print("Average of these numbers is",average)


#print a cost of list with currency code
prods=[100,200,300,400]
currency_code="INR"
a=[]
for prod in prods:
    concatenate=currency_code+" "+str(prod)
    a.append(concatenate)
print(a)









































































"""numbers=[30,70,89,50,50]
sum=0
enum_numbers=enumerate(numbers)
print(type(enum_numbers))
for i,number in enum_numbers:
   print("entering iteration process for item#:"+str(i))
   print("before sum",sum)
   sum=sum+number
   print("after sum",sum)
   print("exiting iteration process for item#:"+str(i))
   print("\n")"""