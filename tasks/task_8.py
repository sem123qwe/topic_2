oklad: int = 50000  # рублей
tax_rate: float = 0.13  # 13% в десятичном виде

tax: float = oklad * tax_rate
salary: float = oklad - (oklad * tax_rate)

print('Размер зарплаты:', oklad, 'рублей')
print('Размер подоходного налога:', tax, 'рублей')
print('Сумма на руки:', salary, 'рублей')
