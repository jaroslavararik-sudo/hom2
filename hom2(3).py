def count_vowels(text):
    vowels = set("аеєиіїоуюяАЕЄИІЇОУЮЯaeiouAEIOU")
    return sum(1 for char in text if char in vowels)
while True:
    user_input = input('Введіть речення:')
    break

result = count_vowels(user_input)
print(f'Ось кількість голосних в реченні: {result}')


