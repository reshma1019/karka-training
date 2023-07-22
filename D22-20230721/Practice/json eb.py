import json
name=input("enter a name:")
eb_reading1=int(input("enter a 1st reading:"))
eb_reading2=int(input("enter a 2nd reading:"))
eb_reading3=int(input("enter a 3rd reading:"))
eb_reading4=int(input("enter a 4th reading:"))
eb_reading5=int(input("enter a 5th reading:"))
consumer_data={"consumer_name":name,
               "eb_readings":[eb_reading1,eb_reading2,eb_reading3,eb_reading4,eb_reading5]}

consumer_data_json=json.dumps(consumer_data)
consumer_new=json.loads(consumer_data_json)
print(consumer_data_json)
print(consumer_new)
# print(type(consumer_data_json))
# print(type(consumer_new))


        




