import math
a = float(input("enter a num:"))
square = a ** 2
cube = a ** 3 
square_root = math.sqrt(a)
celing_value = math.ceil(a)
floor = a // 2
absloute_value = math.fabs(a)
print(f"square of a: {square}")
print(f"cube of a: {cube}")
print(f"square_root: {square_root}")
print(f"celing_value: {celing_value}")
print(f"floor_div: {floor}")
print(f"absolute_value of a: {absloute_value}")
print(f"type of variable: {type(a)}")
print(f"memory address of a: {id(a)}")