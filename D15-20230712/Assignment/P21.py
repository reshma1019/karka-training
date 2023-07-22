import P7
height=float(input("Your height in m:"))
weight=int(input("Your weight in kg:"))
BMI=P7. bmi(weight,height)
if BMI<18.5:
    print("BMI Categery:underweight")
if BMI>=18.5 and BMI<=24.9:
    print("BMI Category:normalweight")
if BMI>=25.0 and BMI<=29.9:
    print("BMI Category:overweight")
if BMI>=36.0:
    print("BMI Category:obese")

