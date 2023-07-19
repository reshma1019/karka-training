item_list=[{"name":"Apple",
           "category":"Fruits"},
          {"name":"Carrot",
           "category":"Vegetable"},
          {"name":"Banana",
           "category":"Fruits"},
          {"name":"Broccoli",
           "category":"Vegetable"}
        ]

fruits=[]
vegetable=[]
for item in item_list:
    
    if item["category"]=="Fruits":
        fruits.append(item["name"])
    if item["category"]=="Vegetable":
        vegetable.append(item["name"])
# print(fruits)
# print(vegetable)
dic_name={"Fruits":fruits,"Vegetable":vegetable}
print(dic_name)



    
        


    