import sys

import numpy as np


def main():
    input_data = sys.stdin.read().splitlines()
    m, n = map(int, input_data[0].split())
    matrix = np.array([np.fromstring(line, sep=" ", dtype=float) for line in input_data[1:]])
    column_means = np.mean(matrix, axis=0)
    matrix -= column_means
    column_std = np.std(matrix, axis=0)
    matrix /= column_std

    for i in range(m):
        print(*matrix[i].astype(int))


if __name__ == "__main__":
    main()
