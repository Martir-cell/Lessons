"""
Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров. Каждый день
спортсмен увеличивал результат на 10 % относительно предыдущего. Требуется определить номер дня, на который общий
результат спортсмена составит не менее b километров. Программа должна принимать значения параметров a и b и выводить
одно натуральное число — номер дня. Например: a = 2, b = 3.
"""
a = "Enter first day result\n"
b = "Enter last day result\n"
a = input(a)
a = float(a)
b = input(b)
b = float(b)

day = 1
if a > b:
    print(day)
while a < b:
    a = a + a/10
    day += 1
print(day)
