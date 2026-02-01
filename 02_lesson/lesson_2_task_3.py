

import math

def square(x):
    y = x * x
    if not isinstance(x, int):
        y = math.ceil(y)    # Округляем вверх
    return y

# Ввод стороны от пользователя (можно и целое, и дробное)
side_input = float(input("Введите сторону квадрата: "))

# Вычисляем площадь и выводим
print(f"Площадь квадрата: {square(side_input)}")