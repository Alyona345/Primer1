# Линейный способ
from sympy import *

k, T, C, L = symbols("k T C L ")
C_ost = 30000
Am_lst_5 = []
C_ost_lst_5 = []
for i in range(7):
    Am = (C - L) / T
    C_ost -= Am.subs({C: 30000, T: 7, L: 0})
    Am_lst_5.append(round(Am.subs({C: 30000, T: 7, L: 0}), 2)) #Что это означает? Ответ от Лысенковой: это округление значения Am до двух знаков после запятой и добавление в список Am_lst_5. Гринина А.: верно
    C_ost_lst_5.append(round(C_ost, 2))
print("Индивидуальное задание: расчёт линейным способом")
print("Am_lst_5:", Am_lst_5)
print("C_ost_lst_5:", C_ost_lst_5)

# Способ уменьшаемого остатка
Aj = 0
C_ost = 30000
Am_lst_6 = []
C_ost_lst_6 = []
for i in range(7):
    Am = k * 1 / T * (C - Aj)
    C_ost -= Am.subs({C: 30000, T: 7, k: 2})
    Am_lst_6.append(round(Am.subs({C: 30000, T: 7, k: 2}), 2))
    Aj += Am
    C_ost_lst_6.append(round(C_ost, 2))
print("Индивидуальное задание: расчёт способом уменьшаемого остатка")
print("Am_lst_6:", Am_lst_6)
print("C_ost_lst_6:", C_ost_lst_6)

# табличное представление
import pandas as pd

Y = range(1, 8)
table1 = list(zip(Y, C_ost_lst_5, Am_lst_5))
table2 = list(zip(Y, C_ost_lst_6, Am_lst_6)) #Что это означает? Ответ от Лысенковой: это объединение списков в кортежи и создание списка кортежей. Гринина А.: верно
tfame = pd.DataFrame(table1, columns=["Y", "C_ost_lst_5", "Am_lst_5"]) 
tfame2 = pd.DataFrame(table2, columns=["Y", "C_ost_lst_6", "Am_lst_6"])
print(tfame)
print(tfame2)

# визуализация
import numpy as np
import matplotlib.pyplot as plt

plt.plot(tfame["Y"], tfame["C_ost_lst_5"], label="Am_5")
plt.savefig("chart7.png")
plt.figure()
plt.plot(tfame2["Y"], tfame2["C_ost_lst_6"], label="Am_6")
plt.savefig("chart8.png")

vals = Am_lst_5
labels = [str(x) for x in range(1, 8)]
explode = (0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15) #Что это означает? Ответ от Лысенковой: это расстояние между фрагментами круговой диаграммы. Гринина А.: верно
fig, ax = plt.subplots()
ax.pie(
    vals,
    labels=labels,
    autopct="%1.1f%%",
    shadow=True,
    explode=explode,
    wedgeprops={"lw": 1, "ls": "--", "edgecolor": "k"},
    rotatelabels=True,
)
ax.axis("equal")
plt.savefig("chart9.png")

vals = Am_lst_6
labels = [str(x) for x in range(1, 8)]
explode = (0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15)
fig, ax = plt.subplots()
ax.pie(
    vals,
    labels=labels,
    autopct="%1.1f%%",
    shadow=True,
    explode=explode,
    wedgeprops={"lw": 1, "ls": "--", "edgecolor": "k"},
    rotatelabels=True,
)
ax.axis("equal")
plt.savefig("chart10.png")

table1 = list(zip(Y, Am_lst_5))
table2 = list(zip(Y, Am_lst_6))
tfame = pd.DataFrame(table1, columns=["Y", "Am_lst_5"])
tfame2 = pd.DataFrame(table2, columns=["Y", "Am_lst_6"])
plt.figure()
plt.bar(tfame["Y"], tfame["Am_lst_5"])
plt.savefig("chart11.png")
plt.figure()
plt.bar(tfame2["Y"], tfame2["Am_lst_6"])
plt.savefig("chart12.png")

# 1 задание
print("Секретные ключи")
import os
S1_LYSENKOVA = os.environ["S1_LYSENKOVA"]
print(S1_LYSENKOVA)
S2_LYSENKOVA = os.environ["S2_LYSENKOVA"]
print(S2_LYSENKOVA)
S3_LYSENKOVA = os.environ["S3_LYSENKOVA"]
print(S3_LYSENKOVA)

# Задание 2 (проверила Алеся) вариант 3
# Проверила Вотинцева А.С.: оценка 5(все верно)
#Задание 3: 
#Задание 4: выполняла с Лысенковой М., все ответы правильные, оценка 5
#Задание 5: создала скрипт оболочки Grinina1.sh
#Задание 6: связала аккаунт на GitHub с Replit

