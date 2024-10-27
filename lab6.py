# -*- coding: utf-8 -*-
"""Lab6.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1zAE-gYBKhczXn9ZnJXiKSd2lvA8hhkwq
"""

from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.linear_model import LinearRegression
import numpy as np
import math

"""# Практическое задание: перевод из градусов цельсия в градусы фаренгейта

"""

celsius = [[-67.0], [-34.0], [0], [34.0], [54.0], [67.0], [100]]
fahrenheit = [[-88.6], [-29.2], [32-0], [93-2], [129.2], [152.6], [212.0]]

plt.figure(figsize=(15,8), dpi=50)
plt.scatter (celsius, fahrenheit, label='вxодные значения', color='green', marker='$f$')
plt.xlabel('celsius')
plt.ylabel('fahrenheit')
plt.legend()
plt.grid(True)
plt.show()

for c, f in zip(celsius, fahrenheit):
    print(f'цельсия{c} = фаренгейт{f}')

lr = LinearRegression()
lr.fit(celsius, fahrenheit)
lr.predict([[256], [123]])
lr.coef_
lr.intercept_
celsius_test = [[-50], [10], [30], [20], [10], [70], [87]]
fahrenheit_test= lr.predict(celsius_test)
fahrenheit_test

for c, f in zip(celsius_test, fahrenheit_test):
    print(f'цельсия{c} = фаренгейт{f}')

x_range = np.arange(-70, 120)
y_range = x_range*1.8+32
plt.figure(figsize=(15,8), dpi=50)
plt.plot(x_range, y_range, label='уравнение', linewidth='1')
plt.scatter(celsius, fahrenheit, label='вxодныe данные', color='green')
plt.scatter(celsius_test, fahrenheit_test, label='предсказанное значение', color='blue')
plt.xlabel('Цельсия')
plt.ylabel('Фaренгейта')
plt.legend()
plt.grid(True)
plt.show()

"""# 1. Возьмите систему мер перевода из фаренгейта в кельвины и проделайте с ними все те же операции что проводились с цельсиями и фаренгейтами.
(стартовые данные вы должны вычислить и занести сами)


"""

fahrenheit = [[-40], [32], [212], [100], [150], [200], [300]]
# Пересчитываем температуру в Кельвинах по формуле, и наполняем ей массив
kelvin = []
for t in fahrenheit:
    kelvin.append([(t[0] - 32) * 5/9 + 273.15])

plt.figure(figsize=(15,8), dpi=50)
plt.scatter(fahrenheit, kelvin, label='вxодные значения', color='green', marker='$f$')
plt.xlabel('Фаренгейт')
plt.ylabel('Кельвин')
plt.legend()
plt.grid(True)
plt.show()

lr = LinearRegression()
lr.fit(fahrenheit, kelvin)
lr.predict([[256], [123]])
lr.coef_
lr.intercept_
fahrenheit_test = [[-50], [10], [30], [20], [10], [70], [87]]
kelvin_test = lr.predict(fahrenheit_test)
kelvin_test

x_range = np.arange(-70, 320)
y_range = (x_range - 32) * 5/9 + 273.15
plt.figure(figsize=(15,8), dpi=50)
plt.plot(x_range, y_range, label='уравнение', linewidth='1')
plt.scatter(fahrenheit, kelvin, label='вxодные значения', color='green')
plt.scatter(fahrenheit_test, kelvin_test, label='предсказанное значение', color='blue')
plt.xlabel('Фаренгейт')
plt.ylabel('Кельвин')
plt.legend()
plt.grid(True)
plt.show()

"""# 3.  Используя документацию библиотеки matplotlib выведите графики трёх типов которые не рассматривались в лабораторной работе, с данными на ваше усмотрение

"""

# 1 - столбчатая

cities = ['Москва', 'Санкт-Петербунг', 'Новосибирск', 'Екатеринбург', 'Казань']
population = [12506468, 5351935, 1597000, 1495000, 1253000]

plt.figure(figsize=(10,6))
plt.bar(cities, population)
plt.xlabel('Город')
plt.ylabel('Население')
plt.title('Население крупнейших городов России')
plt.show()

# 2 - стволовая диаграмма
months = ['Янв', 'Фев', 'Мар', 'Апр', 'Май', 'Июнь', 'Июль', 'Авг', 'Сен', 'Окт', 'Ноя', 'Дек']
temperature = [2, 4, 8, 14, 18, 22, 24, 23, 18, 12, 6, 3]

plt.figure(figsize=(10,6))
plt.stem(months, temperature)
plt.xlabel('Месяц')
plt.ylabel('Температура (°C)')
plt.title('Средняя месячная температура')
plt.show()

#3 - круговая

brands = ['Samsung', 'Apple', 'Xiaomi', 'Oppo', 'Vivo', 'Huawei']
market_share = [25, 20, 15, 10, 10, 20]

plt.figure(figsize=(8,8))
plt.pie(market_share, labels=brands, autopct='%1.1f%%')
plt.title('Продажи смартфонов')
plt.show()

"""# 4.  Подключите библиотеку math и выведите

"""

# Число Эйлера
print("Число Эйлера:", math.e)

# Число Пи
print("Число Пи:", math.pi)

# nan
print("nan:", math.nan)

# Факториал числа 10
print("Факториал числа 10:", math.factorial(10))

# Наибольший делитель для чисел 10 и количества памяти телефона
memory_gb = 256
print("НОД для чисел 10 и количества памяти телефона:", math.gcd(10, memory_gb))

"""# Задания повышенной сложности:
# 1.  При помощи функционала библиотеки matplotlib, используя графики нарисуйте сложную фигуру или котика.

"""

fig = plt.figure(figsize=(10,8))
ax = fig.add_subplot(111, projection='3d')

# Генерация данных
theta = np.linspace(0, 2*np.pi, 100)
z = np.linspace(0, 1, 100)
t, Z = np.meshgrid(theta, z)
X = np.cos(t)
Y = np.sin(t)

# Настройка и расположение
ax.plot_surface(X, Y, Z, cmap='viridis')
ax.grid(False)
ax.set_title('Цилиндр')

plt.show()