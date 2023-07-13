#area of a traingle
def area_of_traingle():
    a=int(input("a="))
    b=int(input("b="))
    c=int(input("c="))
    s=(a+b+c)/2
    area_of_traingle=(s*(s-a)*(s-b)*(s-c))**0.5
    print("The area of a traingle is",area_of_traingle)
area_of_traingle()

#area of a square
def area_of_square():
    side=int(input("a="))
    Area=side*side
    print("The area of a square is",Area)
area_of_square()

#area of a rectangle
def area_of_rectangle():
    length=int(input("l="))
    width=int(input("w="))
    Area=length*width
    print("The Area of a rectangle is",Area)
area_of_rectangle()

#area of a circle
def area_of_circle():
    radius=int(input("r="))
    Area=3.14*radius**2
    print("The Area of a circle is",Area)
area_of_circle()


#area of a trapezium
def area_of_Trapezoid():
    base_a=int(input("a="))
    base_b=int(input("b="))
    height=int(input("h="))
    Area=(base_a+base_b/2)*height
    print("The area of a Trapezoid",Area)
area_of_Trapezoid()






    
