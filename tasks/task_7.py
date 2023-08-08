cost: int = 1000
discount: int = 20
quantity: int = 3

sum_without_discount: int = cost * quantity

total_cost: float = (
        sum_without_discount - (sum_without_discount * discount / 100)
)

print('стоимость вашего заказа:', total_cost, 'рублей')
