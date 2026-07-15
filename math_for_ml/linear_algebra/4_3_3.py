import sys

import numpy as np


def main():
    input_data = sys.stdin.read().splitlines()
    matrix = np.array([np.fromstring(line, sep=" ", dtype=int) for line in input_data[1:]])
    verification_matrix = np.zeros_like(matrix)
    resulting_matrix = matrix.copy()

    if np.array_equal(matrix, verification_matrix):
        print(1)

    else:
        for k in range(2, 101):
            resulting_matrix = matrix @ resulting_matrix
            if not np.any(resulting_matrix):
                print(k)
                return


if __name__ == "__main__":
    main()
