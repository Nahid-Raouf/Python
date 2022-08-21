number1 = float(input ("Enter the radius of the cylinder: "))
number2 = float(input ("Enter the height of the cylinder: "))
SideArea = 2 * number1 * 3.14 * number2 
V = 3.14 * number1 * number1 * number2
totalArea = 2 * 3.14 * number1 * number1 + 2 * 3.14 * number1 * number2
print("Side Area:", SideArea)
print("cylinder volume:", V)
print("TotalArea:", totalArea)