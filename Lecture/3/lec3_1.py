# ignore these and anything related to this 
import time


# X is your Variable aka. codename, and input... is your content
# input is something where you can input something from the terminal
x = input('What is your name?\n')

print("Your name is", x)

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

time.sleep(0.5)

# Basically this meant variable a is equal to variable b is also equal to viarable c which is 15, thus all printed out value will be 15 no matter what variable is being printed.
a = b = c = 15

print(a)
print(b)
print(c)

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

time.sleep(0.5)

# int aka. integar only allows number, str aka. string allows number and words while float will inc decimal.
x = int(input('Insert a number:\n'))
print(x)

y = int(input('Enter another number:\n'))
print (y)

add = x + y
sub = x - y
mult = x * y
div_true = float(x/y)
div_int = x//y
mod = x%y

print("Addition of both number is", add)
print("Substraction of both number is", sub)
print("Multiplication of both number is", mult)
print("Division of both number is", div_true)
print("Division with integar only of both number is", div_int)
print("Modulus or remainder of both number is", mod)

# There are extra stuffs for string I will put it into another file later