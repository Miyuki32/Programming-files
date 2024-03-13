import locale

locale.setlocale(locale.LC_ALL, 'en_MY')

local_cur = locale.currency

pen = float(0.89)
pencil = float(0.55)
paper = float(6.79)
ruler = float(0.45)

print('''Rainbow Stationary
~*************************~
Enter the quantity of item purchased:
''')

pur_pen = int(input('Pen: '))
pur_pencil = int(input('Pencil: '))
pur_paper = int(input('A4 Paper: '))
pur_ruler = int(input('Ruler: '))

print('~*************************~')

total_pen = float(pur_pen*pen)
total_pencil = float(pur_pencil*pencil)
total_paper = float(pur_paper*paper)
total_ruler = float(pur_ruler*ruler)
total_pur = float(total_pen + total_pencil + total_paper + total_ruler)

print(pur_pen, "Pen(S):", local_cur(total_pen))
print(pur_pencil, "Pencil(S):", local_cur(total_pencil))
print(pur_paper, "Paper(S):", local_cur(total_paper))
print(pur_ruler, "Ruler(S):", local_cur(total_ruler))
print('Total purchase:', local_cur(total_pur))

print('~*************************~')

paid = float(input('Amount paid: '))

balance = float(paid - total_pur)

print('Your balance:', local_cur(balance))





