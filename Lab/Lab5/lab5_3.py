a = float(input("Input the length of side1: "))
b = float(input("Input the length of side2: "))
c = float(input("Input the length of side3: "))

if (a < (b + c)) and (b < (a + c)) and (c < (a + b)):
    print("It is a triangle!")

else:
    print("It is not a triangle")