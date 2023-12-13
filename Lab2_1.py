def calculate_discounted_price(original_price):
    discount = 0
    
    if original_price > 100:
        discount = 3
    if original_price > 500:
        discount = 5
    if original_price > 1000:
        discount = 10
    
    discounted_price = original_price - (original_price * discount / 100)
    return discounted_price


original_price = float(input("Введіть вартість товару: "))
result = calculate_discounted_price(original_price)
print(f"Знижена вартість товару: {result:.2f} грн")
