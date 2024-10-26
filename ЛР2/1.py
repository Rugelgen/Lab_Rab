money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

increase += increase+1
i = 0
while money_capital > 0:

    money_capital = money_capital + salary - (increase**i)*spend
    # print(money_capital)
    i += 1
# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов

print("Количество месяцев, которое можно протянуть без долгов:", i+1)
