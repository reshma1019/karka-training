names=[{"name":"Reshma",
        "age":21,
        "place":"Panachamoodu",
        
        },
        {
        "name":"Devi priya",
        "age":21,
        "place":"Aralvaimozhi",
        
        },
        {
        "name":"Ashwin Kumar",
        "age":20,
        "place":"Nagarcovil",
        
        },
        {
        "name":"Rabin",
        "age":22,
        "place":"Ramanputhoor",
        },
        {
        "name":"Kavish",
        "age":21,
        "place":"Vadasery",
        
        },
        {
        "name":"Sulebha",
        "age":22,
        "place":"Panakudi",
        
        },
        {
        "name":"Rashika",
        "age":21,
        "place":"vadasery",
        
        },
    ]
def personal_details(names):
    for i in names:
        name=i["name"]
        age=i["age"]
        place=i["place"]
        print(f"I am {name},I'm {age} years old,and I'm from {place}.\n")

   
        if i["age"]>21:
            print(f"I am {name} ,and I'm from {place}.")
    
personal_details(names)