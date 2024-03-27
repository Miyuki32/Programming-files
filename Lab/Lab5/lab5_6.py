import locale
locale.setlocale(locale.LC_ALL, 'en_MY')

print(
"""
B & B Inn
Breakfast Menu
[A]merican Breakfast\t(RM12.50)
[C]hinese Porridge]\t(RM 6.30)
[N]asi Lemak\t\t(RM 5.50)
[F]ried Noodle\t\t(RM 5.50)
[L]aksa\t\t\t(RM 5.30)
[M]ee mamak\t\t(RM 4.80)
""")

cus_selection =  input("What would you like to order? (A/C/N/F/L/M) ").upper()
amt = int(input("How many portion? "))

selection = cus_selection.upper()

if selection == 'A':
    total = amt * 12.50
elif selection == 'C':
    total = amt * 6.30
elif selection == 'N':
    total = total = amt * 5.50
elif selection == 'F':
    total = amt * 5.50
elif selection == 'L':
    total = amt * 5.30
elif selection == 'M':
    total = amt * 4.80

else:
    print('Invalid input')
    total = 0

print("Total:", locale.currency(total))

