import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as spi
import random

# Визначення функції та межі інтегрування
def f(x):
    return x ** 2

def monte_carlo_simulation(a, b, num_experiments):
    total_area = 0
    for _ in range(num_experiments):
        N = 15000  # Количество случайных точек в одном эксперименте
        x_rand = [random.uniform(a, b) for _ in range(N)]
        y_rand = [f(xi) for xi in x_rand]
        average_height = sum(y_rand) / N
        area = (b - a) * average_height
        total_area += area
    return total_area / num_experiments
    
a = 0  # Нижня межа
b = 2  # Верхня межа

# Обчислення інтеграла
result, error = spi.quad(f, a, b)

print("Інтеграл: ", result, error)

# Кількість експериментів
num_experiments = 100

# Виконання симуляції
average_area = monte_carlo_simulation(a, b, num_experiments)

print(f"Середня площа за {num_experiments} експериментів: {average_area}")

# Створення діапазону значень для x
x = np.linspace(-0.5, 2.5, 400)
y = f(x)

# Створення графіка
fig, ax = plt.subplots()

# Малювання функції
ax.plot(x, y, 'r', linewidth=2)

# Заповнення області під кривою
ix = np.linspace(a, b)
iy = f(ix)

ax.fill_between(ix, iy, color='gray', alpha=0.3)

# Налаштування графіка
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')

# Додавання меж інтегрування та назви графіка
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Графік інтегрування f(x) = x^2 від ' + str(a) + ' до ' + str(b))
plt.grid()
plt.show()
