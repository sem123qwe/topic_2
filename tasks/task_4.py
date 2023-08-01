price: int = 50
quantity: int = 3
total_cost: int = int(price) * int(quantity)  # здесь Ваш код
print(str(int(total_cost)))
print(str(int(price)))
print(str(int (quantity)))
print('Вы должны заплатить', total_cost, 'рублей за', quantity, 'единице товара по цене', price, 'рублей за единицу')
