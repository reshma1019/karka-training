def f_or_m_game():
    gender=input("What is your gender (M or F):")
    first_name=input("First Name :")
    last_name=input("Last Name:")
    age=int(input("Age:"))
    
    if gender=="F" and age>=20:
        status=input("Are you married,(y or n)?")
        if status=="y":
            print(f"Then I shall call you Mrs.{first_name}{last_name}")
        
        elif status=="n" :
            print(f"Then I shall call you Ms.{first_name}{last_name}")
        else:
            print(f"Then I shall call you {first_name}{last_name}")
    
        if gender=="M" and age>=20:
         print(f"Then I shall call you Mr.{first_name}{last_name}")
    else:
         print(f"Then I shall call you {first_name}{last_name}")

f_or_m_game()