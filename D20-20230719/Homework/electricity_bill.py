consumer_data={"consumer_name":"Reshma",
               "eb_reading":[1100,1200,1350,1650,2050,2567,2768,3124,3345,3689,4567,5423]}
def calculate_electricity_bill(consumer_data):
  # print(len("eb_reading"))
  consumer_name=consumer_data["consumer_name"]
  eb_reading=consumer_data["eb_reading"]

  
  for i in range(1,9):
    
     unit_consumed= eb_reading[i] - eb_reading[i-1]
     print(unit_consumed)
     bill_amount=[]
  
     if unit_consumed < 100:
         bill_amount.append(0)
      
     if unit_consumed>=100 and unit_consumed<=200:
        bill_amount.append(2*unit_consumed)
      
     if unit_consumed>=200 and unit_consumed<=500:
       bill_amount.append(5*unit_consumed)

     if unit_consumed>=500 and unit_consumed<=1000:
      bill_amount.append(10*unit_consumed)

     if unit_consumed>1000:
       bill_amount.append(14*unit_consumed)
  print("bill amount:",bill_amount)

  total_bill=0
  for bill in bill_amount:
    total_bill=total_bill+bill
  print()
    
  dict=[{"month":1,
        "unit_consumed":unit_consumed,
        "bill amount":bill_amount[0]},
        {"month":2,
       "unit_consumed":unit_consumed,
       "bill amount":bill_amount[1],
        },
      {"month":3,
      "unit_consumed":unit_consumed,
      "bill amount":bill_amount[2],
       },
      {"month":4,
      "unit_consumed":unit_consumed,
     "bill amount":bill_amount[3],
       },
       ]
  print("dictionary_view:",dict)

 
calculate_electricity_bill(consumer_data)