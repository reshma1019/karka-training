consumer_data={"consumer_name":"Reshma",
               "eb_reading":[1100,1200,1350,1650,2050]}
def calculate_electricity_bill(consumer_data):
 
  consumer_name=consumer_data["consumer_name"]
  Eb_reading=consumer_data["eb_reading"]
  months=[1,2,3,4,5]
  unit=[]
  bill_amount=[]
 
  for unit in Eb_reading:
    if unit < 100:
      bill_amount.append(0)
      print(unit,bill_amount)
    if unit>=100 and unit<=200:
      bill_amount.append(2*unit)
      print(unit,bill_amount) 
    if unit>=200 and unit<=500:
      bill_amount.append(5*unit)
    if unit>=500 and unit<=1000:
      bill_amount.append(10*unit)
    if unit>1000:
      bill_amount.append(14*unit)
 
  print(months,bill_amount)
  # total_bill=0
  # for bill in bill_amount:
  #   total_bill=total_bill+bill
  #   print(total_bill)
  # dict={"consumer name":consumer_name,
  #      "bill amount":bill_amount,
  #      "total bill amount":total_bill}
  # print(dict)
 
 
   
 
     










calculate_electricity_bill(consumer_data)