import random

R = float(input("Введите радиус мишени R: "))
N = 10000  # количество выстрелов (для точности)

hits = 0
print("-" * 45)
print(f"{'№':>3} | {'x':>8} | {'y':>8} | результат")
print("-" * 45)

for i in range(1, N + 1):
    # генерируем точки в квадрате [-R, R] x [-R, R]
    x = random.uniform(-R, R)
    y = random.uniform(-R, R)

    inside_circle = (x * x + y * y) <= R * R

    popal = False
    if inside_circle:
        # правая верхняя четверть
        if x >= 0 and y >= 0:
            popal = True
        # левая нижняя четверть
        elif x <= 0 and y <= 0:
            popal = True
        # левая верхняя (только под прямой y = -x)
        elif x <= 0 and y >= 0 and y <= -x:
            popal = True

    if popal:
        hits += 1
        result = "ПОПАЛ"
    else:
        result = "мимо"

    # выводим только первые 10 выстрелов, чтобы консоль не зависла от 10000 строк
    if i <= 10:
        print(f"{i:3d} | {x:8.2f} | {y:8.2f} | {result}")

print("-" * 45)
print(f"Всего выстрелов: {N}, попаданий: {hits}")