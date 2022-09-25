import math
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
d = b ** 2 - 4 * a * c
if d > 0:
    x1 = (-b + math.sqrt(d)) / (2 * a)
    x2 = (-b - math.sqrt(d)) / (2 * a)
elif d == 0:
    x = -b / (2 * a)
else:
    print("Корней нет")
