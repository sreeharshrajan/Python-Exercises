# Find out an area of a triangle whose base is 15 meter and height is 22 meter. 
# The mathematical equation for an area of a triangle is: Area = ½*Base*Height

def area(base,height):
    return 1/2*(base*height)

base=int(input('enter base : '))
height=int(input('enter height : '))
print('Area of triangle is: ',area(base,height))