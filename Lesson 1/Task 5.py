"""Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым результатом работает фирма
(прибыль — выручка больше издержек, или убыток — издержки больше выручки). Выведите соответствующее сообщение.
Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.
"""
profit = "Enter profit \n"
p = input(profit)
costs = "Enter costs \n"
c = input(costs)
c = int(c)
p = int(p)
if p > c:
    profitability = p-c
    rent = profitability/p
    print(f"Your profitability is {profitability} ")
    employees = "How many employees do you have? \n"
    e = input(employees)
    e = int(e)
    print(f"{profitability/e} is your profit per employee")
elif p == c:
    print("You are not making profit")
else:
    print(f"Your costs are {c - p} higher than your profit")