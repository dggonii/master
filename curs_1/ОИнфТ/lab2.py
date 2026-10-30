import numpy as np
import math
import matplotlib.pyplot as plt


def f(x):
    return 0.1 * x ** 3 + x ** 2 - 10 * np.sin(x)


def calculate_matrix_values(f, ab, m):
    x = np.array([ab[0] + (i - 1) * (ab[1] - ab[0]) / (m - 1) for i in range(1, m + 1)])
    y = f(x)
    return np.column_stack([x, y]) 


def N1(x_t, xy_left, xy_right):

    (x1, y1) = xy_left
    (x2, y2) = xy_right

    k = (y2 - y1) / (x2 - x1)
        
    return y1 + (x_t - x1) * k


def calculate_pnl(x_t, matrix, m):

    if not (matrix[0][0] <= x_t <= matrix[m - 1][0]):

        print("x_t за пределами таблицы")
        return None

    i = 1

    for i in range(1, m):
        if x_t <= matrix[i][0]:
            break

    return N1(x_t, matrix[i-1], matrix[i])


def error_d(fx, pnl_x):
    return fx - pnl_x

print("----PNL Линейная интерполяция Ньютона----")

ab = [-4, 2]

m = 11

n = 2

print("- Интервал [a, b]: ", ab)
print(f"- Количество точек m = {m}; неизвестных параметров n = {n}")
print("- Функция f(x): 0.1 * x^3 + x^2 - 10sin(x)")

# Таблица значений
matrix = calculate_matrix_values(f, ab, m)
print("- Матрица значений размера : ", matrix.shape)
print(matrix)

# Контрольные 21 точка
x_j = np.array([ab[0] + (j-1)*(ab[1] - ab[0])/20 for j in range(1, 22)])

fx = f(x_j)
print(f"\n- Полученные значения функции f(x_j) для 21 точек: ", end="")
print(", ".join(map("{:.2f}".format, fx)))



pnl = np.array([calculate_pnl(x, matrix, m) for x in x_j])

print(f"\n- PNL для 21 точек : ", end="")
print(", ".join(map("{:.2f}".format, pnl)))



d = error_d(fx, pnl)

print(f"\n- Погрешность: ")
print(", ".join(map("{:.2f}".format, pnl)))


# 3) Графики
xs = np.linspace(ab[0], ab[1], 400)
plt.plot(xs, f(xs), label='f(x)')
plt.plot(xs, [calculate_pnl(x, matrix, m) for x in xs], '--', label='PNL')
plt.plot(matrix[:, 0], matrix[:, 1], 'o')
plt.plot(x_j, d, '.', label='d(x)')
plt.legend(); plt.grid(); plt.show()
