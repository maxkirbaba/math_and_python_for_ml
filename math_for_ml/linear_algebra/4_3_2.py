import sys

import numpy as np


def main():
    input_data = sys.stdin.read().splitlines()
    m, n = map(int, input_data[0].split())
    matrix_a = np.array([np.fromstring(line, sep=" ", dtype=int) for line in input_data[1 : 1 + m]])
    h, k = map(int, input_data[m + 1].split())
    matrix_b = np.array([np.fromstring(line, sep=" ", dtype=int) for line in input_data[m + 2 :]])

    result_matrix = np.zeros((m, k), dtype=int)
    if n == h:
        for i in range(m):
            for j in range(k):
                for s in range(n):
                    result_matrix[i, j] += matrix_a[i, s] * matrix_b[s, j]
            print(*result_matrix[i])
    else:
        print("NOT_DEFINED")


if __name__ == "__main__":
    main()
