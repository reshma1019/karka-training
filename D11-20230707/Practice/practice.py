n=int(input("enter a row:"))
pattern=""
for i in range(1,n+1):
    if (i % 2) == 0:
        pattern=pattern+"*"
        pattern=pattern+str(i)
        
        print(pattern)
        
