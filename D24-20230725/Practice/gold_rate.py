monthly_gold_rate=[{"month":"January",
                    "gold_rate":3000,
                    "jewel_list":[{"name":"Chain",
                                   "making_cost":12},
                                  {"name":"Earings",
                                    "making_cost":10},
                                  {"name":"Ring",
                                    "making_cost":15}]
                    },
                    {"month":"February",
                   "gold_rate":1000,
                   "jewel_list":[{"name":"Chain",
                                   "making_cost":12},
                                  {"name":"Earings",
                                    "making_cost":10},
                                  {"name":"Ring",
                                    "making_cost":15}]
                    },
                    {"month":"March",
                     "gold_rate":5600,
                     "jewel_list":[{"name":"Chain",
                                   "making_cost":12},
                                  {"name":"Earings",
                                    "making_cost":10},
                                  {"name":"Ring",
                                    "making_cost":15}]
                    },
                    {"month":"April",
                    "gold_rate":2000,
                    "jewel_list":[{"name":"Chain",
                                   "making_cost":12},
                                  {"name":"Earings",
                                    "making_cost":10},
                                  {"name":"Ring",
                                    "making_cost":15}]
                    }]


for gold in monthly_gold_rate:
    gold_rate=gold["gold_rate"]
    jewel_list=gold["jewel_list"]
    month=gold["month"]
    for i in gold["jewel_list"]:
      jewel_name=i["name"]
      percentage=gold["gold_rate"]*i["making_cost"]/100
      total_cost=percentage+gold_rate
      print(f"Month:{month}\nGold Rate:{gold_rate}\n{jewel_name} Rate:{total_cost}\n")


    


    
    


