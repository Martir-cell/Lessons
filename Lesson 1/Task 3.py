"""
Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3.
Считаем 3 + 33 + 333 = 369.
"""

ask_number = "Enter number\n"
n = input(ask_number)
a = int(n + n)
b = int(n+n+n)
result = int(n) + a + b

print(result)
