# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя –
# школьница. Петя помогает Кате по математике.
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна
# их отгадать. Для этого Петя делает две подсказки. Он называет
# сумму этих чисел S и их произведение P. Помогите Кате
# отгадать задуманные Петей числа.

print("Введите сумму двух чисел X и Y:")
S = int(input())
print("Введите произведение двух чисел X и Y:")
P = int(input())

for X in range(1, S + 1):
    if S - X > 0:
        Y = S - X
        if X * Y == P:
            print(X, Y)
            break
    else:
        print("Нет чисел, подходящих под условие")
