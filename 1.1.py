import matplotlib.pyplot as plt

try:
    with open('001.dat', 'r', encoding="utf-8") as file:
        income_data = file.read().split('\n')
    for i in range(1, len(income_data)):
        income_data[i] = income_data[i].split(' ')

    x = []
    y = []
    k = int(income_data[0])
    for i in range(1, k + 1):
        x.append(float(income_data[i][0]))
        y.append(float(income_data[i][1]))

    plt.scatter(x, y)
    # масштабирование
    plt.axis('equal')
    plt.axis('scaled')
    # установка границ, чтобы все точки было хорошо видно
    plt.axis([min(x) - 15, max(x) + 15, min(y) - 15, max(y) + 15])

    plt.title(f'Number of points: {income_data[0]}')
    plt.show()
    plt.savefig('001.png')

except:  # прекратить работу программы при обнаружении данных не по нужному формату (лишние данные)
    pass
