"""
Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк.
"""

ask_time = "Enter time \n"
a = input(ask_time)
a = int(a)
h = ((a // 3600)) % 24
m = (a // 60) % 60
s = a % 60

print('%d:%02d:%02d' % (h, m, s))
