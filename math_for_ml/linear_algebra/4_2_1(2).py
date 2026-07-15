import sys

import numpy as np


def main():
    # Настраиваем округление вывода NumPy один раз в начале (опционально)
    # np.set_printoptions(precision=2, suppress=True)

    # Читаем сразу все данные из стандартного ввода, чтобы не вызывать input() многократно
    input_data = sys.stdin.read().splitlines()
    if not input_data:
        return

    k = int(input_data[0])

    # Быстро превращаем вторую строку в массив коэффициентов
    kef = np.fromstring(input_data[1], sep=" ")

    # Собираем оставшиеся строки в матрицу векторов
    # (Создаем матрицу напрямую из среза строк, без циклов for)
    matrix = np.array([np.fromstring(line, sep=" ") for line in input_data[2 : 2 + k]])

    # Главная магия: матричное умножение вектора коэффициентов на матрицу векторов.
    # kef @ matrix сразу делает и умножение, и сложение по столбцам!
    result = kef @ matrix

    # Выводим результат, округлив до 2 знаков
    print(*result.round(2))


if __name__ == "__main__":
    main()
