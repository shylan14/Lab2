def check_empty_string(input_string):
    return None if not input_string else input_string


user_input = input("Введіть рядкове значення: ")
result = check_empty_string(user_input)
print("Результат:", result)
