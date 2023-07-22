consumer_data={"consumer_name":"Reshma",
               "eb_reading":[1100,1200,1350,1650,2050,2500,3800]}
def calculate_electricity_bill(consumer_data):

    eb_reading=consumer_data["eb_reading"]
    output=[]
    
    
    for i in range(len(eb_reading)-1):
        unit_consumed=eb_reading[i+1] - eb_reading[i]
        # print(unit_consumed)
        month=i+1
        bill_amount=0
        
        if unit_consumed <100:
            bill_amount=bill_amount+0
         
      
        elif unit_consumed>=100 and unit_consumed<200:
            bill_amount=bill_amount+(2*unit_consumed)
      
        elif unit_consumed>=200 and unit_consumed<500:
            bill_amount=bill_amount+(5*unit_consumed)

        elif unit_consumed>=500 and unit_consumed<1000:
            bill_amount=bill_amount+(10*unit_consumed)

        elif unit_consumed>1000:
            bill_amount=bill_amount+(14*unit_consumed)
        # print(bill_amount)
    
        dict={"Month":month,"unit_consumed":unit_consumed,"bill_amount":bill_amount}
        output.append(dict)
    print(output)
    total=0
    total=total+bill_amount
    print("total amount:",total)
    

    
    s=str(output)
    print(s)
    file_name="/home/reshma/resh.txt"
    with open(file_name,"w")as file:
        file.write(s)


    text=""
    for data in output:
        text=text+f"Month:{data['Month']},\nUnit_consumed:{data['unit_consumed']},\nBill amount:{data['bill_amount']}\n\n"
        file_name="/home/reshma/resh.txt"
        with open(file_name,"w")as file:
            file.write(text)
        
    


calculate_electricity_bill(consumer_data)
