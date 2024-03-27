h_age = int(input("Input a dog's age in human years: "))

if h_age < 0:
    print("Age must be positive number.")
    exit()
elif h_age <= 1:
    d_age = h_age * 15
elif h_age <= 2:
    d_age = 15 + 9
else:
    d_age = (15 + 9) + ((h_age - 2) * 5)
    print("The dog's age in dog's years is", d_age)