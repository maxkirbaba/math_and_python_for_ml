import sys

import numpy as np


def main():
    input_data = sys.stdin.read().splitlines()
    n, m = map(int, input_data[0].split())
    matrix = np.array([np.fromstring(line, sep=" ", dtype=int) for line in input_data[1:]])
    transpond_matrix = np.zeros((m, n), dtype=int)

    for i in range(n):
        for j in range(m):
            transpond_matrix[j, i] = matrix[i, j]

    for string in range(m):
        print(*transpond_matrix[string])


if __name__ == "__main__":
    main()
