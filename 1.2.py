import numpy as np
import matplotlib.pyplot as plt

with open('frames.dat.txt', 'r', encoding="utf-8") as file:
    income_data = file.read().split('\n')
for i in range(len(income_data)):
    income_data[i] = income_data[i].split(' ')

x = []
y = []

for i in range(len(income_data) - 1):  # -1 так как в конце есть одна пустая ячейка
    for j in range(len(income_data[i])):  # кол-во чисел в строке
        if i % 2 == 0:
            x.append(np.double(income_data[i][j]))  # четные - х
        else:
            y.append(np.double(income_data[i][j]))  # нечетные - у
    if i % 2 == 1:  # отрисовка каждого кадра
        num = i // 2 + 1  # номер текущего кадра
        plt.subplot(2, 3, num)  # задаем расположение каждого кадра (2 на 3, место текущего)
        plt.plot(x, y)
        plt.title('Frame' + str(num))
        plt.grid()  # создаем сетку
        # размерность сетки
        plt.xticks(np.arange(0, 16, 2))
        plt.yticks(np.arange(-10, 14, 2))
        x = []
        y = []
plt.tight_layout()  # чтобы графики не накладывались друг на друга
plt.show()
plt.savefig('frames.png')
