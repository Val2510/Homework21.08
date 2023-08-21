# Задача 10: На столе лежат n монеток.
# Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть,
# чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть

print("Введите количество монет на столе: ")
n = int(input())
if n <= 0:
    print("Число должно быть больше ноля!")
else:
    print("Введите по порядку какой стороной лежат монеты: E или R через пробел")
    coins = input().split()
    eagle = sum(coin == 'E' for coin in coins)
    result = min(eagle, len(coins) - eagle)
    print("Минимальное количество монет, которое надо перевернуть: ")
    print(result)
