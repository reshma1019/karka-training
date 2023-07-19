item_list=[{"name":"Chess",
            "category":"Indoor game"},
           {"name":"Ludo",
            "category":"Indoor game"},
           {"name":"Football",
            "category":"Outdoor game"},
           {"name":"Hide and seek",
            "category":"Indoor game"},
           {"name":"Hockey",
            "category":"Outdoor game"},
           {"name":"Cricket",
            "category":"Outdoor game"}
           ]
indoor=[]
outdoor=[]

for item in item_list:
    if item["category"]=="Indoor game":
     indoor.append(item["name"])
    if item["category"]=="Outdoor game":
     outdoor.append(item["name"])
    
# print(indoor)
# print(outdoor)
dic_name={"Indoor game":indoor,"Outdoor game":outdoor}
print(dic_name)



    





