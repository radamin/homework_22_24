# Task 22
# Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые
# встречаются в обоих наборах.
# Пользователь вводит 2 числа, n - кол-во элементов первого множества,
# m - кол-во элементов второго множества.
# Затем пользователь вводит сами элементы множеств.
# Выдать в порядке возрастания уникальные числа, из двух списков
# Пример:
# 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18
# 6 12"

import random
import time

n = (int(input("Введите количество элементов первого списка: ")))
m = (int(input("Введите количество элементов второго списка: ")))
start = time.perf_counter()
first = [random.randint(-10, 10) for _ in range(n)]
second = [random.randint(-10, 10) for _ in range(m)]

print(*sorted(first), sep="\t")
print(*sorted(second), sep="\t")

result = list()
for i in first:
    for j in second:
        if i == j:
            result.append(i)
print(*sorted(set(result)), sep="\t")
end = time.perf_counter()
time = end - start
print(f"Script execution time: {time}")
