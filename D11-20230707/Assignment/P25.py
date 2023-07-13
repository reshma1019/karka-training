months=["January","February","March","April","May","June","July","August","September","October","November","December"]
def month_name(months):
    if months==1:
        return "January"
    elif months==2:
        return "February"
    elif months==3:
        return "March"
    elif months==4:
        return "April"
    elif months==5:
        return "May"
    elif months==6:
        return "June"
    elif months==7:
        return "July"
    elif months==8:
        return "August"
    elif months==9:
        return "September"
    elif months==10:
        return "October"
    elif months==11:
        return "November"
    elif months==12:
        return "December"
    else:
        return "error! choose between 1 to 12"

result=month_name(12)
print(result)

