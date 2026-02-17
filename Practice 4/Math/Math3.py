import math

n = int(input("Input number of sides: "))
length = float(input("Input the length of a side: "))

area = (n * length ** 2) / (4 * math.tan(math.pi / n))
print("The area of the polygon is:", area)
