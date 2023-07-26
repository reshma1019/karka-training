# from datetime import datetime
# import pytz
# current_time =pytz. timezone("Asia/Kolkata")
# print(datetime.now(current_time))

# from datetime import datetime

# date_str="26 July 2023"
# print(type(date_str))

# date=datetime.strptime(date_str,"%d %B %Y")
# print(date)

from datetime import timedelta,datetime

date_str="26 July 2023"
date=datetime.strptime(date_str,"%d %B %Y")
end_date=date+timedelta(days=5)
print(end_date)



