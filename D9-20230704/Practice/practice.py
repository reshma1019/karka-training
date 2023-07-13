#list
fruits=["Apple","Strawbery","Mango","Grapes","pinapple","watermelon","lichi"]
print(len(fruits))
#print fruits with index no
for i,fruit in enumerate(fruits):
    print(str(i)+" "+fruit)

#print first 5 fruits
for i,fruit in enumerate(fruits):
  if(i<=5):
    print(fruit)
  else:
    break
#only print 3rd index fruit
for i,fruit in enumerate (fruits):
   if i==1:
      print(fruit)
#print last 3 index fruits
fruits=["Apple","Strawbery","Mango","Grapes","pinapple","watermelon","lichi"]
for i,fruit in enumerate(fruits):
     if(i<=3):
      continue
     else:
      print(fruit)

