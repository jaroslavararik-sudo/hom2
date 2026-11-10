def square_numbers(numbers_list):
    return [x ** 2 for x in numbers_list]

user_input = input("Введіть числа: ")
numbers = [int(n) for n in user_input.split()]
print(f"Числа піднесені до квадрату: {square_numbers(numbers)}")
