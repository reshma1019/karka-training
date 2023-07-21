dup_value=[1,2,3,2,5,1,5]
org_value=[]
for i in dup_value:
    if i not in org_value:
        org_value.append(i)
print("Org_value =",org_value)

"""dup_value=[1,2,3,2,5,1,5]
org_value=set(dup_value)
print(org_value)"""